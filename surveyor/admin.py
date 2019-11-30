from django.contrib import admin
from .models import Surveyor
# Register your models here.

from material.admin.decorators import register
from material.admin.options import MaterialModelAdmin
from material.admin.sites import site



@register(Surveyor)
class SurveyorMaterialAdmin(MaterialModelAdmin):
	list_display = ('judul', 'waktu_post', 'kerusakan')
	list_filter = ('judul', 'waktu_post', 'kerusakan')
# admin.site.register(Surveyor)