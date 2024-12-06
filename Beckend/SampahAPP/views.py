from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from .models import *
from .serializer import *

# @api_view(['GET'])
# def get_ContactUs(request):
#     Contact_Uss = Contact_Us.objects.all()
#     SerializerData = Contact_UsSerializer(Contact_Uss, many=True).data
#     return Response(SerializerData)

# @api_view(['POST'])
# def create_ContactUs(request):
#     contact_us = request.data
#     serializer = Contact_UsSerializer(data = contact_us)
#     if serializer.valid():
#         serializer.save
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_201_BAD_REQUEST)

from rest_framework import viewsets
from .models import TitikPoin, Sampah, User, Setor, Tarik, Tabungan, Contact_Us, Admin
from .serializer import TitikPoinSerializer, SampahSerializer, TarikSerializer, SetorSerializer, TabunganSerializer, UserSerializer, Contact_UsSerializer, AdminSerializer

class TitikPoinViewSet (viewsets.ModelViewSet):
    queryset = TitikPoin.objects.all()
    serializer_class = TitikPoinSerializer

class SampahViewSet (viewsets.ModelViewSet):
    queryset = Sampah.objects.all()
    serializer_class = SampahSerializer

class UserViewSet (viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SetorViewSet (viewsets.ModelViewSet):
    queryset = Setor.objects.all()
    serializer_class = SetorSerializer

class TarikViewSet (viewsets.ModelViewSet):
    queryset = Tarik.objects.all()
    serializer_class = TarikSerializer

class TabunganViewSet (viewsets.ModelViewSet):
    queryset = Tabungan.objects.all()
    serializer_class = TabunganSerializer

class Contact_UsViewSet (viewsets.ModelViewSet):
    queryset = Contact_Us.objects.all()
    serializer_class = Contact_UsSerializer

class AdminViewSet (viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
