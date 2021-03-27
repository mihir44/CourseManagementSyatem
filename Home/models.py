from django.db import models


# Create your models here.
class Student(models.Model):
    username = models.CharField(max_length=300, unique=True)
    password = models.TextField(default='abc123')
    cpassword = models.TextField(default='abc123')
    email = models.TextField()
    firstname = models.TextField(default='asc')
    phone = models.TextField(default='123')

