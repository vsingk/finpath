"""
Signals for automatic syncing between budget expenses and goal contributions.
"""
from django.db.models.signals import post_delete, pre_delete
from django.dispatch import receiver
from decimal import Decimal
import logging

from .models import GoalContribution, GoalAllocation, MonthlyAllocation

logger = logging.getLogger(__name__)


@receiver(pre_delete, sender=GoalContribution)
def sync_contribution_deletion(sender, instance, **kwargs):
    """
    When a goal contribution is deleted:
    1. Subtract from goal's current amount
    2. Delete corresponding budget expense (if exists)
    3. Delete corresponding GoalAllocation record (so goal can be re-allocated)
    """
    try:
        from budgets.models import Expense
        
        # 1. Update goal balance
        goal = instance.goal
        goal.current_amount = max(goal.current_amount - instance.amount, Decimal('0'))
        goal.save()
        logger.info(f"Updated {goal.name} balance: -{instance.amount}")
        
        # 2. Find and delete corresponding budget expense
        expense = Expense.objects.filter(
            user=goal.user,
            amount=instance.amount,
            date=instance.date,
            description__icontains=goal.name,
        ).first()
        
        if expense:
            # Temporarily disconnect signals to avoid infinite loop
            from budgets.models import Expense as ExpenseModel
            post_delete.disconnect(sync_expense_deletion, sender=ExpenseModel)
            
            expense.delete()
            logger.info(f"Deleted corresponding expense: ${expense.amount}")
            
            # Reconnect signals
            post_delete.connect(sync_expense_deletion, sender=ExpenseModel)
        
        # 3. Delete the GoalAllocation record so the goal can be re-allocated
        contribution_month = instance.date.replace(day=1)
        monthly_allocation = MonthlyAllocation.objects.filter(
            user=goal.user,
            month=contribution_month
        ).first()
        
        if monthly_allocation:
            # Delete the goal allocation record
            deleted_count = GoalAllocation.objects.filter(
                monthly_allocation=monthly_allocation,
                goal=goal,
                amount=instance.amount
            ).delete()[0]
            
            if deleted_count > 0:
                logger.info(f"Deleted {deleted_count} GoalAllocation record(s) for {goal.name}")
            else:
                logger.warning(f"No GoalAllocation found to delete for {goal.name}")
        else:
            logger.warning(f"No MonthlyAllocation found for month {contribution_month}")
            
    except ImportError:
        # Budgets app not installed, just update goal
        logger.warning("Budgets app not available")
    except Exception as e:
        # Log error but don't prevent deletion
        logger.error(f"Error in sync_contribution_deletion: {e}")


def sync_expense_deletion(sender, instance, **kwargs):
    """
    When a budget expense is deleted:
    1. Check if it's a goal allocation expense (description starts with "Allocation to ")
    2. Find corresponding goal contribution and delete it
    3. Find corresponding goal allocation record and delete it (so goal can be re-allocated)
    4. Update goal balance
    """
    # Check if this is a goal allocation expense by description pattern
    if not instance.description or not instance.description.startswith('Allocation to '):
        return
    
    try:
        # Parse goal name from description
        # Description format: "Allocation to [Goal Name]"
        goal_name = instance.description.replace('Allocation to ', '')
        logger.info(f"Processing expense deletion for goal: {goal_name}")
        
        from .models import SavingsGoal
        
        # Find matching goal
        goal = SavingsGoal.objects.filter(
            user=instance.user,
            name=goal_name
        ).first()
        
        if goal:
            # Find matching contribution
            contribution = GoalContribution.objects.filter(
                goal=goal,
                amount=instance.amount,
                date=instance.date
            ).first()
            
            if contribution:
                # Temporarily disconnect our signal to avoid infinite loop
                pre_delete.disconnect(sync_contribution_deletion, sender=GoalContribution)
                
                # Update goal balance
                goal.current_amount = max(goal.current_amount - contribution.amount, Decimal('0'))
                goal.save()
                logger.info(f"Updated {goal.name} balance: -{contribution.amount}")
                
                # Delete contribution
                contribution.delete()
                logger.info(f"Deleted corresponding contribution: ${contribution.amount}")
                
                # Reconnect signals
                pre_delete.connect(sync_contribution_deletion, sender=GoalContribution)
            else:
                logger.warning(f"No matching contribution found for {goal_name}")
            
            # Also delete the GoalAllocation record so the goal can be re-allocated
            expense_month = instance.date.replace(day=1)
            monthly_allocation = MonthlyAllocation.objects.filter(
                user=instance.user,
                month=expense_month
            ).first()
            
            if monthly_allocation:
                # Delete the goal allocation record
                deleted_count = GoalAllocation.objects.filter(
                    monthly_allocation=monthly_allocation,
                    goal=goal,
                    amount=instance.amount
                ).delete()[0]
                
                if deleted_count > 0:
                    logger.info(f"Deleted {deleted_count} GoalAllocation record(s) for {goal_name}")
                else:
                    logger.warning(f"No GoalAllocation found to delete for {goal_name}")
            else:
                logger.warning(f"No MonthlyAllocation found for month {expense_month}")
        else:
            logger.warning(f"No goal found with name: {goal_name}")
                
    except Exception as e:
        # Log error but don't prevent deletion
        logger.error(f"Error in sync_expense_deletion: {e}", exc_info=True)


# Register the expense deletion signal when budgets app is available
try:
    from budgets.models import Expense
    post_delete.connect(sync_expense_deletion, sender=Expense)
    logger.info("Expense deletion signal registered")
except ImportError:
    logger.warning("Budgets app not installed - expense sync disabled")
