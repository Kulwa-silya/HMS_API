from django_filters.rest_framework import FilterSet
from .models import *

class VitalSignsFilter(FilterSet):
  class Meta:
    model = VitalSigns
   
    fields = {
      'patient':['exact'],
      
      }