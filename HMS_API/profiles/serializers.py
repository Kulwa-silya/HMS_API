from .models import Patient, NextOfKin
from rest_framework import serializers

class NextOfKinSerializer(serializers.ModelSerializer):
    class Meta:
        model = NextOfKin
        fields = ['id', 'first_name', 'middle_name' , 'gender',
                'last_name', 'birth_date', 'phone' , 'city', 'street']
     
class PatientSerializer(serializers.ModelSerializer):
    next_of_kin = NextOfKinSerializer()
    class Meta:
        model = Patient 
        fields = ['id', 'first_name', 'middle_name' , 'gender',
                'last_name', 'birth_date', 'phone' , 'city', 'street', 'next_of_kin']

    def create(self, validated_data):
        next_of_kin = validated_data.pop('next_of_kin')
        next_of_kin_instance = NextOfKin.objects.create(**next_of_kin)
        patient_instance = Patient.objects.create(next_of_kin=next_of_kin_instance, **validated_data)
        return patient_instance
