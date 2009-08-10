from django.conf import settings
from django.conf.urls.defaults import *

from config.settings import media_url, app_media_paths

urlpatterns = patterns('django.views.static', *[
    ('^%s%s(?P<path>.*)$' % (media_url[1:], url), 'serve', {
        'document_root': path} )
    for url, path in app_media_paths ] )
