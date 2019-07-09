#  Copyright (c) 2018 - Amith K K
#  Released under the GNU GPLv3 License
#

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
from minerva_event.views import mass_attendance

app_name = 'minerva_core'


if hasattr(settings, 'ADMIN_SITE_HEADER'):
    admin.site.site_header = settings.ADMIN_SITE_HEADER
    admin.site.site_title = settings.ADMIN_SITE_HEADER

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)
logout_redir = RedirectView.as_view(url='/login')
urlpatterns = [
    path(r'minerva_event/massattendanceproxy/', mass_attendance ),
    path(r'accounts/login/', logout_redir),
    path('accounts/resetpwd', PasswordResetView.as_view(), name="reset_password"),
    path('', admin.site.urls),
    path('accounts/', include('authtools.urls')),
    path('jet/', include('jet.urls', 'jet')),
    path('favicon\.ico', favicon_view),
    path('auth_as_student', views.student_login, name= "student_login")]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + staticfiles_urlpatterns()
