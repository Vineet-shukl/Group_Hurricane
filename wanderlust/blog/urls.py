
from django.urls import path
from .views import blog_index, get_post,create_post,content_post,home,post_update,post_delete,register, post_detail,custom_logout

urlpatterns = [
    path('',home, name='home'),
    path('posts/new_post',content_post,name='content_post'),
    path('post/<int:pk>/edit/',post_update, name='post_update'),
    path('post/<int:pk>/delete/',post_delete, name='post_delete'),
    path('register/',register, name='register'),
    path('post/<int:pk>/',post_detail, name='post_detail'),
    path('create/', content_post, name='create_post'),
    path('logout/',custom_logout , name='custom_logout'),
   ]
