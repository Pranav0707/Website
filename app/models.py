from django.db import models


# Create your models here.
class Student(models.Model):
    firstname = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.CharField(max_length=150)

    def __str__(self):
        return self.email
