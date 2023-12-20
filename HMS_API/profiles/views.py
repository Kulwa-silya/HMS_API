from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from .filters import *



class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.select_related('next_of_kin').all()
    serializer_class = PatientSerializer


class AdmissionViewSet(viewsets.ModelViewSet):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer


class DischargeViewSet(viewsets.ModelViewSet):
    queryset = Discharge.objects.all()
    serializer_class = DischargeSerializer



class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
# views.py


class DiagnosisViewSet(viewsets.ModelViewSet):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSerializer


class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer

class InvoiceCategoryViewSet(viewsets.ModelViewSet):
    queryset = InvoiceCategory.objects.all()
    serializer_class = InvoiceCategorySerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class InsuranceViewSet(viewsets.ModelViewSet):
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer


class InsuranceProviderViewSet(viewsets.ModelViewSet):
    queryset = InsuranceProvider.objects.all()
    serializer_class = InsuranceProviderSerializer



class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer


class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer


class PrescribedMedicineViewSet(viewsets.ModelViewSet):
    queryset = PrescribedMedicine.objects.all()
    serializer_class = PrescribedMedicineSerializer


class LabTestViewSet(viewsets.ModelViewSet):
    queryset = LabTest.objects.all()
    serializer_class = LabTestSerializer


class LabTestResultViewSet(viewsets.ModelViewSet):
    queryset = LabTestResult.objects.all()
    serializer_class = LabTestResultSerializer


class ImagingReportViewSet(viewsets.ModelViewSet):
    queryset = ImagingReport.objects.all()
    serializer_class = ImagingReportSerializer



# class UserTypesViewSet(viewsets.ModelViewSet):
#     queryset = UserType.objects.all()
#     serializer_class = UserTypeSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer




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
    queryset = CriticalPatient.objects.all()
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
    queryset = Onboarding.objects.all()
    serializer_class = OnboardingSerializer


class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer


class CertificationViewSet(viewsets.ModelViewSet):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer
# views.py


class RemoteConsultationViewSet(viewsets.ModelViewSet):
    queryset = RemoteConsultation.objects.all()
    serializer_class = RemoteConsultationSerializer


class VideoConferenceViewSet(viewsets.ModelViewSet):
    queryset = VideoConference.objects.all()
    serializer_class = VideoConferenceSerializer


class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
# views.py


class RegulatoryComplianceViewSet(viewsets.ModelViewSet):
    queryset = RegulatoryCompliance.objects.all()
    serializer_class = RegulatoryComplianceSerializer


class QualityAssuranceViewSet(viewsets.ModelViewSet):
    queryset = QualityAssurance.objects.all()
    serializer_class = QualityAssuranceSerializer
# views.py


class HospitalSupplyViewSet(viewsets.ModelViewSet):
    queryset = HospitalSupply.objects.all()
    serializer_class = HospitalSupplySerializer
# views.py


class PatientFeedbackViewSet(viewsets.ModelViewSet):
    queryset = PatientFeedback.objects.all()
    serializer_class = PatientFeedbackSerializer


class StaffPerformanceEvaluationViewSet(viewsets.ModelViewSet):
    queryset = StaffPerformanceEvaluation.objects.all()
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