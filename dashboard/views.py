from __future__ import annotations
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from transactions.models import Transaction
from django.http import JsonResponse


@method_decorator(login_required, name="dispatch")
class DashboardView(View):
    template_name = "dashboard/view.html"

    def get(self, request):
        return render(request, self.template_name)
    

def calendar_data(request):
    transactions = Transaction.objects.filter(user=request.user)
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
    
    
def get_pending_list(request):
    """Returns a JSON response containing a list of pending transactions.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response containing a list of pending transactions, sorted by execution date. Each transaction is represented as a dictionary with the following keys:
            - title (str): The name of the transaction category.
            - start (str): The execution date of the transaction, in ISO format.
            - description (str): A description of the transaction.
            - amount (dict): A dictionary containing the amount and currency of the transaction, represented as strings.
            - type (str): The name of the transaction type (e.g. "Income" or "Expense").
            - color (str): The color code for the transaction type, "#198754" for income transactions and "#dc3545" for expense transactions.
            - budget (str): The name of the budget associated with the transaction.
            - created (str): The creation date of the transaction, in ISO format.
            - updated (str): The last update date of the transaction, in ISO format.
            - is_executed (bool): True if the transaction has been executed, False otherwise.
            - execution_date (str): The execution date of the transaction, in ISO format.

    Raises:
        None
    """
    pending_transacion = Transaction.objects.filter(is_executed=False).order_by('execution_date')
    data = []
    for transaction in pending_transacion:
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
            "execution_date": transaction.execution_date.isoformat()
            
        })
    return JsonResponse(data, safe=False)