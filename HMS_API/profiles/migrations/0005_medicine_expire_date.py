# Generated by Django 4.2.7 on 2023-11-24 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_remove_prescription_medicine_medicine_manufacturer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='expire_date',
            field=models.DateField(default='2023-01-01'),
        ),
    ]