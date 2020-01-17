from django.contrib import admin
from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns

from webapp import views
urlpatterns = [
    path('Employees/<int:pk>/',views.EmployeesListDetail.as_view()),
    path('Employees/',views.EmployeesList.as_view()),
    
    #path('',include('webapp.urls')),
]
