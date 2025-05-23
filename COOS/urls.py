"""
URL configuration for COOS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from users.views import * 
from user_staff.views import *
from user_admin.views import *
from categories.views import *
from menuitems.views import *
from tables.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('register-staff/', register_staff, name = "register_staff"),
    path('login/', login_user, name = "login"),
    path('logout/', logout_view, name = "logout"),

    path('staff-dashboard/', staff_dashboard, name="staff_dasboard" ),
    path('admin-dashboard/', admin_dashboard, name="admin_dashboard" ),
    path('categories/', include('categories.urls')),
    path('menuitems/', include('menuitems.urls')),
    path('tables/', include('tables.urls')),
    path('website/', include('website.urls')),




]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()