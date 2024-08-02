from django.db import models
import re

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class KYCDetail(models.Model):

    country = models.CharField(max_length=100, blank=True, null=True)
    document_type = models.CharField(max_length=100, blank=True, null=True)
    adhar_number = models.CharField(max_length=12, blank=True, null=True)
    adhar_front_image = models.ImageField(upload_to='adhar_images/front/', blank=True, null=True)
    adhar_back_image = models.ImageField(upload_to='adhar_images/back/', blank=True, null=True)
    pan_number = models.CharField(max_length=10, blank=True, null=True)
    pan_front_image = models.ImageField(upload_to='pan_images/front/', blank=True, null=True)
    pan_back_image = models.ImageField(upload_to='pan_images/back/', blank=True, null=True)
    investment = models.BooleanField(default=False, blank=True, null=True)
    nfts = models.BooleanField(default=False, blank=True, null=True)
    web3 = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        db_table = 'kyc'

    def __str__(self):
        return self.adhar_number or self.pan_number or 'KYC Detail'