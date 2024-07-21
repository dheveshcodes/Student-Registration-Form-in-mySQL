from django.db import models

# Create your models here.

class STUDENTS(models.Model):
    Name = models.CharField(max_length=15)
    Email = models.EmailField(max_length=40)
    Phone = models.BigIntegerField(max_length=10)
