from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    foundation = models.CharField(max_length=50)


class student(models.Model):
    name = models.CharField(max_length=100)
    edad = models.IntegerField()
    github = models.CharField(max_length=100)
