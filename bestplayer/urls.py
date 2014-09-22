from django.conf.urls import url,patterns
from bestplayer import views
urlpatterns = patterns("",
             url(r'^$', views.index, name='index'),
             url(r'^(?P<club_id>\d+)/$',views.detail,name = 'detail'),
             url(r'^(?P<club_id>\d+)/result/$',views.result,name = 'result'),
             url(r'^(?P<club_id>\d+)/vote/$',views.vote,name = 'vote'),
             )