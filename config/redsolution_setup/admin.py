from django.contrib import admin
from redsolutioncms.admin import CMSBaseAdmin
from config.redsolution_setup.models import ConfigSettings, ConfigSite, ConfigRedirect

class ConfigSiteInline(admin.TabularInline):
    model = ConfigSite

class ConfigRedirectInline(admin.TabularInline):
    model = ConfigRedirect

class ConfigSettingsAdmin(CMSBaseAdmin):
    model = ConfigSettings
    inlines = [ConfigSiteInline, ConfigRedirectInline]
