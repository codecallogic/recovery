from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login_success/', views.login_success, name='login_success'),
    path('patients/', views.PatientInfo.as_view(), name='patients'),
    path('patients/lookup/', views.SearchView.as_view(), name='lookup'),
    path('patients/symptoms/', views.PatientSymptoms.as_view(), name='patients_symptoms'),
    path('patients/<int:pk>/delete/', views.SymptomsDelete.as_view(), name='symptoms_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('trackers/', views.PatientAssessment.as_view(), name='patients_assessment'),
    # path('trackers/', views.trackers_index, name='index'),
    path('trackers/<int:tracker_id>/', views.trackers_detail, name='detail'),
    path('trackers/create/', views.TrackerCreate.as_view(), name='trackers_create'),
    path('trackers/<int:pk>/update/', views.TrackerUpdate.as_view(), name='trackers_update'),
    path('trackers/<int:pk>/delete/', views.TrackerDelete.as_view(), name='trackers_delete'),
    path('trackers/<int:tracker_id>/add_record/', views.add_record, name='add_record'),
]