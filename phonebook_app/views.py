from django.shortcuts import render
from rest_framework.views import APIView
from phonebook_app.serializer import PhonebookSerializer
from rest_framework.response import Response

# Create your views here.
class Phonebook(APIView):
  def get(self,request,format=None()):
    all_contacts=Phonebook.objects.all()
    serializer=PhonebookSerializer(all_contacts,many=True)
    return Response(serializer.data)
