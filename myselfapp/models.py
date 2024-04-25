from django.db import models

class message(models.Model):
    Your_Name=models.CharField(max_length=50)
    Your_Email=models.CharField(max_length=50)
    Subject=models.CharField(max_length=255)
    Message=models.CharField(max_length=255)
    
# Create your models here.
