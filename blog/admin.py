from django.contrib import admin
from .models import (
	Post, 
	# Surveyor, 
	Alamat, 
	Status, 
	Kategori,
	WaktuPost
	)
from material.admin.decorators import register
from material.admin.options import MaterialModelAdmin
from material.admin.sites import site
# Register your models here.

# class PostAdmin(admin.ModelAdmin):
# 	readonly_fields =[
# 			'judul',
# 			'isi',
# 			'alamat',
# 			'kategori',
# 			# 'waktu_post',
# 			# 'waktu_update',
# 			'foto',
# 			'penulis',
# 		]

# 	list_display = ('judul', 'waktu_post',)
# 	list_filter = ('waktu_post',)
		


@register(Post)
class PostMaterialAdmin(MaterialModelAdmin):
	list_display = ('judul', 'waktu_post',)


site.register(Alamat)
site.register(Kategori)
site.register(Status)
site.register(WaktuPost)





# admin.site.register(Post, PostAdmin)
# admin.site.register(Surveyor)
# admin.site.register(Alamat)
# admin.site.register(Status)
# admin.site.register(Kategori)
# admin.site.register(WaktuPost)