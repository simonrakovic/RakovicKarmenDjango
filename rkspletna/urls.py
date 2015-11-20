from django.conf.urls import patterns, include, url

from django.contrib import admin

from rkWebApp import views
from rkspletna.settings import MEDIA_ROOT

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rkspletna.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.home, name='home'),
    # url(r'^podjetje/', views.podjetje, name='home'),
    url(r'^storitve/', views.storitve, name='home'),
    url(r'^povprasevanje/', views.povprasevanje, name='home'),
    url(r'^kontakti/', views.kontakti, name='home'),
    url(r'^novice/', views.novice, name='home'),
    url(r'^novica/(?P<id>\d+)/$', views.novica, name='home'),
    url(r'^admin/', include(admin.site.urls)),

    # url(r'^media/(.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
)
