from django.shortcuts import render
from rest_framework.views import APIView
from phonebook_app.serializer import PhonebookSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Phonebook

# Create your views here.
class PhonebookView(APIView):
  def get(self,request,format=None):
    all_contacts=Phonebook.objects.all()
    serializer=PhonebookSerializer(all_contacts,many=True)
    return Response(serializer.data)

class PhonebookAdd(APIView):
  def post(self,request,format=None):
    serializer=PhonebookSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status.HTTP_201_CREATED)
    return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

