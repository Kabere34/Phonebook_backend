from django.urls import path
from .import views

urlpatterns = [
    path('phonebook', views.Phonebook.as_view),
]
