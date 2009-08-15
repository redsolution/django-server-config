from django.conf import settings
from django.conf.urls.defaults import *

from config.settings import media_url, media_paths

urlpatterns = patterns('django.views.static', *[
    ('^%s%s(?P<path>.*)$' % (media_url[1:], url[1:]), 'serve', {
        'document_root': path} )
    for url, path in media_paths ] )
