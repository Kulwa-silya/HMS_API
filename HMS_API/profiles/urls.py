# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'wards', WardViewSet, basename='ward')
router.register(r'cities', CityViewSet, basename='city')
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'admissions', AdmissionViewSet, basename='admission')
router.register(r'discharges', DischargeViewSet, basename='discharge')
router.register(r'rooms', RoomViewSet, basename='room')
router.register(r'appointments', AppointmentViewSet, basename='appointment')
router.register(r'diagnoses', DiagnosisViewSet, basename='diagnosis')
router.register(r'medications', MedicationViewSet, basename='medication')
router.register(r'invoices', InvoiceViewSet, basename='invoice')
router.register(r'invoices-categories', InvoiceCategoryViewSet, basename='invoice-categories')
router.register(r'insurances', InsuranceViewSet, basename='insurance')
router.register(r'medicines', MedicineViewSet, basename='medicine')
router.register(r'prescriptions', PrescriptionViewSet, basename='prescription')
router.register(r'users', UserViewSet, basename='user')
router.register(r'user-types', UserTypesViewSet, basename='user-types')
router.register(r'userroles', UserRoleViewSet, basename='userrole')
router.register(r'budgets', BudgetViewSet, basename='budget')
router.register(r'expenses', ExpenseViewSet, basename='expense')
router.register(r'financialreports', FinancialReportViewSet,
                basename='financialreport')
router.register(r'appointmentbookings', AppointmentBookingViewSet,
                basename='appointmentbooking')
router.register(r'communications', CommunicationViewSet,
                basename='communication')
router.register(r'notifications', NotificationViewSet, basename='notification')
router.register(r'emergencyrooms', EmergencyRoomViewSet,
                basename='emergencyroom')
router.register(r'criticalpatients', CriticalPatientViewSet,
                basename='criticalpatient')
router.register(r'customreports', CustomReportViewSet, basename='customreport')
router.register(r'analyticsdata', AnalyticsDataViewSet,
                basename='analyticsdata')
router.register(r'staffrecruitments', StaffRecruitmentViewSet,
                basename='staffrecruitment')
router.register(r'onboardings', OnboardingViewSet, basename='onboarding')
router.register(r'trainings', TrainingViewSet, basename='training')
router.register(r'certifications', CertificationViewSet,
                basename='certification')
router.register(r'remoteconsultations', RemoteConsultationViewSet,
                basename='remoteconsultation')
router.register(r'videoconferences', VideoConferenceViewSet,
                basename='videoconference')
router.register(r'chats', ChatViewSet, basename='chat')
router.register(r'regulatorycompliances',
                RegulatoryComplianceViewSet, basename='regulatorycompliance')
router.register(r'qualityassurances', QualityAssuranceViewSet,
                basename='qualityassurance')
router.register(r'hospitalsupplies', HospitalSupplyViewSet,
                basename='hospitalsupply')
router.register(r'patientfeedbacks', PatientFeedbackViewSet,
                basename='patientfeedback')
router.register(r'staffperformanceevaluations',
                StaffPerformanceEvaluationViewSet, basename='staffperformanceevaluation')


urlpatterns = [
    path('', include(router.urls)),
]
