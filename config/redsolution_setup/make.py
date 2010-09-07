import os
from redsolutioncms.make import BaseMake
from redsolutioncms.models import CMSSettings
from config.redsolution_setup.models import ConfigSettings

class Make(BaseMake):
    def make(self):
        super(Make, self).make()
        config_settings = ConfigSettings.objects.get_settings()
        cms_settings = CMSSettings.objects.get_settings()
        cms_settings.render_to('settings.py', 'config/redsolutioncms/settings.pyt', {
            'config_settings': config_settings,
        })
        cms_settings.render_to('urls.py', 'config/redsolutioncms/urls.pyt', {
            'config_settings': config_settings,
        })
        cms_settings.render_to(os.path.join('..', 'buildout.cfg'), 'config/redsolutioncms/buildout.cfg', {
            'config_settings': config_settings,
        })
        cms_settings.render_to(os.path.join('..', 'develop.cfg'), 'config/redsolutioncms/develop.cfg', {
            'config_settings': config_settings,
        })

make = Make()