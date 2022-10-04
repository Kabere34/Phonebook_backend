from django.urls import path
from .import views

urlpatterns = [
  path('/contactView', views.PhonebookView.as_view()),
  path('/contactAdd', views.PhonebookAdd.as_view()),
]
