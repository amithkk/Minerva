"""Minerva URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
import authtools
import jet
from authtools.views import PasswordResetView
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.views.generic import RedirectView

from Minerva import settings
from minerva_core import views

app_name = 'minerva_core'


if hasattr(settings, 'ADMIN_SITE_HEADER'):
    admin.site.site_header = settings.ADMIN_SITE_HEADER
    admin.site.site_title = settings.ADMIN_SITE_HEADER

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)
logout_redir = RedirectView.as_view(url='/login', permanent=True)
urlpatterns = [
    path(r'logout/', logout_redir),
    path(r'accounts/login/', logout_redir),
    path('accounts/resetpwd', PasswordResetView.as_view(), name="reset_password"),
    path('', admin.site.urls),
    path('accounts/', include('authtools.urls')),
    path('jet/', include('jet.urls', 'jet')),
    path('favicon\.ico', favicon_view),
    path('auth_as_student', views.student_login, name= "student_login")]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + staticfiles_urlpatterns()
