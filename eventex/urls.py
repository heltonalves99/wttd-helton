# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

from core.views import Home

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name='home'),

    url(r'^inscription/', include('apps.subscriptions.urls')),

    url(r'^admin/', include(admin.site.urls)),

)

urlpatterns += staticfiles_urlpatterns()
