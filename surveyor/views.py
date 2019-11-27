from django.shortcuts import render
from .models import Surveyor
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.decorators import login_required
# from rest_framework import viewsets
# from .serializers import PostSerializer
# Create your views here.


class SurveyorListView(ListView):
	model = Surveyor
	context_object_name = 'posts'
	ordering = ['-waktu_post']





def SurveyList(request):
	surveyor = Surveyor.objects.all()
	template = 'surveyor/surveyor_list.html'
	context = {
		'surveyor':surveyor
	}
	return render(request, template, context)


class SurveyorCreateView(LoginRequiredMixin,CreateView):
	model = Surveyor
	fields = [
		'judul',
		'kerusakan',
		'lalu_lintas',
		'deskripsi',
		# 'anggaran',
		'alamat',

	]

	def form_valid(self, form):
		form.instance.penulisSurvey = self.request.user
		return super().form_valid(form)


class SurveyorDetailView(DetailView):
	model = Surveyor



