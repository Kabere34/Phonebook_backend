from django.contrib import admin
from .models import Phonebook

# Register your models here.
# class PhonebookAdmin(admin.ModelAdmin):

admin.site.register(Phonebook)
