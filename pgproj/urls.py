"""pgproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from pgapp import views
from django.conf import settings
from django.views.static import serve
from django.urls import re_path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),  # Route to the Django admin site
    path('home/', views.home, name='home'),  # Route to the 'home' view from pgapp.views
    path('mysave/', views.mysave, name='mysave'),  # Route to the 'home' view from pgapp.views
    path('index/',views.index,name='index'),
    path('pg_register/',views.pg_register,name='pg_register'),
    path('PG_Register_DataSaving/',views.PG_Register_DataSaving,name='PG_Register_DataSaving'),
    path('',views.login,name='login'),
    path('index1/',views.index1,name='index1'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)