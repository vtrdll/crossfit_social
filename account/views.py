from .models import Profile
from django.urls import reverse_lazy
from Social.models import Comment, Post
from django.contrib.auth.models import User

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm
from django.views.generic import UpdateView, FormView, DeleteView, DetailView
from .forms import ProfileForm, UserFormUpdate, ProfileFormUpdate,CustomCreateUser


def register_view(request):
    if request.method == "POST":
        
        user_form = CustomCreateUser(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            return redirect('login')
    else:
        user_form = CustomCreateUser()
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


@method_decorator(login_required(login_url='login'), name='dispatch')
class UserUpdate(UpdateView):


    model = User
    form_class = UserFormUpdate
    template_name = 'user-update.html'
    success_url = reverse_lazy('my-perfil')

    def get_object(self):
        return self.request.user
    

@method_decorator(login_required(login_url='login'), name='dispatch')
class PasswordUpdate(LoginRequiredMixin, FormView):
    template_name = 'pass-update.html'
    form_class = SetPasswordForm
    success_url = reverse_lazy('login') 

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  
        return kwargs

    def form_valid(self, form):
        form.save()  
        return super().form_valid(form)
    

@method_decorator(login_required(login_url='login'), name='dispatch')
class UserDelete(DeleteView):
    model = User
    template_name = 'user-delete.html'
    success_url = reverse_lazy ('home')

    
@method_decorator(login_required(login_url='login'), name='dispatch')
class UserDetail(DetailView):
    model = Profile 
    template_name = 'configuracao.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return self.request.user.profile  


@method_decorator(login_required(login_url='login'), name='dispatch')
class PhotoUpdate(UpdateView):
    model = Profile 
    form_class = ProfileFormUpdate
    template_name = 'photo-update.html'
    success_url = reverse_lazy('my-perfil')
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'update'  
        return context
    
    def get_object(self, queryset=None):
        return self.request.user.profile 
    
    
@method_decorator(login_required(login_url='login'), name='dispatch')
class PhotoDelete(DeleteView):
    model = Profile
    template_name = 'photo-update.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.photo.delete(save=True)
        return redirect('user-detail', pk=self.object.user.pk)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.action = 'delete'  
        return context

    def get_object(self, queryset = ...):
        return self.request.user.profile
    
class ProfileDetail(DetailView):

    def get(self, request, pk):
        user_profile = get_object_or_404(User, pk=pk)
        posts = Post.objects.filter(author=user_profile).order_by('-created_at')
        comments = Comment.objects.filter(author=user_profile).order_by('-created_at')
        return render(request, 'profile.html', {
            'user_profile': user_profile,
            'posts': posts,
            'comments': comments,
        })