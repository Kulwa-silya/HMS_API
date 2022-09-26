from distutils.text_file import TextFile
from django.db import models

# Create your models here.
class NextOfKin(models.Model):
    choices = (('Male','Male'),('Female','Female'))
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=6, choices=choices)
    birth_date = models.DateField()
    phone = models.CharField(max_length=12,unique=True)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['first_name', 'last_name']


class Patient(models.Model):
    choices = (('Male','Male'),('Female','Female'))
    
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=6, choices=choices)
    birth_date = models.DateField()
    phone = models.CharField(max_length=12,unique=True)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)

    first_visit = models.DateField(auto_now=True)
    next_of_kin = models.OneToOneField(NextOfKin,
                                         on_delete=models.CASCADE, 
                                         null=True,
                                         blank=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['first_name', 'last_name']

# class PatientHistory(models.Model):
#     date_of_visit = models.DateField(auto_now_add=True)
#     reason_of_visit = models.TextField(max_length=1000)
    