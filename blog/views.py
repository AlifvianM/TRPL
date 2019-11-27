from django.shortcuts import render
from .models import Post
from surveyor.models import Surveyor
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializers import PostSerializer
# Create your views here.

def home(request):
	context = {
		'posts':Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = ['-waktu_update']

	# def get_context_data(self, **kwargs):
	# 	context = super(LaundryListModel, self).get_context_data(**kwargs)
	# 	context.update(
	# 			{
	# 				'total_harga_laundry':Laundry.objects.annotate(Sum('harga'))
	# 			}
	# 		)
	# 	print(Laundry.objects.annotate(total_income=Sum('harga')))
	# 	return context 

	def get_context_data(self, **kwargs):
	    context = super(PostListView, self).get_context_data(**kwargs)
	    context.update(
	    		{
	    			'surveyor':Surveyor.objects.all().order_by('-waktu_post')
	    		}
	    	)
	    return context


@login_required
def UserPost(request):
	user_post = Post.objects.filter(penulis = request.user).order_by('-waktu_update')
	template = 'blog/my_post.html'
	return render(request, template, {
				'user_post':user_post
			}
		)

class PostMyView(LoginRequiredMixin, ListView):
	model = Post
	paginate_by = 10
	template_name = 'blog/my_post.html'
	# queryset = Post.objects.filter(penulis)

	def get_queryset(self):
		my_post = Post.objects.filter(penulis = self.user)
		return super().get_queryset()

	# def get_queryset(self):
	# 	posts = []
	# 	for user in self.request.user.post.all():
	# 		for post in Post.objects.filter(penulis = user):
	# 			posts.append(post)
	# 	return posts

class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['judul', 'isi','foto', 'alamat', 'kategori']
		
	def form_valid(self, form):
		form.instance.penulis = self.request.user
		return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['judul', 'isi','foto']
		
	def form_valid(self, form):
		form.instance.penulis = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.pemesan:
			return True
		return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'


	def test_func(self):
		post = self.get_object()
		if self.request.user == post.penulis:
			return True
		return False

def about(request):
	return render(request, 'blog/about.html')


class PostViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.all().order_by('-waktu_update')
	serializer_class = PostSerializer









