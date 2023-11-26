# Generated by Django 4.2.7 on 2023-11-24 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_medicine_expire_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medication',
            name='dosage',
        ),
        migrations.RemoveField(
            model_name='medication',
            name='name',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='dosage',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='medicines',
        ),
        migrations.AddField(
            model_name='medication',
            name='prescribed_medicine',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.prescribedmedicine'),
        ),
    ]
