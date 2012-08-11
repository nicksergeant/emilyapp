from django.conf.urls.defaults import include, patterns, url
from django.contrib import admin
from emilyapp.views import home


admin.autodiscover()
urlpatterns = patterns('',
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', home, name='home'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login',),
    url(r'^events', include('events.urls')),
)
