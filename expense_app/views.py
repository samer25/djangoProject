from django.shortcuts import render, redirect

# Create your views here.
from expense_app.forms import UserForm, ExpenseForm
from expense_app.models import User, Expense


def home_page(req):
    user = User.objects.count()
    expense = Expense.objects.all()
    form = UserForm()

    context = {
        'user': user,
        'expense': expense,
        'form': form,
    }
    if not user:
        if req.method == 'GET':
            return render(req, 'home-no-profile.html', context)

        else:
            form = UserForm(req.POST)
            if form.is_valid():
                form.save()
                return redirect('home page')
    return render(req, 'home-with-profile.html', context)


def create(req):
    if req.method == 'GET':
        form = ExpenseForm()
        return render(req, 'expense-create.html', {'form': form})
    else:
        form = ExpenseForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')


def edit(req):
    expense = Expense.objects.get()
    if req.method == 'GET':
        form = ExpenseForm(instance=expense)
        return render(req, 'expense-edit.html', {'form': form})
    else:
        form = ExpenseForm(req.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home page')


def delete(req, pk):
    expense = Expense.objects.get(pk=pk)
    if req.method == 'GET':
        form = ExpenseForm(instance=expense)
        return render(req, 'expense-delete.html', {'form': form})
    else:

        expense.delete()
        return redirect('home page')


def profile(req):
    user = User.objects.get()
    return render(req, 'profile.html', {'user': user})


def profile_edit(req, pk):
    user = User.objects.get(pk=pk)
    if req.method == 'GET':
        form = UserForm(instance=user)
        return render(req, 'profile-edit.html', {'form': form})
    else:
        form = UserForm(req.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')


def profile_delete(req):
    if req.method == 'GET':
        return render(req, 'profile-delete.html')
    else:
        user = User.objects.get()
        expense = Expense.objects.get()
        expense.delete()
        user.delete()

        return redirect('home page')
