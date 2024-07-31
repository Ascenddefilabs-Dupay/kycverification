from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class KYCDetail(models.Model):
    country = models.CharField(max_length=100,blank=True, null=True)
    document_type = models.CharField(max_length=100 ,blank=True, null=True)
    adhar_number = models.CharField(max_length=12, blank=True, null=True)
    adhar_image = models.ImageField(upload_to='adhar_images/', blank=True, null=True)
    pan_number = models.CharField(max_length=10, blank=True, null=True)
    pan_image = models.ImageField(upload_to='pan_images/', blank=True, null=True)

    def __str__(self):
        return self.adhar_number