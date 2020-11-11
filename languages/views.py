from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import LanguageSerializer,ProgrammerSerializer,ParadigmSerializer
from .models import Programmer,Paradigm,Language
# Create your views here.
class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

    #THIS IS PERMISSION REQUIRED DONE IN INDIVIDUAL VIEWS; ONLY LOGGED IN USERS CAN ADD THE DATA IN THE MODEL
    #INSTEAD OF DOING THIS IN EVERY VIEWS WE CAN DO FOR ALL AT ONCE IN SETTINGS.PY
    #WRITTEN IN LIST OF TUPLE FORM
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer

class ProgrammerView(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer