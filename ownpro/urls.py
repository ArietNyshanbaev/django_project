from django.conf.urls import patterns, include, url
from django.contrib import admin
from bestplayer import urls
from signups import urls
admin.autodiscover()

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:
    url(r"^bestplayer/",include('bestplayer.urls',namespace = "bestplayer")),
    
    url(r'^signups/', include('signups.urls',namespace = 'signups')),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG :
    urlpatterns += static(settings.STATIC_URL,
                          document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root = settings.MEDIA_ROOT)