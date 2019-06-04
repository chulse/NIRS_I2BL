from django.db import models
from django.conf import settings

class MessageModel(models.Model):

    user = models.TextField() #just store their username

    date = models.CharField(max_length=125)
    pd1r1 = models.TextField()
    pd2r1 = models.TextField()
    pd3r1 = models.TextField()
    pd1ir1 = models.TextField()
    pd2ir1 = models.TextField()
    pd3ir1 = models.TextField()
    
    pd1r2 = models.TextField()
    pd2r2 = models.TextField()
    pd3r2 = models.TextField()
    pd1ir2 = models.TextField()
    pd2ir2 = models.TextField()
    pd3ir2 = models.TextField()
    
    pd1r3 = models.TextField()
    pd2r3 = models.TextField()
    pd3r3 = models.TextField()
    pd1ir3 = models.TextField()
    pd2ir3 = models.TextField()
    pd3ir3 = models.TextField()

    processedData1 = models.TextField()
    processedData2 = models.TextField()
    processedData3 = models.TextField()
    StO2 = models.TextField()


class UserModel(models.Model):
    username = models.CharField(max_length=125)
    password = models.TextField()
    email = models.TextField()


# Create your models here.
