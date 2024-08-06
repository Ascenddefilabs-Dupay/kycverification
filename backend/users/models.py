from django.db import models
import re

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class CustomUser(models.Model):
    user_id = models.CharField(max_length=100, unique=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=10)
    dob = models.DateField()
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    class Meta:
        db_table = 'users_details'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def save(self, *args, **kwargs):
        if not self.user_id:
            self.user_id = self.generate_user_id()
        super().save(*args, **kwargs)

    def generate_user_id(self):
        latest_user = CustomUser.objects.order_by('-user_id').first()
        if latest_user and re.search(r'\d+', latest_user.user_id):
            last_id = latest_user.user_id
            number = int(re.search(r'\d+', last_id).group())
            new_number = number + 1
            return f'dupC{new_number:04d}'
        return 'dupC0001'
    

class KYCDetail(models.Model):
    user_id = models.CharField(max_length=100)
    kyc_id = models.CharField(max_length=100, unique=True)
    country_name = models.CharField(max_length=100, blank=True, null=True)
    document_type = models.CharField(max_length=100, blank=True, null=True)
    document_number1 = models.CharField(max_length=12, blank=True, null=True)
    document_front_image1 = models.ImageField(upload_to='adhar_images/front/', blank=True, null=True)
    document_back_image1 = models.ImageField(upload_to='adhar_images/back/', blank=True, null=True)
    document_number2 = models.CharField(max_length=10, blank=True, null=True)
    document_front_image2 = models.ImageField(upload_to='pan_images/front/', blank=True, null=True)
    document_back_image2 = models.ImageField(upload_to='pan_images/back/', blank=True, null=True)
    investment = models.BooleanField(default=False, blank=True, null=True)
    nfts = models.BooleanField(default=False, blank=True, null=True)
    web3 = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        db_table = 'kyc'

    def __str__(self):
        return f'{[self.user_id, self.kyc_id, self.country_name, self.document_type,
                   self.document_number1, self.document_front_image1, self.document_back_image1,
                   self.document_number2, self.document_front_image2, self.document_back_image2, self.investment,
                   self.nfts, self.web3]}'
    


