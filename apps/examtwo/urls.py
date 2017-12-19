from django.conf.urls import url
from . import views          
urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^show$', views.show),
    url(r'^addquote$', views.addquote),
    url(r'^addfavorite/(?P<number>\d+)$', views.addfavorite),
    url(r'^removefavorite/(?P<number>\d+)$', views.removefavorite),
    url(r'^users/(?P<number>\d+)$', views.usersinfo),
    url(r'^dashboard$', views.dashboard),
    url(r'^logout$', views.logout),
     url(r'^login$', views.login),
    #url(r'^login$',views.login),
    
]