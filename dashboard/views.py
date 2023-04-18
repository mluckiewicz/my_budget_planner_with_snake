from __future__ import annotations
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from transactions.models import Transaction
from django.http import JsonResponse
from transactions.models import Transaction


@method_decorator(login_required, name="dispatch")
class DashboardView(View):
    template_name = "dashboard/view.html"

    def get(self, request):
        data = Transaction.objects.all()
        
        return render(request, self.template_name)
    

def data(request):
    transactions = Transaction.objects.all()
    data = []
    for transaction in transactions:
        data.append({
            'title': transaction.category.category_name,
            'start': transaction.execution_date.isoformat(),
            'amount': {
                'amount': str(transaction.amount.amount),
                'currency': str(transaction.amount.currency)
            },
        })
    return JsonResponse(data, safe=False)
    
    
