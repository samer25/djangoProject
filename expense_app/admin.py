from django.contrib import admin

# Register your models here.
from expense_app.models import User, Expense

admin.site.register(User)
admin.site.register(Expense)
