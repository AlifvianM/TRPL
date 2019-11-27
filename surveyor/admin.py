from django.contrib import admin
from .models import Surveyor
# Register your models here.

from material.admin.decorators import register
from material.admin.options import MaterialModelAdmin
from material.admin.sites import site


site.register(Surveyor)

# admin.site.register(Surveyor)