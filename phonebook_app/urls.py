from django.urls import path
from .import views

urlpatterns = [
  path('/contactView', views.PhonebookView.as_view()),
  path('/contactAdd', views.PhonebookAdd.as_view()),
  path('/search/', views.SearchAPIView.as_view()),
  path('/contactEdit/<int:pk>/', views.updateContact.as_view()),
  path('/deleteContact/<int:pk>/', views.deleteContact.as_view())
]

