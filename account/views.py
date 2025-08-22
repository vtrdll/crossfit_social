from .models import Profile
from .models  import ProfilePersonalRecord
from django.urls import reverse_lazy
from Social.models import Comment, Post 
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm
from django.views.generic import UpdateView, FormView, DeleteView, DetailView, ListView
from .forms import ProfileForm, UserFormUpdate, ProfileFormUpdate,CustomCreateUser, PersonalRecordForm, PrivacyConfigForm


def register_view(request):
    if request.method == "POST":
        
        user_form = CustomCreateUser(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if user_form.is_valid():
            print('ok')
        else:
            
            print(user_form.errors)
        
        if profile_form.is_valid():
            print('ok')
        else:
            
            print(profile_form.errors)



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


class UserList(ListView):
    model = User
    template_name = 'home.html'
    context_object_name = 'search_users'
    
    def get_queryset(self):
        
        search  = self.request.GET.get('search')
        if search:
            return User.objects.filter(username__icontains = search)
        
        return User.objects.all()



@method_decorator(login_required(login_url='login'), name='dispatch')
class UserUpdate(UpdateView):


    model = User
    form_class = UserFormUpdate
    template_name = 'user-update.html'
    success_url = reverse_lazy('my_perfil')

    
    def get_object(self):
        
        return self.request.user

    def form_valid(self, form):
        print("Dados recebidos no POST:", self.request.POST)
        response = super().form_valid(form)

        # Atualiza também o perfil
        profile = self.request.user.profile
        profile.box = self.request.POST.get('box')
        profile.category = self.request.POST.get('category')
        profile.weight = self.request.POST.get('weight')
        profile.height =  self.request.POST.get('height')
        profile.genre = self.request.POST.get('genre')
        
        
        profile.save()

        return response
    
    def form_invalid(self, form):
        print("Dados recebidos no POST:", self.request.POST)
        # You can print the errors to debug
        print(form.errors)

        # You can log or customize the response here
        return super().form_invalid(form)

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
class UserConfig(DetailView):
    model = Profile 
    template_name = 'config_account.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return self.request.user.profile  


@method_decorator(login_required(login_url='login'), name='dispatch')
class PhotoUpdate(UpdateView):
    model = Profile 
    form_class = ProfileFormUpdate
    template_name = 'photo-update.html'
    success_url = reverse_lazy('my_perfil')
    

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
    

def register_pr (request):
    
    if request.method == 'POST':
        form = PersonalRecordForm(request.POST, user=request.user)

        if form.is_valid():
            pr =  form.save(commit=False)
            pr.athlete = request.user
            pr.save()
            return redirect('my_perfil')
        
    else:
        form  = PersonalRecordForm()

    return  render (request, 'create_pr.html',{'form':form})

def update_pr (request,pk):
    obj =  get_object_or_404(ProfilePersonalRecord,  pk  = pk)
    
    if  obj.athlete!=request.user:
        return HttpResponseForbidden("Você não tem permissão para editar este registro.")

    if request.method =='POST':
        new_pr =  request.POST.get('personal_record')
        
        if new_pr:
            obj.personal_record = new_pr
            obj.save()
            return redirect('my_perfil')
    return render  (request,'update_pr.html',{'obj':obj})

def list_pr(request):

    detail = ProfilePersonalRecord.objects.filter(athlete=request.user)

    return render(request, 'list_pr.html',  {'detail':detail})

def privacy_config (request):
    profile = request.user.profile
    
    if request.method  == 'POST':
        form  = PrivacyConfigForm(request.POST, instance=  profile)
        if  form.is_valid():
            form.save()
            return redirect('my_perfil')
    else:
        form = PrivacyConfigForm(instance=  profile)
    
    return render(request, 'privacy_settings.html', {'form': form})