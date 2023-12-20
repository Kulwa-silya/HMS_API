from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):

 
    list_per_page = 10
 

admin.site.register(Insurance)
admin.site.register(InsuranceProvider)