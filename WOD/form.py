from django import forms

from .models import WOD


class WodForm(forms.ModelForm):
    


    class  Meta():

        model = WOD
        fields = ['description_wod','title','pinned','elite','rx', 'amauter', 'scaled','fit' ]


