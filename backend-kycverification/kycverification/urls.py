from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KYCDetailViewSet, UsersViewSet


router = DefaultRouter()

router.register(r'kyc-details', KYCDetailViewSet)
router.register(r'personal-details', UsersViewSet)


urlpatterns = [
    path('',include(router.urls)),
]
