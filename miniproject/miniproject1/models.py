from django.db import models
from django.contrib.auth.models import User

class Register(models.Model):
  
    Student_name = models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    Confirm_Password=models.CharField(max_length=100)
    def __str__(self):
            return self.Student_name


class LogIn(models.Model):
    Email=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)

    def __str__(self):
            return self.Email


class Feedback(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()

    message =models.TextField()
    date = models.DateField(auto_now_add=True)
 
    def __str__(self):
        return self.name



