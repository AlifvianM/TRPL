# Generated by Django 2.2.6 on 2019-11-25 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191125_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='status',
            field=models.CharField(choices=[('Belum Di Survey', 'belum_di_survey'), ('Sedang Di Survey', 'sedang_di_survey'), ('Telah Di Survey', 'telah_di_survey'), ('Dalam Proses Pengerjaan', 'dalam_proses_pengerjaan'), ('Telah Di Perbaiki', 'telah_di_perbaiki')], max_length=255),
        ),
    ]
