from __future__ import annotations
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.generic import View
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import AddSingleTransactionForm, AddRepeatableTransactionForm
from .models import Transaction, RepeatableTransaction


@method_decorator(login_required, name="dispatch")
class AddSingleTransactionView(View):
    template_name = "transaction/add_transaction_single.html"
    form_class = AddSingleTransactionForm

    def get(self, request):
        return render(request, self.template_name, self.get_context(request))

    def post(self, request):
        # Check if the form is valid
        form = self.form_class(request.POST)
        if form.is_valid():
            # Add new transaction
            transaction = Transaction.objects.create(
                user=self.request.user,
                type=form.cleaned_data["type"],
                amount=form.cleaned_data["amount"],
                category=form.cleaned_data["category"],
                budget=form.cleaned_data["budget"],
                execution_date=form.cleaned_data["execution_date"],
                is_executed=form.cleaned_data["is_executed"],
                description=form.cleaned_data["description"],
            )
            transaction.save()

            # Redirect back to main form
            back_url = request.POST.get("back_url", None)
            if back_url is not None and back_url != "None":
                return redirect(back_url)
            return redirect(request.path)

        return render(request, self.template_name, self.get_context(request))

    def get_context(self, request, form=None):
        # Helper method to generate a dictionary with data to pass to the template
        context = {}
        if form:
            context["form"] = form
        else:
            context["form"] = self.form_class()
        context["back_url"] = request.GET.get("back_url", None)
        return context


@method_decorator(login_required, name="dispatch")
class AddRepeatableTransactionView(View):
    template_name = "transaction/add_transaction_repeatable.html"
    form_class = AddRepeatableTransactionForm

    def get(self, request):
        return render(request, self.template_name, self.get_context(request))

    def post(self, request):
        # Check if the form is valid
        form = self.form_class(request.POST)
        if form.is_valid():
            # Add new transaction
            transaction = RepeatableTransaction.objects.create(
                user=self.request.user,
                type=form.cleaned_data["type"],
                base_amout=form.cleaned_data["base_amout"],
                start_date=form.cleaned_data["start_date"],
                end_date=form.cleaned_data["end_date"],
                recurrence_type=form.cleaned_data["recurrence_type"],
                recurrence_value=form.cleaned_data["recurrence_value"],
                category=form.cleaned_data["category"],
                budget=form.cleaned_data["budget"],
                description=form.cleaned_data["description"],
            )
            transaction.save()

            # Redirect back to main form
            back_url = request.POST.get("back_url", None)
            if back_url is not None and back_url != "None":
                return redirect(back_url)
            return redirect(request.path)

        return render(request, self.template_name, self.get_context(request))

    def get_context(self, request, form=None):
        # Helper method to generate a dictionary with data to pass to the template
        context = {}
        if form:
            context["form"] = form
        else:
            context["form"] = self.form_class()
        context["back_url"] = request.GET.get("back_url", None)
        return context


@method_decorator(login_required, name="dispatch")
class TransactionTableView(View):
    model = Transaction
    template_name = "transaction/table.html"
    context_object_name = "transactions"

    def get(self, request):
        context = {}
        transactions = self.model.objects.all()
        context["transactions"] = transactions
        return render(request, self.template_name, context)


@method_decorator(login_required, name="dispatch")
class TransactionUpdateView(UpdateView):
    model = Transaction
    form_class = AddSingleTransactionForm
    template_name = "transaction/edit_single.html"
    success_url = reverse_lazy("transactions:transactions")


def delete_transactions(request) -> JsonResponse[dict]:
    """
    Deletes the selected categories from the database. Uses AJAX equest form template
    """
    if request.method == "POST":
        ids = request.POST.getlist("ids[]")
        Transaction.objects.filter(id__in=ids).delete()
        return JsonResponse({"success": True})
    else:
        return JsonResponse({"success": False, "message": "Invalid request method"})
