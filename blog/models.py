from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):

	STATUS = (
			('Belum Di Survey', 'belum_di_survey'),
			('Sedang Di Survey', 'sedang_di_survey'),
			('Telah Di Survey', 'telah_di_survey'),
			('Dalam Proses Pengerjaan','dalam_proses_pengerjaan'),
			('Telah Di Perbaiki', 'telah_di_perbaiki') 
		)

	judul		= models.CharField(max_length=255)
	isi 		= models.TextField()
	# kategori 	= models.CharField(max_length=255, choices=KATEGORI)
	kategori 	= models.ForeignKey('Kategori', on_delete=models.CASCADE)
	# WaktuPost 	= models.ForeignKey('WaktuPost', on_delete=models.CASCADE, default=timezone.now)
	waktu_post	= models.DateTimeField(default=timezone.now)
	waktu_update= models.DateTimeField(auto_now=True)
	foto 		= models.ImageField(default='blank.jpg', upload_to='pengaduan', null=True, blank=True)
	# status 		= models.CharField(max_length=255, choices=STATUS, default='Belum Di Survey')
	status_id	= models.ForeignKey('Status', on_delete=models.CASCADE,default='1')
	alamat 		= models.ForeignKey('Alamat', on_delete=models.CASCADE)
	tanggapan 	= models.CharField(max_length=50, null=True, blank=True)
	penulis		= models.ForeignKey(User, on_delete = models.CASCADE)
	# surveyor 	= models.ForeignKey('Surveyor', on_delete=models.CASCADE, default=None)

	def __str__(self):
		return self.judul
		

	def save(self):
		super().save()

	def get_absolute_url(self):
		return reverse('post-detail', kwargs = {'pk':self.pk})


class Kategori(models.Model):
	KATEGORI = (
			('Jalan', 'jalan'),
			('Jembatan', 'jembatan'),
			('Lampu Jalan', 'lampu_jalan'),
	)
	kategori 	= models.CharField(max_length=255, choices=KATEGORI)

	def __str__(self):
		return self.kategori



class Alamat(models.Model):
	ALAMAT_JALAN=(
			('Pilih Alamat', '------'),
			('Kalimantan', 'kalimantan'),
			('Gajah Mada', 'gajah_mada'),
			('Jawa', 'jawa'),
			('Sumatra', 'sumatra'),
			('Karimata', 'karimata'),
			('Semeru', 'semeru'),
			('Bangka', 'bangka'),
			('Halmahera', 'halmahera')
		)
	alamat 		= models.CharField(max_length=255, choices=ALAMAT_JALAN, default='Pilih Alamat', null=True)
	# alamat 		= models.CharField(max_length=255, default='Pilih Alamat')


	def __str__(self):
		return self.alamat


class Status(models.Model):
	STATUS = (
			('Belum Di Survey', 'belum_di_survey'),
			('Sedang Di Survey', 'sedang_di_survey'),
			('Telah Di Survey', 'telah_di_survey'),
			('Dalam Proses Pengerjaan','dalam_proses_pengerjaan'),
			('Telah Di Perbaiki', 'telah_di_perbaiki') 
		)	
	status = models.CharField(max_length=255, choices=STATUS)

	def __str__(self):
		return self.status


class WaktuPost(models.Model):
	waktu_post 		= models.DateTimeField(auto_now_add=True)
	waktu_update	= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.id


