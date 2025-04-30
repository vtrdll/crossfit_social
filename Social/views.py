from django.shortcuts import render
from account.models import Profile
from Social.models import Post
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

# Create your views here.

@method_decorator(login_required(login_url='login'), name='dispatch')
class PostCreateView(CreateView):
    model = Post
    fields = ['text','photo']
    template_name = 'post.html'
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


class PostListView(ListView):
    model = Post
    template_name = 'users_list.html'
    context_object_name = 'posts'


class UsersList(ListView):
    model = User
    template_name = 'users_list.html'
    context_object_name = 'users'





class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'home.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object.user
        
        context['posts'] = Post.objects.filter(usuario=user)
        return context
    

def perfil_view(request):
    posts = request.user.post_set.all().order_by('-date')
    return render(request, 'meu_perfil.html', {'user': request.user, 'posts': posts})

def home_view(request):
    posts = Post.objects.select_related('author__profile').order_by('-date')
    return render(request, 'home.html', {'posts': posts})