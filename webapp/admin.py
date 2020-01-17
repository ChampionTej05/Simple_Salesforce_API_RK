from django.contrib import admin
from .models import Employees,SalesforceModel
# Register your models here.

admin.site.register(Employees)
admin.site.register(SalesforceModel)
