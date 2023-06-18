from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="home" ),
    path('posts/<int:post_id>/post_detail', views.post_detail, name='post_detail')
]