from .models import Phonebook
from rest_framework import serializers


class PhonebookSerializer(serializers.ModelSerializer):
  class Meta:
    model=Phonebook
    fields='__all__'


