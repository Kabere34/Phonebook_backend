from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Phonebook(models.Model):
  firstName = models.CharField(max_length=30)
  lastName=models.CharField(max_length=30)
  phoneNumber = models.CharField(max_length=10,null=False, blank=False, unique=True)

  def __str__(self) -> str:
    return firstName + ' ' + lastName + ' ' + phoneNumber
