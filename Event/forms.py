from django import forms
from .models  import Event


class  EventForm  (forms.ModelForm):
    date_initial = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class':'form-control'}),  input_formats  = ['%Y-%m-%d'], required=True)
    date_end  = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class':'form-control'}),  input_formats  = ['%Y-%m-%d'], required=True)


    class Meta():
        model =  Event
        fields  =  ['text','link', 'local', 'title','date_initial','date_end', 'price']
    
    
