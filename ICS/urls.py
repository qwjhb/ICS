"""ICS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
import login.urls
import login.views
import client.urls
import survey.views
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', login.views.index, name='index'),
    url(r'^register$',login.views.register,name='register'),
    url(r'^portal$', login.views.portal,name='portal'),
    url(r'^logout$', login.views.userlogout,name='userlogout'),
    url(r'^accounts/login/', survey.views.error,name='error'),
    url(r'client/',include('client.urls')),
    url(r'survey/',include('survey.urls'))

]
