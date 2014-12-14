from django.db import models
from django.forms import ModelForm

# Create your models here.
class guests(models.Model):
    guest_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=50, editable=True, serialize=True)
    first_name = models.CharField(max_length=50, editable=True, serialize=True, null=True)
    ip_address = models.IPAddressField(max_length=50, editable=False, serialize=True, null=True)
    entry_date = models.TimeField(auto_now=True, serialize=True, null=True)
    o_s = models.CharField(max_length=50, editable=False, serialize=True, null=True)
    device = models.CharField(max_length=50, editable=False, serialize=True, null=True)

def __unicode__(self):
        return self.last_name

def __str__(self):

        return ' '.join([
            self.last_name,
            self.first_name,
            self.ip_address,
            self.o_s,
            self.device
        ])