# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('like_post/<int:post_id>/', views.like_post, name='like_post'),
    path('list/', views.get_posts, name='get_posts'),

]