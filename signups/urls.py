from django.conf.urls import url,patterns,include
import views

urlpatterns = patterns('',
    url(r'^$',views.home,name = 'home'),
    url(r'^thank-you/$',views.thankyou,name = 'thank-you'),
    )

