import os
from grandma.make import BaseMake
from grandma.models import GrandmaSettings
from config.grandma_setup.models import ConfigSettings

class Make(BaseMake):
    def make(self):
        super(Make, self).make()
        config_settings = ConfigSettings.objects.get_settings()
        grandma_settings = GrandmaSettings.objects.get_settings()
        grandma_settings.render_to('settings.py', 'config/grandma/settings.py', {
            'config_settings': config_settings,
        })
        grandma_settings.render_to('urls.py', 'config/grandma/urls.py', {
            'config_settings': config_settings,
        })
        grandma_settings.render_to(os.path.join('..', 'buildout.cfg'), 'config/grandma/buildout.cfg', {
            'config_settings': config_settings,
        })
        grandma_settings.render_to(os.path.join('..', 'develop.cfg'), 'config/grandma/develop.cfg', {
            'config_settings': config_settings,
        })
