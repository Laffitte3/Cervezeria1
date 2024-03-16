from django.shortcuts import render
from .models import Cerveza
from django.views.generic import ListView
from django.views.generic.edit import CreateView
# Create your views here.

class CocuyListView(ListView):
    model = Cerveza
    template_name = 'home.html'

class BlogCreateView(CreateView):
    model = Cerveza #Mi modelo era en mayuscula????
    template_name = 'post_new.html'
    fields=['title','body','author']
    


