# Generated by Django 2.2.6 on 2019-11-28 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20191125_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tanggapan',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]