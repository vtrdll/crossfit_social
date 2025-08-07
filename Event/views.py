from django.shortcuts import render
from .forms import EventForm
from django.views.generic import CreateView, ListView
from .models import Event
from django.urls import reverse_lazy
# Create your views here.


class EventCreate  (CreateView):
    model = Event
    form_class  =  EventForm
    template_name  = 'create_event.html'
    success_url =  reverse_lazy('home')
    


    
    def form_valid(self, form, ):

        form.instance.author = self.request.user

        return super().form_valid(form)
    
    def form_invalid(self, form):
        print("FORM INVÁLIDO:", form.errors)  # isso imprime no terminal
        return super().form_invalid(form)
    


class EventList(ListView):
    model = Event 
    template_name  ='event_list.html'
    fields  = ['date_initial','date_end', 'text','link', 'title','local']
   