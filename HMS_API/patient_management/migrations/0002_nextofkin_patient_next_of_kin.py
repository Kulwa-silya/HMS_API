# Generated by Django 4.1.1 on 2022-09-19 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NextOfKin',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='patient_management.person')),
            ],
            bases=('patient_management.person',),
        ),
        migrations.AddField(
            model_name='patient',
            name='next_of_kin',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patient_management.nextofkin'),
        ),
    ]