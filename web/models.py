from django.db import models

# Create your models here.

class users(models.Model):

    uname = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    psw = models.CharField(max_length = 100)
    