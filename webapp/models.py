from django.db import models

# Create your models here.
class Employees(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    emp_id=models.IntegerField()

    def __str__(self):
        return self.firstname


class SalesforceModel(models.Model):
    Description=models.CharField(max_length=100)
    MD5=models.CharField(max_length=100)
    Name=models.CharField(max_length=100)
    ReleaseDate=models.CharField(max_length=100)
    Version=models.CharField(max_length=100)
    URL=models.TextField(max_length=100)

    def __str__(self):
        return "Object : "+self.Description

    
