from distutils.text_file import TextFile
from django.db import models
from django.contrib.auth.models import AbstractUser, Group,  Permission
# Create your models here.

class UserType(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    user_type = models.ForeignKey(UserType, on_delete=models.SET_NULL, null=True)   
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    groups = models.ManyToManyField(Group, related_name='auth_user_groups', null=True, blank=True)
    user_permissions = models.ManyToManyField(
        Permission, related_name='auth_user_permissions',null=True, blank=True
    )
    


class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)

class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class NextOfKin(models.Model):
    choices = (('Male', 'Male'), ('Female', 'Female'))
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=6, choices=choices)
    birth_date = models.DateField()
    phone = models.CharField(max_length=12, unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['first_name', 'last_name']


class Insurance(models.Model):
    insurance_provider = models.CharField(max_length=100)
    policy_number = models.CharField(max_length=50)

    def __str__(self):
        return self.insurance_provider

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
    insurance = models.OneToOneField(Insurance, on_delete=models.SET_NULL, null=True, blank=True)
    
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
    doctor = models.ForeignKey(User, related_name='doctor_appointments',on_delete=models.CASCADE, limit_choices_to={'user_type__name': 'Doctor'})
    nurse = models.ForeignKey(User, related_name='nurse_appointments',on_delete=models.CASCADE, limit_choices_to={'user_type__name': 'Nurse'})
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    


class Diagnosis(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diagnosis_date = models.DateField()
    description = models.TextField()



class Medicine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()
    manufacturer = models.CharField(max_length=100, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=200)
    expire_date = models.DateField(default='2023-01-01')

    def __str__(self):
        return self.name

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'user_type__name': 'Doctor'})
    issue_date = models.DateField()

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
    # Add other necessary fields


class FinancialReport(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    # Add other necessary fields


# models.py

class AppointmentBooking(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    reason = models.TextField()
    # Add other necessary fields


class Communication(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    provider = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'user_type__name': 'Doctor'})
    message = models.TextField()
    date = models.DateTimeField()
    


class Notification(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    message = models.TextField()
    date = models.DateTimeField()
    # Add other necessary fields





    

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
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'user_type__name': 'Doctor'})
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
    invoice_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(InvoiceCategory, on_delete=models.CASCADE, default=0)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='cash')
    # Add other necessary fields



    
    # Add other necessary fields


# models.py

class Test(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Add other necessary fields


class TestResult(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    result_date = models.DateField()
    result_description = models.TextField()
    # Add other necessary fields


class ImagingReport(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    description = models.TextField()
    report_date = models.DateField()
    # Add other necessary fields
