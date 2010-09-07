# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from redsolutioncms.models import BaseSettings, CMSSettings

class ConfigSettingsManager(models.Manager):
    def get_settings(self):
        if self.get_query_set().count():
            return self.get_query_set()[0]
        else:
            cms_settings = CMSSettings.objects.get_settings()
            config_settings = self.get_query_set().create()
            ConfigSite.objects.create(settings=config_settings, site='www.%s.com' % cms_settings.project_name)
            ConfigRedirect.objects.create(settings=config_settings, site='%s.com' % cms_settings.project_name)
            return config_settings

class ConfigSettings(BaseSettings):
    objects = ConfigSettingsManager()

class ConfigSite(models.Model):
    settings = models.ForeignKey(ConfigSettings, related_name='sites')
    site = models.CharField(verbose_name=_('site'), max_length=255)

class ConfigRedirect(models.Model):
    settings = models.ForeignKey(ConfigSettings, related_name='redirects')
    site = models.CharField(verbose_name=_('site'), max_length=255)

class ConfigAppMedia(models.Model):
    settings = models.ForeignKey(ConfigSettings, related_name='appmedia')
    appname = models.CharField(verbose_name=_('Application name'), max_length=255)
    source = models.CharField(verbose_name=_('Source dir'), max_length=255)
    target = models.CharField(verbose_name=_('target dir'), max_length=255)