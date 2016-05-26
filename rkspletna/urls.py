from django.conf.urls import patterns, include, url

from django.contrib import admin

from rkWebApp import views
from rkspletna.settings import MEDIA_ROOT
from django.contrib.sitemaps.views import sitemap
from sitemap import StaticSitemap

admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rkspletna.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.home, name='home'),
    # url(r'^podjetje/', views.podjetje, name='home'),
    url(r'^storitve/', views.storitve, name='home'),
    url(r'^povprasevanje/', views.povprasevanje, name='povprasevanje'),
    url(r'^kontakti/', views.kontakti, name='kontakti'),
    url(r'^novice/', views.novice, name='novice'),
    url(r'^novica/(?P<id>\d+)/$', views.novica),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^media/(.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
)

sitemaps = {
    'static': StaticSitemap()
}

urlpatterns += patterns('',
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
)