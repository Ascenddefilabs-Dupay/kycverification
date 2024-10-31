from django.db import models
import re

from cloudinary.models import CloudinaryField


from django.db import models
import re


class KYCDetail(models.Model):
    user_id = models.CharField(max_length=8, primary_key=True)
    kyc_id = models.CharField(max_length=100, unique=True,blank=True, null=True)
    country_name = models.CharField(max_length=100, blank=True, null=True)
    document_type = models.CharField(max_length=100, blank=True, null=True)
    document_number1 = models.CharField(max_length=12, blank=True, null=True)
    document_front_image1 = models.FileField(upload_to='Dupay_Files',blank=True, null=True)
    document_back_image1 = models.FileField(upload_to='Dupay_Files',blank=True, null=True)
    document_number2 = models.CharField(max_length=10, blank=True, null=True)
    document_front_image2 = models.FileField(upload_to='Dupay_Files',blank=True, null=True)
    document_back_image2 = models.FileField(upload_to='Dupay_Files',blank=True, null=True)
    investment = models.BooleanField(default=False, blank=True, null=True)
    nfts = models.BooleanField(default=False, blank=True, null=True)
    web3 = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        db_table = 'kyc_data'
        managed=False

    def __str__(self):
    
        def __str__(self):
            return str([self.user_id, self.kyc_id, self.country_name, self.document_type, self.document_number1, self.document_front_image1, self.document_back_image1, self.document_number2, self.document_front_image2, self.document_back_image2, self.investment, self.nfts, self.web3])






class CustomUser(models.Model):
    user_id = models.CharField(max_length=100, unique=True, blank=False, primary_key=True)
    user_first_name = models.CharField(max_length=100)
    user_last_name = models.CharField(max_length=100)
    user_phone_number = models.CharField(max_length=15)
    user_dob = models.DateField()
    user_address_line_1 = models.CharField(max_length=255)  # Ensure this matches your DB column
    user_address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    user_state = models.CharField(max_length=100)
    user_city = models.CharField(max_length=100)
    user_pin_code = models.CharField(max_length=20)
    user_country = models.CharField(max_length=100)

    class Meta:
        db_table = 'users'
        managed=False

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        # Removed auto-generation of user_id
        super().save(*args, **kwargs)