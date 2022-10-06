from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from phonebook_app import serializer
from phonebook_app.serializer import PhonebookSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Phonebook
from django.db.models import Q
from rest_framework import generics
from rest_framework import filters
from rest_framework.decorators import api_view


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

class SearchAPIView(generics.ListCreateAPIView):
    search_fields = ['firstName', 'lastName', 'phoneNumber','email']
    filter_backends = (filters.SearchFilter,)
    queryset = Phonebook.objects.all()
    serializer_class = PhonebookSerializer


class updateContact(APIView):
  def post(self, request, pk):

    contact = Phonebook.objects.get(id=pk)
    # print(contact.phoneNumber)

    print(contact.firstName,'contact')
    serializer = PhonebookSerializer(instance=contact,data=request.data)
    # print(request)
    if contact:
      firstName=request.data["firstName"]
      lastName=request.data["lastName"]
      phoneNumber=request.data['phoneNumber']
      email=request.data["email"]
      updated_contact=Phonebook.objects.filter(id=pk).update(firstName=firstName,lastName=lastName,phoneNumber=phoneNumber, email=email)
    return Response()


class deleteContact(APIView):
  def deleteContact(request, pk):
    product = Phonebook.objects.get(id=pk)
    product.delete()

    return Response('Items delete successfully!')





