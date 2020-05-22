from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [
    path('blog', PostListView.as_view(), name='blog-home'),
    path('blog/user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('blog/post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('blog/post/new/', PostCreateView.as_view(), name='post-create'),
    path('blog/post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('blog/post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('blog/about/', views.about, name='blog-about'),
]