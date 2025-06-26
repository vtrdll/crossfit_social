from .forms import CommentForm

from .models import Post, Comment
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import PostCommentInventory
from django.http import HttpResponseNotAllowed
from django.views.generic.edit import FormMixin
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView



@method_decorator(login_required(login_url='login'), name='dispatch')
class PostCreateView(CreateView):
    model = Post
    fields = ['text','photo']
    template_name = 'post-create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDetail(DetailView):
    model = Post
    template_name = 'post-detail.html'

class PostUpdate(UpdateView):
    model = Post
    fields = ['text', 'photo']
    template_name ='post-update.html'
    context_object_name = 'post_update'
    success_url =reverse_lazy('my-perfil')

class PostDelete(DeleteView):
    model = Post 
    template_name = 'post-delete.html'
    success_url = reverse_lazy('my-perfil')

class HomeView(FormMixin, ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by("-created_at")
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
    
class PostList (ListView):
    model = Post 
    template_name = 'home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        context = Post.objects.all()
        search = self.request.GET.get('search')

        if search:
           return Post.objects.filter(text__icontains=search)
           

        return context
    
class CommentList(ListView):
    model = Comment
    template_name = 'comment-list.html'

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])

        return Comment.objects.filter(post=post)

class CommentUpdate(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment-update.html'
    success_url = reverse_lazy ('home')

class CommentDelete(DeleteView):
    model = Comment
    template_name = 'comment-delete.html'
    success_url = reverse_lazy('home')

def my_profile(request):
    user = request.user
    posts = request.user.post_set.all().order_by('-created_at')
    comments = request.user.comment_set.all().order_by('-created_at')

    inventory_post = PostCommentInventory.objects.filter(author=user).first()
    return render(request, 'my_perfil.html', {'user': request.user, 'posts': posts, 'comments':comments, 'inventory_post': inventory_post, 'mostrar_inventory':True})

def like_post(request, pk):

    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    
    user = request.user
    post = get_object_or_404(Post, pk=pk)

    if user in post.like.all():
        post.like.remove(user)
    else:
        post.like.add(user)
    

    return redirect (reverse_lazy('home'))

def like_comment (request, pk):
     
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    
    user = request.user
    comment = get_object_or_404(Comment, pk=pk)
    
    if user in comment.like_comment.all():
        comment.like_comment.remove(user)
    else:
        comment.like_comment.add(user)
    return redirect(reverse_lazy('home'))
         

