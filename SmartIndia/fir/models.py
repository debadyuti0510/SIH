from django.db import models
from django.urls import reverse
# Create your models here.
class firstruc(models.Model):
    name = models.CharField(max_length=250)
    dob = models.CharField(max_length=250)
    pnr = models.CharField(max_length=250)
    gender = models.CharField(max_length=250)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.CharField(max_length=10000)
    complaint = models.CharField(max_length=10000)
    description = models.CharField(max_length=10000)
    location = models.CharField(max_length = 70)

def get_absolute_url(self):
    return reverse('/homepage/', kwargs={'pk': self.pk})
