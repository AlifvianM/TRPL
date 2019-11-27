from django.urls import path
from .views import (
	SurveyorListView,
	SurveyorCreateView,
	SurveyorDetailView,
	SurveyList,
	)
from . import views

urlpatterns = [
	path('detail/<int:pk>/',SurveyorDetailView.as_view(), name = 'surveyor-detail'),
	path('new/', SurveyorCreateView.as_view(), name = 'surveyor-create'),
	path('',SurveyorListView.as_view(), name = 'surveyor-list'),
]