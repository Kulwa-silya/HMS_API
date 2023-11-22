# Generated by Django 4.2.7 on 2023-11-22 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_remove_admission_bed_number_admission_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='number',
            field=models.CharField(default='00', max_length=2),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('APPOINTMENT', 'Appointment'), ('PATIENT', 'Patient')], default='PATIENT', max_length=12),
        ),
    ]
