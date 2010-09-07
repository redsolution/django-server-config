# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url
from config.redsolution_setup.admin import ConfigSettingsAdmin
admin_instance = ConfigSettingsAdmin()

urlpatterns = patterns('',
    url(r'^$', admin_instance.change_view, name='config_index'),
)
