# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = '''Usage manage.py make_config [template]
    Make specified config file.
    
Available templates:
    init.d
    lighttpd
    logrotate
    monit
    httpd
'''

    def handle(self, *args, **options):
        if not args or len(args) > 1:
            print self.help
        else:
            template = 'config/%s.conf' % args[0]
            from config.utils import make_config
            print make_config(template)
