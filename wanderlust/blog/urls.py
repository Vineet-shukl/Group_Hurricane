
from django.urls import path
from .views import list_posts, create_post, home, post_update, post_delete, register, post_detail, custom_logout

urlpatterns = [
    path('', home, name='home'),
    path('post/<int:pk>/edit/', post_update, name='post_update'),
    path('post/<int:pk>/delete/', post_delete, name='post_delete'),
    path('register/', register, name='register'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('create/', create_post, name='create_post'),
    path('logout/', custom_logout, name='custom_logout'),
]
