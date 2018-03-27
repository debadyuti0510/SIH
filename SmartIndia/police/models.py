from django.db import models

# Create your models here.
class policeuser(models.Model):
    user = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
