from django.shortcuts import render
from rest_framework import viewsets ,generics
from rest_framework.response import Response
from .models import KYCDetail
from .serializers import KYCDetailSerializer


# from rest_framework import status
from .models import Project  
from .serializers import ProjectSerializer    

# Create your views here.

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class KYCDetailViewSet(viewsets.ModelViewSet):
    queryset = KYCDetail.objects.all()
    serializer_class = KYCDetailSerializer


