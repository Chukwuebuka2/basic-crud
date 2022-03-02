from django.shortcuts import render
from django.views.generic import (View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from . import models
from django.urls import reverse_lazy

# Create your views here.
'''def index(request):
    return render(request, 'index.html')'''

# Now using class based views 

'''class CBView(View):
    def get(self, request):
        return HttpResponse("<h1> CLASS BASED VIEWS ARE COOL! </h1>")'''

class IndexView (TemplateView):
    template_name = 'index.html'

'''
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['injectme'] = "BASIC INJECTION!"
        return context
'''

class SchoolListView(ListView):
    model = models.School

    # Or we can say context_object_name = 'schools'. In this way we have redefined it to be schools and no longer school_list
    #template_name = 'basic_app/school_list.html'

class SchoolDetailView(DetailView):
    model = models.School
    context_object_name = 'school_detail'
    # but the detail view just turns to lower case but we can choose to redfine our own to what we want

    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('basic_app:list')