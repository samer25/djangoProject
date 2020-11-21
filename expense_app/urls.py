from django.urls import path

import expense_app.views as ex_view

urlpatterns = [
    path('', ex_view.home_page, name='home page'),
    path('create/', ex_view.create, name='create'),
    path('edit/', ex_view.edit, name='edit'),
    path('delete/<int:pk>', ex_view.delete, name='delete'),
    path('profile/', ex_view.profile, name='profile'),
    path('profile-edit/<int:pk>', ex_view.profile_edit, name='profile edit'),
    path('profile-delete/', ex_view.profile_delete, name='profile delete'),
]
