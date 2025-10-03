from django.shortcuts import render, redirect,  HttpResponse

from .form import WodForm
from  .models import WOD

from django.http import HttpResponseNotAllowed
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render
# Create your views here.





'''


def create_wod (request):
    coach = request.user.profile

    if request.method == 'POST':
        formset =  WoodInlineFormSet (request.POST, instance= coach)
        if formset.is_valid():
            formset.save()

            return redirect('home')
            
        else:
            formset  =WoodInlineFormSet(instance= coach)
            HttpResponse(formset)

    else:
        formset = WoodInlineFormSet
        
    
    return render(request, 'wod_create.html', {'formset':formset  })''''''
'''
def create_wod(request):
    if request.method == "POST" and request.user.profile.is_coach:
        form = WodForm(request.POST)
        if form.is_valid():
            wod = form.save(commit=False)
            wod.coach = request.user.profile  # pega o perfil do usuário logado
            wod.save()
            return redirect(reverse_lazy("home"))
    else:
        form = WodForm()

    return render(request, "create_wod.html", {"form": form})





def like_wod (request, pk):
    
    if request.method != 'POST':
        return  HttpResponseNotAllowed(['POST'])
    
    user =  request.user
    wod = get_object_or_404  (WOD,pk=pk)

    if user in wod.like.all():
        wod.like.remove(user)
    else:
        wod.like.add(user)
    

    return redirect (reverse_lazy('home'))
