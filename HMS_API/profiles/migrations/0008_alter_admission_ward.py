# Generated by Django 4.2.7 on 2023-11-22 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_remove_room_room_number_room_number_room_room_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='ward',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.ward'),
        ),
    ]
