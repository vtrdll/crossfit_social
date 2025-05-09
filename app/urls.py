"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from Social.views import my_profile, HomeView
from account.views import PhotoUpdate, PhotoDelete
from account.views import register_view, login_view, logout_view
from Social.views import CommentList, CommentUpdate, CommentDelete
from Social.views import PostCreateView, PostDetail, PostUpdate, PostDelete
from account.views import  UserDetail, UserUpdate, UserDelete, PasswordUpdate, ProfileDetail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register' ),
    path('login/', login_view, name='login' ),
    path('logout/', logout_view, name='logout' ),
    
    
    path('post/', PostCreateView.as_view(), name='post-create' ),
    path('perfil/<int:pk>/', ProfileDetail.as_view(), name='user-public-profile'),
    
    path('post/<int:pk>/editar/', PostUpdate.as_view(), name='post-edit'),
    path('post/<int:pk>/delete/', PostDelete.as_view(), name='post-delete'),
    path('post/<int:pk>/detail/', PostDetail.as_view(), name='post-detail'),

    path('post/<int:pk>/comment/', CommentList.as_view(), name='comment-list'),
    path('comment/<int:pk>/edit/', CommentUpdate.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDelete.as_view(),  name='comment-delete'),


    path('user/<int:pk>/editar/', UserUpdate.as_view(), name='user-update'),
    path('user/<int:pk>/detail/', UserDetail.as_view(), name='user-detail'),
   
    path('user/<int:pk>/delete/', UserDelete.as_view(), name ='user-delete'),
    path('password/<int:pk>/editar/', PasswordUpdate.as_view(), name='password-change'),

    path('photo/<int:pk>/delete/', PhotoDelete.as_view(), name='photo-delete'),
    path('photo/<int:pk>/update/', PhotoUpdate.as_view(), name='photo-update'),
    path('', HomeView.as_view(), name='home'),
    path('my-perfil/', my_profile, name='my-perfil'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
