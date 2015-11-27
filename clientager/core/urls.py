from django.conf.urls import patterns, include, url

urlpatterns = patterns('clientager.core.views',
    url(r'^$', 'home', name='home'),
)