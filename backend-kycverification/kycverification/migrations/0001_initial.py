# Generated by Django 5.0.1 on 2024-08-21 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, max_length=100, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=10)),
                ('dob', models.DateField()),
                ('address_line1', models.CharField(max_length=255)),
                ('address_line2', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'users_details',
            },
        ),
        migrations.CreateModel(
            name='KYCDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100)),
                ('kyc_id', models.CharField(max_length=100, unique=True)),
                ('country_name', models.CharField(blank=True, max_length=100, null=True)),
                ('document_type', models.CharField(blank=True, max_length=100, null=True)),
                ('document_number1', models.CharField(blank=True, max_length=12, null=True)),
                ('document_front_image1', models.FileField(blank=True, null=True, upload_to='Dupay_Files')),
                ('document_back_image1', models.FileField(blank=True, null=True, upload_to='Dupay_Files')),
                ('document_number2', models.CharField(blank=True, max_length=10, null=True)),
                ('document_front_image2', models.FileField(blank=True, null=True, upload_to='Dupay_Files')),
                ('document_back_image2', models.FileField(blank=True, null=True, upload_to='Dupay_Files')),
                ('investment', models.BooleanField(blank=True, default=False, null=True)),
                ('nfts', models.BooleanField(blank=True, default=False, null=True)),
                ('web3', models.BooleanField(blank=True, default=False, null=True)),
            ],
            options={
                'db_table': 'kyc',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]
