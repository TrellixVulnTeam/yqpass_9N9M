"""yuanqu2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from main import views as main_views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^main/', include('main.urls')),
    url(r'^accounts/', include('users.urls')),
    url(r'^accounts/profile/$', main_views.accounts_profile, name='accounts_profile'),
    url(r'^accounts/profile/change/$', main_views.accounts_change, name='accounts_change'),
    url(r'^$', login, {'template_name': 'users/login.html'}),
]
