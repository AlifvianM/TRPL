"""TRPL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views

from django.contrib.staticfiles.templatetags.staticfiles import static as staticfiles
# from django.urls import path, include
from django.utils.translation import ugettext_lazy as _

from material.admin.sites import site


# optional
###################################################
site.site_header = _('JemberINF Administrations')
# site.site_title = _('Your site title')
# site.favicon = staticfiles('path/to/favicon')
# site.main_bg_color = 'green'
# site.main_hover_color = 'yellow'
# site.profile_picture = staticfiles('path/to/image')
# site.profile_bg = staticfiles('path/to/image')
# site.login_logo = staticfiles('path/to/image')
# site.logout_bg = staticfiles('path/to/image')
###################################################

urlpatterns = [
    path('admin/', include('material.admin.urls')),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name='logout'),
    path('surveyor/', include('surveyor.urls')),
	path('',include('blog.urls')),
]


if settings.DEBUG:
	urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)