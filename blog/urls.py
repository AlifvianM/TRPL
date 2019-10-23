from django.urls import path
from .views import PostMyView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
	path('', PostListView.as_view(), name = 'blog-home'),
	path('post/post-saya/', views.UserPost, name = 'blog-post_saya'),
	# path('post/post-saya/', PostMyView.as_view(), name = 'blog-post_saya'),
	path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
	path('post/new/', PostCreateView.as_view(), name = 'post-create'),
	path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update'),
	path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete'),
    path('about/', views.about, name='blog-about'),
]