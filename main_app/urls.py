from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('patients/', views.PatientInfo.as_view(), name='patients'),
    path('patients/lookup/', views.SearchView.as_view(), name='lookup'),
    path('patients/symptoms/', views.PatientSymptoms.as_view(), name='patients_symptoms'),
    path('accounts/signup/', views.signup, name='signup'),
    path('patients/assessment/', views.PatientAssessment.as_view(), name='patients_assessment'),
]