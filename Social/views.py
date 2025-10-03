
import random 
from WOD.models import  WOD
from django.http import Http404
from django.urls import reverse
from datetime import timedelta
from django.utils import timezone
from django.urls import reverse_lazy
from .models import Post, Comment, PostImage, PostVideo
from django.shortcuts import redirect

from .models import PostCommentInventory,StoryMedia, Story
from .forms import CommentForm, PostForm, ImageForm, VideoForm, StoryForm
from django.http import HttpResponseNotAllowed
from django.views.generic.edit import FormMixin
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView



@method_decorator(login_required(login_url='login'), name='dispatch')
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post-create.html'
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()

        media_files = request.FILES.getlist('media')
        image_files = [f for f in media_files if f.content_type.startswith('image/')]
        video_files = [f for f in media_files if f.content_type == 'video/mp4']

        image_form = ImageForm()
        video_form = VideoForm()

        image_errors = image_form.validate_photos(image_files)
        video_errors = video_form.validate_videos(video_files)

        if form.is_valid() and not image_errors and not video_errors:
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            for image in image_files:
                PostImage.objects.create(post=post, photo=image)

            for video in video_files:
                PostVideo.objects.create(post=post, video=video)

            return redirect(self.success_url)

        context = self.get_context_data(form=form)
        context['media_errors'] = image_errors + video_errors
        return self.render_to_response(context)





class PostDetail(DetailView):
    model = Post
    template_name = 'post-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()  # pega o Post atual pelo ID da URL

        # acessando imagens e vídeos
        context['imagens'] = post.images.all()  # retorna QuerySet de PostImagem
        context['videos'] = post.videos.all()    # retorna QuerySet de PostVideo
        

        context['total_media'] = post.images.count() + post.videos.count()
       

        return context

class PostUpdate(UpdateView):
    model = Post
    fields = ['text' ]
    template_name ='post-update.html'
    context_object_name = 'post_update'


    def get_success_url(self):
        # Redireciona para a página de detalhes do post atualizado
        return reverse('post-detail', kwargs={'pk': self.object.pk})

class PostDelete(DeleteView):
    model = Post 
    template_name = 'post-delete.html'
    success_url = reverse_lazy('my_perfil')

class HomeView(FormMixin, ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    form_class = CommentForm
    success_url = reverse_lazy('home')
    ordering = ['-created_at'] 


    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        
        context['stories'] = Story.objects.all()
    
        if self.request.user.is_authenticated:
            inventory = PostCommentInventory.objects.get_or_create(author=self.request.user)
            context['mostrar_inventory'] = True
            context['inventory_post'] = inventory
        else:
            pass
        
        # Post do coach fixado (pined=True)
        context['imagens'] = PostImage.objects.all()  # <-- ESSENCIAL
        context['videos'] = PostVideo.objects.all()
        posts  = context['posts']
        
        pinned = WOD.objects.filter(pinned=True).last()
        
        context['pinned'] = pinned
        if pinned:
            
            context['coach_profile'] =  pinned
            
           
        for post in posts:
            imagens = [img.photo.url for img in post.images.all() if img.photo]
            videos = [vid.video.url for vid in post.videos.all() if vid.video]
            post.media_dict = {
                'imagens': imagens,
                'videos': videos,
            }
            
        
       

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
    posts = user.post_set.all().order_by('-created_at')
    
    comments = request.user.comment_set.all().order_by('-created_at')
    
    pr = user.profilepersonalrecord_set.all()
   
    for post in posts:
            imagens = [img.photo.url for img in post.images.all() if img.photo]
            videos = [vid.video.url for vid in post.videos.all() if vid.video]
            post.media_dict = {
                'imagens': imagens,
                'videos': videos,
            }


    inventory_post = PostCommentInventory.objects.filter(author=user).first()
    return render(request, 'my_perfil.html', {'user': request.user, 'posts': posts, 'comments':comments, 'inventory_post': inventory_post, 'mostrar_inventory':True, 'pr':pr})

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
         









class StoryCreateView(CreateView):
    model  = StoryMedia
    form_class =  StoryForm
    template_name = 'story_create.html'
    success_url=  reverse_lazy('home')


 
    

    def post(self,request):
        form  = StoryForm( request.POST, request.FILES)
        
        if form.is_valid():
            print("POST recebido")
            story = Story.objects.create(user=request.user, expires_at=timezone.now() + timedelta(days=1))
            
            objeto =  form.save(commit=False)
            objeto.story = story
            
            objeto.save()

            return redirect('home')
        else:
            print(f'erro no formulario  de post para storie{form.errors}')
           
        return render(request, 'story_create.html',{'form':form})
  

class StoryDetailView(DetailView):
    model = Story
    template_name = 'story_detail.html'
    context_object_name = 'story'


