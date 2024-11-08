# Generated by Django 5.0.1 on 2024-09-09 10:41

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
                ('user_id', models.CharField(max_length=100, unique=True)),
                ('user_first_name', models.CharField(max_length=100)),
                ('user_last_name', models.CharField(max_length=100)),
                ('user_phone_number', models.CharField(max_length=10)),
                ('user_dob', models.DateField()),
                ('user_address_line_1', models.CharField(max_length=255)),
                ('user_address_line_2', models.CharField(blank=True, max_length=255, null=True)),
                ('user_state', models.CharField(max_length=100)),
                ('user_city', models.CharField(max_length=100)),
                ('user_pin_code', models.CharField(max_length=20)),
                ('user_country', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='KYCDetail',
            fields=[
                ('user_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('kyc_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
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
                'db_table': 'kyc_data',
                'managed': False,
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
