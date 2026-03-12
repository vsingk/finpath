from django.db.models.signals import post_delete, pre_delete
from django.dispatch import receiver
from decimal import Decimal
import logging

from .models import GoalContribution, GoalAllocation, MonthlyAllocation

logger = logging.getLogger(__name__)


@receiver(pre_delete, sender=GoalContribution)
def sync_contribution_deletion(sender, instance, **kwargs):
    try:
        from budgets.models import Expense
        
        goal = instance.goal
        goal.current_amount = max(goal.current_amount - instance.amount, Decimal('0'))
        goal.save()
        logger.info(f"Updated {goal.name} balance: -{instance.amount}")
        
        expense = Expense.objects.filter(
            user=goal.user,
            amount=instance.amount,
            date=instance.date,
            description__icontains=goal.name,
        ).first()
        
        if expense:
            from budgets.models import Expense as ExpenseModel
            post_delete.disconnect(sync_expense_deletion, sender=ExpenseModel)
            
            expense.delete()
            logger.info(f"Deleted corresponding expense: ${expense.amount}")
            
            post_delete.connect(sync_expense_deletion, sender=ExpenseModel)
        
        contribution_month = instance.date.replace(day=1)
        monthly_allocation = MonthlyAllocation.objects.filter(
            user=goal.user,
            month=contribution_month
        ).first()
        
        if monthly_allocation:
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
        logger.warning("Budgets app not available")
    except Exception as e:
        logger.error(f"Error in sync_contribution_deletion: {e}")


def sync_expense_deletion(sender, instance, **kwargs):
    if not instance.description or not instance.description.startswith('Allocation to '):
        return
    
    try:
        goal_name = instance.description.replace('Allocation to ', '')
        logger.info(f"Processing expense deletion for goal: {goal_name}")
        
        from .models import SavingsGoal
        
        goal = SavingsGoal.objects.filter(
            user=instance.user,
            name=goal_name
        ).first()
        
        if goal:
            contribution = GoalContribution.objects.filter(
                goal=goal,
                amount=instance.amount,
                date=instance.date
            ).first()
            
            if contribution:
                pre_delete.disconnect(sync_contribution_deletion, sender=GoalContribution)
                
                goal.current_amount = max(goal.current_amount - contribution.amount, Decimal('0'))
                goal.save()
                logger.info(f"Updated {goal.name} balance: -{contribution.amount}")
                
                contribution.delete()
                logger.info(f"Deleted corresponding contribution: ${contribution.amount}")
                
                pre_delete.connect(sync_contribution_deletion, sender=GoalContribution)
            else:
                logger.warning(f"No matching contribution found for {goal_name}")
            
            expense_month = instance.date.replace(day=1)
            monthly_allocation = MonthlyAllocation.objects.filter(
                user=instance.user,
                month=expense_month
            ).first()
            
            if monthly_allocation:
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
        logger.error(f"Error in sync_expense_deletion: {e}", exc_info=True)


try:
    from budgets.models import Expense
    post_delete.connect(sync_expense_deletion, sender=Expense)
    logger.info("Expense deletion signal registered")
except ImportError:
    logger.warning("Budgets app not installed - expense sync disabled")
