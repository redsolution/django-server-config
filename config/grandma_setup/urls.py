# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'config.grandma_setup.views.index', name='config_index'),
)
