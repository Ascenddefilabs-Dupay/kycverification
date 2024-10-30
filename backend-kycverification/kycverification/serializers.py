from rest_framework import serializers
# from .models import AadhaarAuthentication,PANAuth
from .models import KYCDetail, CustomUser



class KYCDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = KYCDetail
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

