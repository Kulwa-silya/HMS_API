from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from .models import *
from .serializers import *
from .filters import *
from .permissions import IsAdminOrReadOnly, IsDoctor



class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAdminUser]


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.prefetch_related('admissions', 'discharges').all()
    serializer_class = PatientSerializer


class AdmissionViewSet(viewsets.ModelViewSet):
    queryset = Admission.objects.select_related('patient', 'ward', 'room').all()
    serializer_class = AdmissionSerializer


class DischargeViewSet(viewsets.ModelViewSet):
    queryset = Discharge.objects.select_related('patient').all()
    serializer_class = DischargeSerializer



class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.select_related('patient', 'doctor', 'nurse', 'room').all()
    serializer_class = AppointmentSerializer
# views.py


class DiagnosisViewSet(viewsets.ModelViewSet):
    queryset = Diagnosis.objects.select_related('patient').all()
    serializer_class = DiagnosisSerializer


class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.select_related('patient', 'prescribed_medicine').all()
    serializer_class = MedicationSerializer

class InvoiceCategoryViewSet(viewsets.ModelViewSet):
    queryset = InvoiceCategory.objects.all()
    serializer_class = InvoiceCategorySerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.select_related('patient', 'category').all()
    serializer_class = InvoiceSerializer


class InsuranceViewSet(viewsets.ModelViewSet):
    queryset = Insurance.objects.select_related('provider', 'patient').all()
    serializer_class = InsuranceSerializer


class InsuranceProviderViewSet(viewsets.ModelViewSet):
    queryset = InsuranceProvider.objects.all()
    serializer_class = InsuranceProviderSerializer



class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer


class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.select_related('patient', 'doctor').all()
    serializer_class = PrescriptionSerializer
    permission_classes = [IsDoctor]


class PrescribedMedicineViewSet(viewsets.ModelViewSet):
    queryset = PrescribedMedicine.objects.select_related('prescription', 'medicine').all()
    serializer_class = PrescribedMedicineSerializer


class LabTestViewSet(viewsets.ModelViewSet):
    queryset = LabTest.objects.all()
    serializer_class = LabTestSerializer


class LabTestResultViewSet(viewsets.ModelViewSet):
    queryset = LabTestResult.objects.select_related('lab_test_request').all()
    serializer_class = LabTestResultSerializer


class ImagingReportViewSet(viewsets.ModelViewSet):
    queryset = ImagingReport.objects.all()
    serializer_class = ImagingReportSerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.prefetch_related('groups', 'user_permissions').all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]




class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class FinancialReportViewSet(viewsets.ModelViewSet):
    queryset = FinancialReport.objects.all()
    serializer_class = FinancialReportSerializer
# views.py


class AppointmentBookingViewSet(viewsets.ModelViewSet):
    queryset = AppointmentBooking.objects.all()
    serializer_class = AppointmentBookingSerializer


class CommunicationViewSet(viewsets.ModelViewSet):
    queryset = Communication.objects.all()
    serializer_class = CommunicationSerializer

# views.py


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

# views.py


class EmergencyRoomViewSet(viewsets.ModelViewSet):
    queryset = EmergencyRoom.objects.all()
    serializer_class = EmergencyRoomSerializer


class CriticalPatientViewSet(viewsets.ModelViewSet):
    queryset = CriticalPatient.objects.select_related('patient', 'emergency_room').all()
    serializer_class = CriticalPatientSerializer
# views.py


class CustomReportViewSet(viewsets.ModelViewSet):
    queryset = CustomReport.objects.all()
    serializer_class = CustomReportSerializer


class AnalyticsDataViewSet(viewsets.ModelViewSet):
    queryset = AnalyticsData.objects.all()
    serializer_class = AnalyticsDataSerializer

# views.py


class StaffRecruitmentViewSet(viewsets.ModelViewSet):
    queryset = StaffRecruitment.objects.all()
    serializer_class = StaffRecruitmentSerializer


class OnboardingViewSet(viewsets.ModelViewSet):
    queryset = Onboarding.objects.select_related('staff').all()
    serializer_class = OnboardingSerializer


class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer


class CertificationViewSet(viewsets.ModelViewSet):
    queryset = Certification.objects.select_related('staff', 'training').all()
    serializer_class = CertificationSerializer
# views.py


class RemoteConsultationViewSet(viewsets.ModelViewSet):
    queryset = RemoteConsultation.objects.select_related('patient', 'doctor').all()
    serializer_class = RemoteConsultationSerializer


class VideoConferenceViewSet(viewsets.ModelViewSet):
    queryset = VideoConference.objects.select_related('consultation').all()
    serializer_class = VideoConferenceSerializer


class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.select_related('consultation', 'sender').all()
    serializer_class = ChatSerializer
# views.py


class RegulatoryComplianceViewSet(viewsets.ModelViewSet):
    queryset = RegulatoryCompliance.objects.all()
    serializer_class = RegulatoryComplianceSerializer


class QualityAssuranceViewSet(viewsets.ModelViewSet):
    queryset = QualityAssurance.objects.select_related('staff').all()
    serializer_class = QualityAssuranceSerializer
# views.py


class HospitalSupplyViewSet(viewsets.ModelViewSet):
    queryset = HospitalSupply.objects.all()
    serializer_class = HospitalSupplySerializer
# views.py


class PatientFeedbackViewSet(viewsets.ModelViewSet):
    queryset = PatientFeedback.objects.select_related('patient').all()
    serializer_class = PatientFeedbackSerializer


class StaffPerformanceEvaluationViewSet(viewsets.ModelViewSet):
    queryset = StaffPerformanceEvaluation.objects.select_related('staff').all()
    serializer_class = StaffPerformanceEvaluationSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class WardViewSet(viewsets.ModelViewSet):
    queryset = Ward.objects.all()
    serializer_class = WardSerializer

class VitalSignsViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = VitalSignsFilter
    search_fields = ['patient']
    queryset = VitalSigns.objects.select_related('patient').all()
    serializer_class = VitalSignsSerializer