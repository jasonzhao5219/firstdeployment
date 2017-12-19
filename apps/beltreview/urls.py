from django.conf.urls import url
from . import views          
urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^login$',views.login),
    url(r'^showbook$',views.showbook),
    url(r'^showbook/add$',views.addbook),
    url(r'^bookreviewcreate$',views.bookreviewcreate),
    url(r'^showone/(?P<number>\d+)$',views.showone),
    url(r'^showonesuc$',views.showonesuc),

    #url(r'^suc$',views.suc)
    #url(r'^(?P<number>\d+)/destroy$',views.destroy)
]