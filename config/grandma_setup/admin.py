from django.contrib import admin
from grandma.admin import GrandmaBaseAdmin
from config.grandma_setup.models import ConfigSettings, ConfigSite, ConfigRedirect

class ConfigSiteInline(admin.TabularInline):
    model = ConfigSite

class ConfigRedirectInline(admin.TabularInline):
    model = ConfigRedirect

class ConfigSettingsAdmin(GrandmaBaseAdmin):
    model = ConfigSettings
    inlines = [ConfigSiteInline, ConfigRedirectInline]
