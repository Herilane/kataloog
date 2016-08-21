from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.avaleht, name='avaleht'),
	url(r'^lisaosanik/(?P<pk>\d+)/$', views.lisaosanik, name='lisaosanik'),
	url(r'^asutamine/$', views.asutamine, name='asutamine'),
	url(r'^nimekiri/$', views.nimekiri, name='nimekiri'),
	url(r'^andmed/(?P<pk>\d+)/$', views.andmed, name='andmed'),
]