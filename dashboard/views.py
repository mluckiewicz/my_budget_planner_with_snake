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
        return render(request, self.template_name)
    

def data(request):
    transactions =Transaction.objects.filter(user=request.user)
    data = []
    for transaction in transactions:
        data.append({
            'title': transaction.category.category_name,
            'start': transaction.execution_date.isoformat(),
            'description': transaction.description,
            'amount': {
                'amount': str(transaction.amount.amount),
                'currency': str(transaction.amount.currency)
            },
            'type': transaction.type.type_name,
            'color': '#198754' if transaction.type.type_name == "Income" else '#dc3545',
            'budget': transaction.budget.budget_name,
            'created': transaction.created.isoformat(),
            'updated': transaction.updated.isoformat(),
            'is_executed': transaction.is_executed,
            
        })
    return JsonResponse(data, safe=False)
    
    
