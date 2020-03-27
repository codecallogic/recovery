from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import model_to_dict
from django import forms
from .forms import SearchForm, SymptomsForm, PatientForm, RecordForm
from .models import Search, Symptoms, Patient, Tracker
import infermedica_api

infermedica_api.configure(app_id='dd7d8ffc', app_key='805d0529637017534b6b5726f942c5b9')

class TrackerCreate(LoginRequiredMixin, CreateView):
  model = Tracker
  fields = '__all__'
  success_url = '/trackers/'

class TrackerUpdate(LoginRequiredMixin, UpdateView):
  model = Tracker
  fields = '__all__'

class TrackerDelete(LoginRequiredMixin, DeleteView):
  model = Tracker
  success_url = '/trackers/'

class SymptomsDelete(LoginRequiredMixin, DeleteView):
    model = Symptoms
    success_url = '/patients/lookup/'

def trackers_detail(request, tracker_id):
    tracker             = Tracker.objects.get(id=tracker_id)
    record_form         = RecordForm()
    arr                 = [tracker.label1, tracker.label2, tracker.label3]
    form_list           = zip(record_form, arr)
    return render(request, 'trackers/detail.html', {
         'tracker': tracker, 'record_form': record_form, 'arr': arr, 'form_list': form_list,
         })

def add_record(request, tracker_id):
    form = RecordForm(request.POST)
    if form.is_valid():
        new_record = form.save(commit=False)
        new_record.tracker_id = tracker_id
        new_record.save()
    return redirect('detail', tracker_id=tracker_id)

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
    template_name = 'trackers/index.html'

    def get(self, request):
        symptoms        = Symptoms.objects.filter(user_id = request.user)
        trackers        = Tracker.objects.all()
        form            = SearchForm()
        return render(request, self.template_name, {'form': form, 'symptoms': symptoms, 'trackers': trackers})

    def post(self, request): 
        symptoms        = Symptoms.objects.filter(user_id = request.user)
        arr             = []
        conditions      = []
        api             = infermedica_api.get_api()
        call            = infermedica_api.Diagnosis(sex='female', age=35)
        for s in symptoms:
            call.add_symptom(s.s_id, 'present', initial=True)
            arr.append(s.s_id)
        call            = api.diagnosis(call)
        conditions.append(call.conditions)
        print(conditions)
        context = {'arr': arr, 'symptoms': symptoms, 'conditions': conditions}
        return render(request, self.template_name, context)       

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

def login_success(request):
    if Patient.objects.filter(user_id = request.user).exists():
            return redirect('lookup')
    else:
        form = PatientForm()
        return render(request, 'patients/index.html', {'form': form})

