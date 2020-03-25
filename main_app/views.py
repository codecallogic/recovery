from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .forms import SearchForm, SymptomsForm, PatientForm
from .models import Search, Symptoms, Patient
import infermedica_api

# infermedica_api.configure(app_id='dd7d8ffc', app_key='805d0529637017534b6b5726f942c5b9')

class SearchView(TemplateView):
    template_name = 'patients/lookup.html'

    def get(self, request):
        symptoms        = Symptoms.objects.filter(user_id = request.user)
        form            = SearchForm()
        return render(request, self.template_name, {'form': form, 'symptoms': symptoms})
        
    def post(self, request):
        symptoms        = Symptoms.objects.filter(user_id = request.user)
        form            = SearchForm(request.POST or None)
        if form.is_valid():
            new_search          = form.save(commit=False)
            new_search.user_id  = request.user.id
            query               = request.POST['query']
            api                 = infermedica_api.get_api()
            search              = api.search(query)
            new_search.save()
        else:
            print('false')
        
        context = {'form': form, 'query': query, 'search': search, 'symptoms': symptoms}
        return render(request, self.template_name , context)

class PatientInfo(LoginRequiredMixin, TemplateView):
    template_name = 'patients/index.html'

    def get(self, request):
        if Patient.objects.filter(user_id = request.user).exists():
            return redirect('lookup')
        else:
            form = PatientForm()
            return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = PatientForm(request.POST or None)
        if form.is_valid():
            new_patient             = form.save(commit=False)
            print(request.user)
            new_patient.user_id     = request.user.id
            new_patient.save()
        else:
            print('false')
        
        context = {'form': form}
        return redirect('lookup')   
        

class PatientSymptoms(TemplateView):
    template_name = 'patients/lookup.html'

    def get(self, request):
        symptoms        = Symptoms.objects.filter(user_id = request.user)
        form = SearchForm()
        return render(request, self.template_name, {'form': form, 'symptoms': symptoms})

    def post(self, request):
        symptoms        = Symptoms.objects.filter(user_id = request.user)
        form            = SearchForm()
        symptomForm     = SymptomsForm(request.POST)
        if request.method == "POST":
           if symptomForm.is_valid():
               new_symptom          = symptomForm.save(commit=False)
               new_symptom.user_id  = request.user.id
               new_symptom.save()
        else:
            print('false')

        context = {'form': form, 'symptoms': symptoms}
        return render(request, self.template_name, context)

class PatientAssessment(TemplateView):
    template_name = 'patients/assessment.html'

    def get(self, request):
        symptoms        = Symptoms.objects.filter(user_id = request.user)
        form            = SearchForm()
        return render(request, self.template_name, {'form': form, 'symptoms': symptoms})

    def post(self, request):
        if request.POST:
            print('Hello')
            
        symptoms        = Symptoms.objects.filter(user_id = request.user)
        
        for s in symptoms:
            print(s)
        

def home(request):
    return render(request, 'index.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('patients')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

