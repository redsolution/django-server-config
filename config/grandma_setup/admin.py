from django.contrib import admin
from config.grandma_setup.models import ConfigSettings, ConfigSite, ConfigRedirect

class ConfigSiteInline(admin.TabularInline):
    model = ConfigSite

class ConfigRedirectInline(admin.TabularInline):
    model = ConfigRedirect

class GrandmaApplicationForm(admin.ModelAdmin):
    model = ConfigSettings
    inlines = [ConfigSiteInline, ConfigRedirectInline]

try:
    admin.site.register(ConfigSettings, GrandmaApplicationForm)
except admin.sites.AlreadyRegistered:
    pass
