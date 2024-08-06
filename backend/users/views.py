from django.shortcuts import render
from rest_framework import viewsets ,generics
from rest_framework.response import Response
from .models import KYCDetail, CustomUser
from .serializers import KYCDetailSerializer, CustomUserSerializer
from rest_framework import status
from rest_framework.decorators import action
import re


# from rest_framework import status
from .models import Project  
from .serializers import ProjectSerializer 
from datetime import date   

# Create your views here.

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class KYCDetailViewSet(viewsets.ModelViewSet):
    queryset = KYCDetail.objects.all()
    serializer_class = KYCDetailSerializer

    #print(queryset)
    user_id_list = []
    # kyc_list = list(queryset)
    # print(kyc_list)

    # for i in queryset:
    #     user_id_list.append(i)

    # print(user_id_list[-1].user_id)

    # id_list = []
    # for i in user_id_list:
    #     print(i)

    #index= user_id_list[-1].index(user_id_list[-1][0])

    #print(index, user_id_list[index])
   
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
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Generate KYC details only with user_id and kyc_id
        kyc_data = {
            'user_id': user.user_id,
            'kyc_id': self.generate_kyc_id(user.user_id),
            'country': None,
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
        kyc_view_set = KYCDetailViewSet()
        kyc_view_set.get_user_id(user.user_id)
        
        kyc_serializer = KYCDetailSerializer(data=kyc_data)
        kyc_serializer.is_valid(raise_exception=True)
        kyc_serializer.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def generate_kyc_id(self, user_id):
        latest_kyc = KYCDetail.objects.order_by('-kyc_id').first()
        if latest_kyc and re.search(r'\d+', latest_kyc.kyc_id):
            last_id = latest_kyc.kyc_id
            number = int(re.search(r'\d+', last_id).group())
            new_number = number + 1
            return f'kycC{new_number:04d}'
        return f'kycC0001'
    
