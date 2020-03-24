from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('patients/', views.patients_index, name='patients_index'),
    path('patients/create/', views.SearchView.as_view(), name='create_patients'),
    path('patients/symptoms/', views.PatientSymptoms.as_view(), name='patients_symptoms'),
    path('accounts/signup/', views.signup, name='signup'),
]