from django.shortcuts import render
from account.models import Profile
from Social.models import Post
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from .forms import CommentForm
# Create your views here.




@method_decorator(login_required(login_url='login'), name='dispatch')
class PostCreateView(CreateView):
    model = Post
    fields = ['text','photo']
    template_name = 'post.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class HomeView(FormMixin, ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    form_class = CommentForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()  
        form = self.get_form()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post_id = request.POST.get('post_id')  
            comment.save()
            return self.form_valid(form)
        return self.form_invalid(form)

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
    return render(request, 'my_perfil.html', {'user': request.user, 'posts': posts})




class PostUpdate(UpdateView):
    model = Post
    fields = ['text', 'photo']
    template_name ='post-edit.html'
    context_object_name = 'post_update'
    success_url =reverse_lazy('my-perfil')
    


class PostDelete(DeleteView):
    model = Post 
    template_name = 'post-delete.html'
    success_url = reverse_lazy('my-perfil')


