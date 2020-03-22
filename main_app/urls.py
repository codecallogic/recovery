from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('patients/create/', views.SearchView.as_view(), name='create_patients'),
]