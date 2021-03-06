"""First URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import users_view, groups_view, home 

urlpatterns = [
    path('admin/', admin.site.urls),
     path('summernote/', include('django_summernote.urls')),
    path('savollar/', include('poll.urls', namespace='poll')),    
    path('more/', include('extra.urls', namespace='extra')),    
    path('accounts/', include('userprofile.urls', namespace='userprofile')),
    path('news/', include('new.urls', namespace='new')),
    path('about/', groups_view, name="groups"),
    # path('update-user/<int:pk>', update_view, name="user_update"),
    path('users', users_view, name="users"),
    path('', home, name="home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
