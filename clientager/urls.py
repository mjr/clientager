from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^inscricao/', include('clientager.manager.urls', namespace='subscriptions')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('clientager.core.urls', namespace='core')),
]
