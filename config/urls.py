from django.conf import settings
from django.conf.urls.defaults import *

from config.settings import app_media_paths

urlpatterns = patterns('django.views.static', *[
    ('^%s(?P<path>.*)$' % url[1:], 'serve', {
        'document_root': path} )
    for url, path in app_media_paths ] )
