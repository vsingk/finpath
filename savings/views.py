import json
from datetime import date
from decimal import Decimal

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from django.utils import timezone

from .models import SavingsEntry
from .forms import SavingsEntryForm


@login_required
def savings_progress(request):
    entries = SavingsEntry.objects.filter(user=request.user)
    today = timezone.now().date()

    if request.method == 'POST':
        form = SavingsEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            messages.success(request, f'Saved ${entry.amount} on {entry.date}!')
            return redirect('savings_progress')
    else:
        form = SavingsEntryForm()

    total_saved = entries.aggregate(total=Sum('amount'))['total'] or Decimal('0.00')
    month_start = today.replace(day=1)
    entries_this_month = entries.filter(date__gte=month_start).count()
    avg_monthly = _calculate_average_monthly(entries, today, total_saved)

    recent_entries = entries[:20]
    historical_labels, historical_data = _build_historical_series(entries)
    projection_data = _build_projection_series(avg_monthly, total_saved, today)

    context = {
        'form': form,
        'total_saved': total_saved,
        'entries_this_month': entries_this_month,
        'avg_monthly': avg_monthly,
        'recent_entries': recent_entries,
        'historical_labels_json': json.dumps(historical_labels),
        'historical_data_json': json.dumps(historical_data),
        'projection_json': json.dumps(projection_data),
    }
    return render(request, 'savings/progress.html', context)


@login_required
def delete_entry(request, pk):
    entry = get_object_or_404(SavingsEntry, pk=pk, user=request.user)
    if request.method == 'POST':
        entry.delete()
        messages.success(request, 'Entry deleted.')
    return redirect('savings_progress')


@login_required
def edit_entry(request, pk):
    entry = get_object_or_404(SavingsEntry, pk=pk, user=request.user)
    if request.method == 'POST':
        form = SavingsEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request, 'Entry updated.')
            return redirect('savings_progress')
    else:
        form = SavingsEntryForm(instance=entry)
    return render(request, 'savings/edit_entry.html', {'form': form, 'entry': entry})

 
def _calculate_average_monthly(entries, today, total=None):
    if not entries.exists():
        return Decimal('0.00')

    first_entry = entries.order_by('date').first()
    if total is None:
        total = entries.aggregate(total=Sum('amount'))['total'] or Decimal('0.00')

    months_elapsed = (
        (today.year - first_entry.date.year) * 12
        + (today.month - first_entry.date.month)
    )
    months_elapsed = max(months_elapsed, 1)

    return (total / Decimal(str(months_elapsed))).quantize(Decimal('0.01'))


def _build_historical_series(entries):
    ordered = entries.order_by('date', 'created_at')
    labels = []
    data = []
    running_total = Decimal('0.00')

    for entry in ordered:
        running_total += entry.amount
        date_str = entry.date.isoformat()
        if labels and labels[-1] == date_str:
            data[-1] = float(running_total)
        else:
            labels.append(date_str)
            data.append(float(running_total))

    return labels, data


def _build_projection_series(avg_monthly, current_total, today):
    max_months = 60
    labels = []
    values = []
    running = float(current_total)
    monthly = float(avg_monthly)

    for i in range(1, max_months + 1):
        future_month = today.month + i
        future_year = today.year + (future_month - 1) // 12
        future_month = ((future_month - 1) % 12) + 1
        month_label = date(future_year, future_month, 1).strftime('%b %Y')

        running += monthly
        labels.append(month_label)
        values.append(round(running, 2))

    return {
        'labels': labels,
        '1yr': values[:12],
        '3yr': values[:36],
        '5yr': values[:60],
    }
