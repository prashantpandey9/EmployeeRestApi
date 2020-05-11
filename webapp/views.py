from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import *
from . serializers import employeesSerializers

# Create your views here.

class employeeList(APIView):
    def get(self,request):
        employees1=employees.objects.all()
        serializer=employeesSerializers(employees1,many=True)
        return Response(serializer.data)

    def post(self):
        pass
