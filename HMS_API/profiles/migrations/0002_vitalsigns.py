# Generated by Django 4.2.7 on 2023-12-11 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VitalSigns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heart_rate', models.IntegerField()),
                ('blood_pressure_systolic', models.IntegerField()),
                ('blood_pressure_diastolic', models.IntegerField()),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('respiratory_rate', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.patient')),
            ],
        ),
    ]