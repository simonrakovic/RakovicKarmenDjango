from django.conf.urls import patterns, include, url

from django.contrib import admin

from rkWebApp import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rkspletna.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.home, name='home'),
    url(r'^podjetje/', views.podjetje, name='home'),
    url(r'^storitve/', views.storitve, name='home'),
    url(r'^povprasevanje/', views.povprasevanje, name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
