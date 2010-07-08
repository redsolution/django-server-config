import os
from django.template.loader import render_to_string

from grandma.make import BaseMake
from grandma.models import GrandmaSettings
from config.grandma_setup.models import ConfigSettings

class Make(BaseMake):
    def make(self):
        config_settings = ConfigSettings.objects.get_settings()
        data = render_to_string('config/grandma/settings.py', {
            'config_settings': config_settings,
        })
        grandma_settings = GrandmaSettings.objects.get_settings()
        grandma_settings.append_to('settings.py', data)
        data = render_to_string('config/grandma/urls.py', {
        })
        grandma_settings = GrandmaSettings.objects.get_settings()
        grandma_settings.append_to('urls.py', data)
        data = render_to_string('grandma/buildout.cfg', {
        })
        grandma_settings.append_to(os.path.join('..', 'buildout.cfg'), data)
        data = render_to_string('grandma/develop.cfg', {
        })
        grandma_settings.append_to(os.path.join('..', 'develop.cfg'), data)
