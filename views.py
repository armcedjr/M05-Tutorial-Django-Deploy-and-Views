from django.shortcuts import render
from .forms import PayrollForm

def payroll_calculator(request):
    if request.method == 'POST':
        form = PayrollForm(request.POST)
        if form.is_valid():
            payroll = form.save(commit=False)
            payroll.total_pay = payroll.rate_of_pay * payroll.hours_worked
            return render(request, 'payroll/result.html', {'payroll': payroll})
    else:
        form = PayrollForm()
    return render(request, 'payroll/calculator.html', {'form': form})
