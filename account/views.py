from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,SetPasswordForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from account.models import Profile
from django.contrib.auth.models import User
from account.forms import ProfileForm, UserForm, PasswordForm
from django.views.generic import UpdateView, FormView
from django.urls import reverse_lazy


def register_view(request):
    if request.method == "POST":
        
        user_form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            return redirect('login')
    else:
        user_form = UserCreationForm()
        profile_form = ProfileForm()

    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form})


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            login_form = AuthenticationForm()
    else:
        login_form = AuthenticationForm()
    return render(request, 'login.html', {'login_form': login_form})


def logout_view(request):
    logout(request)
    return redirect('login')


class UserUpdate(UpdateView):
    model = User
    form_class = UserForm
    
    
    template_name = 'user-update.html'
    success_url = reverse_lazy('my-perfil')


    def get_object(self):
        return self.request.user
    


class PasswordUpdate(LoginRequiredMixin, FormView):
    template_name = 'pass-update.html'
    form_class = SetPasswordForm
    success_url = reverse_lazy('login')  # redirecionamento após sucesso

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Passando o usuário para o formulário
        return kwargs

    def form_valid(self, form):
        form.save()  # Salva a nova senha
        return super().form_valid(form)
