from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView #so that normal views can return API views
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet,ViewSet
from pprint import pprint
# from rest_framework.decorators import list_route
from rest_framework import status
from .models import Employees, SalesforceModel
from .utils import setup_connection_salesForce
from rest_framework.permissions import AllowAny
from .serializers import EmployeesSerializer,SalesforceModelSerializer
# import Salesforce_setup as ss
import pandas as pd
from rest_framework.decorators import action
import io
# Create your views here.


class UserViewSet(ModelViewSet):
    """
    A simple ViewSet for EMPLOYEES .
    Method names should not be changed for default usage
    """
    # def list(self, request):
    #     queryset = Employees.objects.all()
    #     serializer = EmployeesSerializer(queryset, many=True)
    #     return Response(serializer.data)
    #
    # def retrieve(self, request, pk=None):
    #     queryset = Employees.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = EmployeesSerializer(user)
    #     return Response(serializer.data)
    #
    # def create(self,request):
    #     serializer=EmployeesSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    #
    # def update(self,request,pk=None):
    #     emp1=self.get_object(pk)
    #     serializer=EmployeesSerializer(emp1,data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    #whole code can be replaced by this two lines
    serializer_class = EmployeesSerializer
    queryset = Employees.objects.all()


    #this shows the name of employee only
    @action(detail=True)
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.firstname)

class EmployeesList(APIView):



    def get(self,request):
        emp1=Employees.objects.all()
        serializer=EmployeesSerializer(emp1,many=True)
        return Response(serializer.data)

        # sf=self.salesforce_Setup()
        # sf_data=ss.query_salesforce(sf)



    def post(self,request):
        serializer=EmployeesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class EmployeesListDetail(APIView):

    def get_object(self,pk):
        try:
            return Employees.objects.get(pk=pk)
        except Employees.DoesNotExist:
            raise Http404




    def get(self,request,pk):
        Emp1=self.get_object(pk)
        serializer=EmployeesSerializer(Emp1)
        return Response(serializer.data)



    def put(self,request,pk):
        emp1=self.get_object(pk)
        serializer=EmployeesSerializer(emp1,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class SalesforceViewSet(ModelViewSet):

    #following lines provide default behaviopur to classes
    queryset=SalesforceModel.objects.all()
    serializer_class=SalesforceModelSerializer

    # @list_route(methods=['post'],permission_classes=[AllowAny])

    def list(self,request):
            sf=setup_connection_salesForce()
            print("Call to get method")
            #GET method then
            sf_data = sf.query("SELECT name,MD5__c,Description__c,Version__c,ReleaseDate__c,URL__c FROM CRS__c")


            #converting the result into Dataframe
            sf_df = pd.DataFrame(sf_data['records']).drop(columns='attributes')
            print(sf_df)
            # pprint(sf_data['records'][0])
            # print(sf.CRS__c.describe())

            result=SalesforceModelSerializer(sf_data['records'],many=True)

            return Response (result.data)


    def create(self,request):
        sf=setup_connection_salesForce()
        print("Call to the POST method")
        data=request.data
        print("COME HERE SAFELY--------------------SSS")
        serializer=SalesforceModelSerializer(data=data)
        if serializer.is_valid():
            print("VALID DATA --------------------SSS")
            return_dict=serializer.validated_data
            query=sf.CRS__c.create(return_dict)
            return Response(query)
        else:
            return Response(serializer.errors)
