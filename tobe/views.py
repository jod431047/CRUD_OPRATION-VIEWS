from django.shortcuts import render
from .models import Tobe
# Create your views here.
from django.views import generic






class TobeList(generic.ListView):
    model = Tobe
    
    
class TobeDetail(generic.DetailView):
    model = Tobe
    
    
    
class TobeCreate(generic.CreateView):  # creating view
    model = Tobe
    fields = '__all__'
    success_url = '/list/'
    
    
class TobeEdit(generic.UpdateView):  # Editing the created post
    model = Tobe
    fields = '__all__'
    success_url = '/list/' # by redirect
    template_name = 'tobe/edit.html' # change the template name by default
    
class TobeDelete(generic.DeleteView): # Delete the created post
    model = Tobe
    success_url = '/list/'    