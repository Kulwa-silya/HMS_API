from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Patient, NextOfKin
from .serializers import PatientSerializer

# Create your views here.
class PatientList(APIView):
    def get(self, request):
        queryset = Patient.objects.select_related('next_of_kin').all()
        serializer = PatientSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
