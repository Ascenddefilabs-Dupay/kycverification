from rest_framework import serializers
from .models import Project
# from .models import AadhaarAuthentication,PANAuth
from .models import KYCDetail



class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class KYCDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = KYCDetail
        fields = fields = '__all__'
