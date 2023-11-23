from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *



# # Create your views here.
# class PatientList(APIView):
#     def get(self, request):
#         queryset = Patient.objects.select_related('next_of_kin').all()
#         serializer = PatientSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = PatientSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.select_related('next_of_kin').all()
    serializer_class = PatientSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class AdmissionViewSet(viewsets.ModelViewSet):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer


class DischargeViewSet(viewsets.ModelViewSet):
    queryset = Discharge.objects.all()
    serializer_class = DischargeSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class NurseViewSet(viewsets.ModelViewSet):
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer


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
# views.py


class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer


class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
# views.py


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TestResultViewSet(viewsets.ModelViewSet):
    queryset = TestResult.objects.all()
    serializer_class = TestResultSerializer


class ImagingReportViewSet(viewsets.ModelViewSet):
    queryset = ImagingReport.objects.all()
    serializer_class = ImagingReportSerializer
# views.py


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRoleViewSet(viewsets.ModelViewSet):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer

# views.py


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