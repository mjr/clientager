from django.conf.urls import patterns, include, url

urlpatterns = patterns('clientager.manager.views',
    url(r'^$', 'subscribe', name='subscribe'),
    url(r'^(\d+)/$', 'detail', name='detail'),
)
