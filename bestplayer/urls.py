from django.conf.urls import url,patterns
from bestplayer import views
urlpatterns = patterns("",
             url(r'^$', views.IndexView.as_view(), name='index'),
             url(r'^(?P<pk>\d+)/$',views.DetailView.as_view(),name = 'detail'),
             url(r'^(?P<pk>\d+)/result/$',views.ResultView.as_view(),name = 'result'),
             url(r'^(?P<club_id>\d+)/vote/$',views.vote,name = 'vote'),
             )