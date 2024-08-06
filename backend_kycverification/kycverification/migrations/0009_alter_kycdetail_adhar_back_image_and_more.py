# Generated by Django 5.0.1 on 2024-08-05 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kycverification', '0008_alter_kycdetail_adhar_back_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kycdetail',
            name='adhar_back_image',
            field=models.FileField(blank=True, null=True, upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='kycdetail',
            name='adhar_front_image',
            field=models.FileField(blank=True, null=True, upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='kycdetail',
            name='pan_back_image',
            field=models.FileField(blank=True, null=True, upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='kycdetail',
            name='pan_front_image',
            field=models.FileField(blank=True, null=True, upload_to='photos'),
        ),
    ]