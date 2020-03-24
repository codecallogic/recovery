from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .forms import SearchForm
from .models import Search
# import infermedica_api

# infermedica_api.configure(app_id='dd7d8ffc', app_key='805d0529637017534b6b5726f942c5b9')

class SearchView(TemplateView):
    template_name = 'patients/create_patients.html'

    def get(self, request):
        form = SearchForm()
        return render(request, self.template_name, {'form': form})
        
    # def post(self, request):
    #     search = []
    #     form = SearchForm(request.POST or None)
    #     if form.is_valid():
    #         query = request.POST['query']
    #         api = infermedica_api.get_api()
    #         search = api.search(query)
    #         form.save()
        
        context = {'form': form, 'query': query, 'search': search}
        return render(request, self.template_name , context)

def home(request):
    return HttpResponse('Hello')

def about(request):
    return render(request, 'about.html')
    


# Create your views here.
