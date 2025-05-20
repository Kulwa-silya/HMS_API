from distutils.text_file import TextFile
from django.db import models
from django.contrib.auth.models import AbstractUser, Group,  Permission
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.contrib.auth.models import User, Group
from django.core.validators import MinValueValidator
# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


    
class InsuranceProvider(models.Model):
    name = models.CharField(max_length=100)
    policy_number = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Patient(models.Model):
    choices = (('Male', 'Male'), ('Female', 'Female'))

    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=6, choices=choices)
    birth_date = models.DateField()
    phone = models.CharField(max_length=12, unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    first_visit = models.DateField(auto_now_add=True)
    last_visit = models.DateField(auto_now=True)
    

    next_of_kin_first_name = models.CharField(max_length=255, default='abc')
    next_of_kin_middle_name = models.CharField(max_length=255, default='abc')
    next_of_kin_last_name = models.CharField(max_length=255, default='abc')
    next_of_kin_gender = models.CharField(max_length=6, choices=choices, default='Male')
    next_of_kin_phone = models.CharField(max_length=12, default='0717553945')
    
    
                                       

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['first_name', 'last_name']


class VitalSigns(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    heart_rate = models.IntegerField()
    blood_pressure_systolic = models.IntegerField()
    blood_pressure_diastolic = models.IntegerField()
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    respiratory_rate = models.IntegerField()
    weight = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Vital Signs for {self.patient} - {self.timestamp}'




class Insurance(models.Model):
    card_number = models.IntegerField(default=0)
    membership_number = models.IntegerField(default=0)
    authorization_number = models.IntegerField(default=0, null=True)
    provider = models.ForeignKey(InsuranceProvider, on_delete=models.CASCADE, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, default=0)






class Room(models.Model):
    APPOINTMENT = 'APPOINTMENT'
    PATIENT = 'PATIENT'

    ROOM_TYPE_CHOICES = [
        (APPOINTMENT, 'Appointment'),
        (PATIENT, 'Patient'),
    ]

    number = models.CharField(max_length=2, default='00')
    room_type = models.CharField(max_length=12, choices=ROOM_TYPE_CHOICES, default=PATIENT)

    def __str__(self):
        return 'room number '+self.number+'-'+self.room_type



class Ward(models.Model):
    name = models.CharField(max_length=100)
    rooms = models.IntegerField()
    beds_per_room = models.IntegerField()

    def __str__(self):
        return self.name

class Admission(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    admission_date = models.DateField()
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    
    


class Discharge(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    discharge_date = models.DateField()


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patient_appointments')
    doctor = models.ForeignKey(User, related_name='doctor_appointments',on_delete=models.CASCADE, limit_choices_to={'groups__name': 'Doctor'})
    nurse = models.ForeignKey(User, related_name='nurse_appointments',on_delete=models.CASCADE, limit_choices_to={'groups__name': 'Nurse'})
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    


class Diagnosis(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diagnosis_date = models.DateField()
    description = models.TextField()



class Medicine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    manufacturer = models.CharField(max_length=100, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=200)
    expire_date = models.DateField(default='2023-01-01')

    def __str__(self):
        return self.name

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'groups__name': 'Doctor'})
    issue_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Prescription for {self.patient} by Dr. {self.doctor}"

class PrescribedMedicine(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    dosage = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.medicine.name} prescribed in {self.prescription}"

class Medication(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medication_date = models.DateField()
    prescribed_medicine = models.ForeignKey(PrescribedMedicine, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Medication for {self.patient} on {self.medication_date}"


class Budget(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # Add other necessary fields


class Expense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    


class FinancialReport(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    


# models.py

class AppointmentBooking(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    reason = models.TextField()
    


class Communication(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    provider = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'groups__name': 'Doctor'})
    message = models.TextField()
    date = models.DateTimeField()
    


class Notification(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    message = models.TextField()
    date = models.DateTimeField()
    





    

class Bed(models.Model):
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    bed_number = models.CharField(max_length=10)
    

    

class EmergencyRoom(models.Model):
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE, null=True, blank=True)
    capacity = models.IntegerField()

    
    

class CriticalPatient(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    emergency_room = models.ForeignKey(EmergencyRoom, on_delete=models.CASCADE)
    handling_notes = models.TextField()

    
    

class CustomReport(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    # Add other necessary fields


class AnalyticsData(models.Model):
    date = models.DateField()
    performance_metric = models.FloatField()
    # Add other necessary fields


# models.py

class StaffRecruitment(models.Model):
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    recruitment_date = models.DateField()
    # Add other necessary fields


class Onboarding(models.Model):
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
    onboarding_date = models.DateField()
    training_notes = models.TextField()
    # Add other necessary fields


class Training(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Add other necessary fields


class Certification(models.Model):
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    certification_date = models.DateField()
    # Add other necessary fields


# models.py

class RemoteConsultation(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'groups__name': 'Doctor'})
    consultation_date = models.DateTimeField()
    consultation_notes = models.TextField()
    # Add other necessary fields


class VideoConference(models.Model):
    consultation = models.ForeignKey(
        RemoteConsultation, on_delete=models.CASCADE)
    video_url = models.URLField()
    # Add other necessary fields


class Chat(models.Model):
    consultation = models.ForeignKey(
        RemoteConsultation, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    # Add other necessary fields


# models.py

class RegulatoryCompliance(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    compliance_date = models.DateField()
    # Add other necessary fields


class QualityAssurance(models.Model):
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
    improvement_notes = models.TextField()
    improvement_date = models.DateField()
    # Add other necessary fields


# models.py

class HospitalSupply(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    # Add other necessary fields


# models.py

class PatientFeedback(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    feedback_date = models.DateField()
    feedback_text = models.TextField()
    # Add other necessary fields


class StaffPerformanceEvaluation(models.Model):
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
    evaluation_date = models.DateField()
    performance_notes = models.TextField()
    # Add other necessary fields



class InvoiceCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Invoice(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('insurance', 'Insurance'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    invoice_date = models.DateField(auto_now=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    category = models.ForeignKey(InvoiceCategory, on_delete=models.CASCADE, default=0)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='cash')


class LabTest(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class LabTestRequest(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    requested_tests = models.ManyToManyField(LabTest)
    request_date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Lab Test Request for {self.patient} on {self.request_date}"

class LabTestResult(models.Model):
    lab_test_request = models.ForeignKey(LabTestRequest, on_delete=models.CASCADE)
    result_date = models.DateField(auto_now_add=True)
    results = models.TextField()

    def __str__(self):
        return f"Lab Test Result for {self.lab_test_request.patient} on {self.result_date}"

    

class ImagingReport(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    description = models.TextField()
    report_date = models.DateField()


class User(AbstractUser):   
    username = models.CharField(max_length=100, unique=True)
    # password = models.CharField(max_length=100)
    groups = models.ManyToManyField(Group, related_name='auth_user_groups', null=True, blank=True)
    user_permissions = models.ManyToManyField(
        Permission, related_name='auth_user_permissions',null=True, blank=True
    )
    
