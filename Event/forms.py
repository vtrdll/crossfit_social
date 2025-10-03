from django import forms
from .models  import Event
from datetime import date

class  EventForm  (forms.ModelForm):
    date_initial = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class':'form-control'}),  input_formats  = ['%Y-%m-%d'], required=True)
    date_end  = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class':'form-control'}),  input_formats  = ['%Y-%m-%d'], required=True)


    class Meta():
        model =  Event
        fields  =  ['text','link', 'local', 'title','date_initial','date_end', 'price']
    
    def clean_date_initial (self):
        value = self.cleaned_data.get('date_initial')
        print(f'type {type(value)} value {value}')
        print(f'type {type(date.today())} value {date.today()}')

        if  value <  date.today():
            raise forms.ValidationError( 'DATA INVALIDA')
        return value
    

    def clean_date_end (self):
        value = self.cleaned_data.get('date_end')
       
        
        if  value >  date.today() :
            raise forms.ValidationError( 'DATA INVALIDA')
        return value


