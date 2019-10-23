# Generated by Django 2.2.3 on 2019-10-18 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20191018_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='NIK',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='default_profile.jpg', null=True, upload_to='profile_pics'),
        ),
    ]
