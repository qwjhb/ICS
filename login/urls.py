from django.conf.urls import patterns,url
from login import views
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^test/$', views.register, name='test'),# ADD NEW PATTERN!
    )

