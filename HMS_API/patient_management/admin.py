from django.contrib import admin
from .models import  Patient, NextOfKin

# Register your models here.
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'middle_name',
                    'last_name']
    list_filter = ['first_visit']
    list_per_page = 10
    search_fields = ['title']

@admin.register(NextOfKin)
class NextOfKinAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'middle_name',
                    'last_name']
    list_per_page = 10
    search_fields = ['title']