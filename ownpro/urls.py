from django.conf.urls import patterns, include, url
from django.contrib import admin
from bestplayer import urls
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r"^bestplayer/",include('bestplayer.urls',namespace = "bestplayer")),
    
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
