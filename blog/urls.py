from django.urls import path, include
from .views import PostMyView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views
# from rest_framework import routers
from django.views.generic import TemplateView

# router = routers.DefaultRouter()
# router.register(r'post', views.PostViewSet)

urlpatterns = [
    path('', TemplateView.as_view(template_name = 'blog/index-two.html'), name = 'blog-index'),
	path('post/', PostListView.as_view(), name = 'blog-home'),
	path('post/post-saya/', views.UserPost, name = 'blog-post_saya'),
	# path('post/post-saya/', PostMyView.as_view(), name = 'blog-post_saya'),
	path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
	path('post/new/', PostCreateView.as_view(), name = 'post-create'),
	path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update'),
	path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete'),
    path('about/', views.about, name='blog-about'),

    # path('api/', include(router.urls)),
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]