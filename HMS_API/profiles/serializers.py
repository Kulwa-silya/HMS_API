from .models import Doctor, Nurse, Room, Appointment
from .models import *
from rest_framework import serializers




class NextOfKinSerializer(serializers.ModelSerializer):
    class Meta:
        model = NextOfKin
        fields = '__all__'


class AdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admission
        fields = '__all__'


class DischargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discharge
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
    next_of_kin = NextOfKinSerializer()
    admissions = AdmissionSerializer(many=True, read_only=True)
    discharges = DischargeSerializer(many=True, read_only=True)

    class Meta:
        model = Patient
        fields = '__all__'
        # fields = ['id', 'first_name', 'middle_name', 'gender',
        #           'last_name', 'birth_date', 'phone', 'city', 'street', 'next_of_kin']

    def create(self, validated_data):
        next_of_kin = validated_data.pop('next_of_kin')
        next_of_kin_instance = NextOfKin.objects.create(**next_of_kin)
        patient_instance = Patient.objects.create(
            next_of_kin=next_of_kin_instance, **validated_data)
        return patient_instance


# class PatientSerializer(serializers.ModelSerializer):
#     admissions = AdmissionSerializer(many=True, read_only=True)
#     discharges = DischargeSerializer(many=True, read_only=True)

#     class Meta:
#         model = Patient
#         fields = '__all__'
# serializers.py


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
# serializers.py


class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = '__all__'


class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = '__all__'
# serializers.py


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'


class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = '__all__'


# serializers.py

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'


class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'


# serializers.py

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'


class TestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResult
        fields = '__all__'


class ImagingReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagingReport
        fields = '__all__'


# serializers.py

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = '__all__'

# serializers.py


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'


class FinancialReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialReport
        fields = '__all__'

# serializers.py


class AppointmentBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentBooking
        fields = '__all__'


class CommunicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Communication
        fields = '__all__'


# serializers.py

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'


# serializers.py

class EmergencyRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyRoom
        fields = '__all__'


class CriticalPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = CriticalPatient
        fields = '__all__'


# serializers.py

class CustomReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomReport
        fields = '__all__'


class AnalyticsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalyticsData
        fields = '__all__'

# serializers.py


class StaffRecruitmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffRecruitment
        fields = '__all__'


class OnboardingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Onboarding
        fields = '__all__'


class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = '__all__'


class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = '__all__'

# serializers.py


class RemoteConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RemoteConsultation
        fields = '__all__'


class VideoConferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoConference
        fields = '__all__'


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'
# serializers.py


class RegulatoryComplianceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegulatoryCompliance
        fields = '__all__'


class QualityAssuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityAssurance
        fields = '__all__'
# serializers.py


class HospitalSupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalSupply
        fields = '__all__'

# serializers.py


class PatientFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientFeedback
        fields = '__all__'


class StaffPerformanceEvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffPerformanceEvaluation
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = '__all__'