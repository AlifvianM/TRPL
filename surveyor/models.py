from django.db import models
from blog import models as blog_models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Surveyor(models.Model):
	KERUSAKAN = (
			('Parah', 'parah'),
			('Sedang', 'sedang'),
			('Ringan', 'ringan')
		)

	LALU_LINTAS = (
			('Padat', 'padat'),
			('Sedang', 'sedang'),
			('Sepi', 'sepi')
		)

	judul 		= models.CharField(max_length=255)
	waktu_post	= models.DateTimeField(auto_now=True)
	# WaktuPost 	= models.ForeignKey(blog_models.WaktuPost, on_delete=models.CASCADE)
	kerusakan	= models.CharField(max_length=255, choices=KERUSAKAN, default='Ringan')
	lalu_lintas	= models.CharField(max_length=255, choices=LALU_LINTAS, default='Sepi')
	deskripsi	= models.TextField(default=None)
	# anggaran	= models.DecimalField(max_digits=9, decimal_places=2)
	alamat 		= models.ForeignKey(blog_models.Alamat, on_delete=models.CASCADE)
	penulisSurvey= models.ForeignKey(User, on_delete=models.CASCADE, default=True)
	# post 		= models.ForeignKey('Post', on_delete=models.CASCADE, default=None)

	def __str__(self):
		return self.judul

	def save(self):
		super().save()

	def get_absolute_url(self):
		return reverse('surveyor-detail', kwargs = {'pk':self.pk})