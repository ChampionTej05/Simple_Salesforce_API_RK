from rest_framework import serializers
from .models import Employees, SalesforceModel
from . import models

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        #fields=('firstname','lastname') #what to getas the represent
        fields='__all__'        #returns all fields


class SalesforceModelSerializer(serializers.ModelSerializer):
    Description=serializers.CharField(source='Description__c')
    ReleaseDate=serializers.CharField(source='ReleaseDate__c')
    MD5=serializers.CharField(source='MD5__c')
    Version=serializers.CharField(source='Version__c')
    URL=serializers.CharField(source='URL__c')

    class Meta:
        model=SalesforceModel
        fields=['Name','MD5','Description','ReleaseDate','Version','URL']  #Specify which fields to serialize here



{'Name':'Rakshit456','Description__c':'Test row three','Version__c':'2019203451',
'MD5__c':'abdbbdbdbdbdbd23u8u8u21','URL__c':'https://avi-portal-s3.s3.amazonaws.com/CrsDownloads/CRS-2019-2-BETA.json?AWSAccessKeyId=AKIAJ2J6EFWYAUAZGNUA&Expires=1597494637&Signature=HRpaJISKlev39go8dVx2d%2FzFy0w%3D',
'ReleaseDate__c':'2020-11-01'}
