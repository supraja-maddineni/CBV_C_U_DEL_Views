from django.shortcuts import render
from app.models import *
# Create your views here.
from django.views.generic import TemplateView,ListView,DetailView

class Home(TemplateView):
    model=School
    template_name='app/Home.html'

class SchoolList(ListView):
    model=School
    context_object_name='schools'

class schooldetail(DetailView):
    model=School
    context_object_name='sclobject'