from django.shortcuts import render
from rest_framework import viewsets ,generics
from rest_framework.response import Response
from .models import KYCDetail, CustomUser
from .serializers import KYCDetailSerializer, CustomUserSerializer
from rest_framework import status
from rest_framework.decorators import action
import re


# from rest_framework import status

from datetime import date   

# Create your views here.
class KYCDetailViewSet(viewsets.ModelViewSet):
    queryset = KYCDetail.objects.all()
    serializer_class = KYCDetailSerializer

    #print(queryset)
    user_id_list = []
   
    def create(self, request, *args, **kwargs):
        queryset = KYCDetail.objects.all()
        serializer_class = KYCDetailSerializer
        user_id_list = []
        for i in queryset:
            user_id_list.append(i)
        print(len(user_id_list))
        user_id = user_id_list[-1].user_id
        kyc_detail, created = KYCDetail.objects.update_or_create(
            user_id=user_id,
            defaults=request.data
        )
        if created:
            return Response(KYCDetailSerializer(kyc_detail).data, status=status.HTTP_201_CREATED)
        return Response(KYCDetailSerializer(kyc_detail).data, status=status.HTTP_200_OK)


    


    def get_user_id(self, user_id):
        print(user_id)
    
class UsersViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        # Check if a user with the given user_id already exists
        user_instance = CustomUser.objects.filter(user_id=request.data.get('user_id')).first()

        if user_instance:
            # If user exists, update the user details
            serializer = self.get_serializer(user_instance, data=request.data, partial=True)
        else:
            # If user does not exist, create a new user
            serializer = self.get_serializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Check if KYC details already exist for the given user_id
        kyc_instance = KYCDetail.objects.filter(user_id=user.user_id).first()
        
        kyc_data = {
            'user_id': user.user_id,
            'kyc_id': self.generate_kyc_id(user.user_id) if not kyc_instance else kyc_instance.kyc_id,
            'country': request.data.get('country'),
            'document_type': None,
            'adhar_number': None,
            'adhar_front_image': None,
            'adhar_back_image': None,
            'pan_number': None,
            'pan_front_image': None,
            'pan_back_image': None,
            'investment': None,
            'nfts': None,
            'web3': None,
        }

        if kyc_instance:
            kyc_serializer = KYCDetailSerializer(kyc_instance, data=kyc_data, partial=True)
        else:
            kyc_serializer = KYCDetailSerializer(data=kyc_data)
        
        kyc_serializer.is_valid(raise_exception=True)
        kyc_serializer.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK if user_instance else status.HTTP_201_CREATED, headers=headers)

    def generate_kyc_id(self, user_id):
        latest_kyc = KYCDetail.objects.order_by('-kyc_id').first()
        if latest_kyc and re.search(r'\d+', latest_kyc.kyc_id):
            last_id = latest_kyc.kyc_id
            number = int(re.search(r'\d+', last_id).group())
            new_number = number + 1
            return f'kycC{new_number:04d}'
        return f'kycC0001'