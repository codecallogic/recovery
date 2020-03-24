from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import SearchForm, SymptomsForm
from .models import Search, Symptoms
import infermedica_api

infermedica_api.configure(app_id='dd7d8ffc', app_key='805d0529637017534b6b5726f942c5b9')

class SearchView(TemplateView):
    template_name = 'patients/create_patients.html'

    def get(self, request):
        form = SearchForm()
        return render(request, self.template_name, {'form': form})
        
    def post(self, request):
        form = SearchForm(request.POST or None)
        if form.is_valid():
            new_search          = form.save(commit=False)
            new_search.user_id  = request.user.id
            query               = request.POST['query']
            api                 = infermedica_api.get_api()
            search              = api.search(query)
            new_search.save()
        else:
            print('false')
        
        context = {'form': form, 'query': query, 'search': search}
        return render(request, self.template_name , context)

class PatientSymptoms(TemplateView):
    template_name = 'patients/create_patients.html'

    def get(self, request):
        form = SearchForm()
        return render(request, self.template_name, {'form': form})

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

def home(request):
    return HttpResponse('Hello')

def about(request):
    return render(request, 'about.html')

def patients_index(request):
    return render(request, 'patients/index.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('patients_index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
    
    


# Create your views here.
