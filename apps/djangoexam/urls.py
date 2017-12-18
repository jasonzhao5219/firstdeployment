from django.conf.urls import url
from . import views          
urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^login$',views.login),
    url(r'^show$',views.show),
    url(r'^Add$',views.add),
    url(r'^addsuc$',views.addsuc),
    url(r'^destination/(?P<number>\d+)$', views.destination),
    url(r'^dsuc$',views.dsuc),
    url(r'^logout$',views.logout),
    url(r'^join/(?P<number>\d+)$',views.join),
    #url(r'^addprocess$',views.addprocess),
    url(r'^add$',views.add),
]