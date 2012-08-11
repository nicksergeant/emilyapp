from django.conf.urls.defaults import patterns, url
from events import views


urlpatterns = patterns('',
    url(r'add/(?P<type>[^/]+)/$', views.add, name='events-add'),
    url(r'(?P<id>\d+)/delete/$', views.delete, name='events-delete'),
)
