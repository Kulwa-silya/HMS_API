from distutils.text_file import TextFile
from django.db import models

# Create your models here.

# models.py


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    # Add other necessary fields


class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
    # Add other necessary fields


class NextOfKin(models.Model):
    choices = (('Male', 'Male'), ('Female', 'Female'))
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=6, choices=choices)
    birth_date = models.DateField()
    phone = models.CharField(max_length=12, unique=True)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['first_name', 'last_name']


class Patient(models.Model):
    choices = (('Male', 'Male'), ('Female', 'Female'))

    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=6, choices=choices)
    birth_date = models.DateField()
    phone = models.CharField(max_length=12, unique=True)
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


class Admission(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    admission_date = models.DateField()
    ward = models.CharField(max_length=50)
    bed_number = models.IntegerField()
    # Add other necessary fields


class Discharge(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    discharge_date = models.DateField()


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    # Add other necessary fields


class Nurse(models.Model):
    name = models.CharField(max_length=100)
    # Add other necessary fields


class Room(models.Model):
    room_number = models.IntegerField(unique=True)
    # Add other necessary fields


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    # Add other necessary fields


class Diagnosis(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diagnosis_date = models.DateField()
    description = models.TextField()
    # Add other necessary fields


# models.py

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()
    # Add other necessary fields


class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    dosage = models.CharField(max_length=50)
    issue_date = models.DateField()
    # Add other necessary fields


class Medication(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medication_date = models.DateField()
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    # Add other necessary fields


# models.py

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
    provider = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    message = models.TextField()
    date = models.DateTimeField()
    # Add other necessary fields

# models.py


class Notification(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    message = models.TextField()
    date = models.DateTimeField()
    # Add other necessary fields


# models.py

class EmergencyRoom(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    # Add other necessary fields


class CriticalPatient(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    emergency_room = models.ForeignKey(EmergencyRoom, on_delete=models.CASCADE)
    handling_notes = models.TextField()
    # Add other necessary fields


# models.py

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
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
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

# models.py


class Invoice(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    invoice_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # Add other necessary fields


class Insurance(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    insurance_provider = models.CharField(max_length=100)
    policy_number = models.CharField(max_length=50)
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
