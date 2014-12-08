from django.db import models
from django.forms import ModelForm

# Create your models here.
class guests(models.Model):
    GuestID = models.AutoField(primary_key=True)
    LastName = models.CharField(max_length=50, editable=True, serialize=True)
    FirstName = models.CharField(max_length=50, editable=True, serialize=True)
    IPAddress = models.IPAddressField(max_length=50, editable=False, serialize=True)
    EntryDate = models.TimeField(auto_now=True, serialize=True)
    OS = models.CharField(max_length=50, editable=False, serialize=True)
    Device = models.CharField(max_length=50, editable=False, serialize=True)

