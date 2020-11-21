from django import forms

from expense_app.models import User, Expense


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'



