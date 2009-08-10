import os
import sys

from django.conf import settings
from django.contrib import admin
from django.template.loader import render_to_string

def make_config(template_name):
    from config.settings import media_url, media_path, \
        admin_media_url, admin_media_path, app_media_paths, \
        project_name, project_file, project_url, project_redirects, project_auth
    return render_to_string(template_name, locals())

def make_path(path):
    if not path.endswith('/') and not path.endswith('\\'):
        path = os.path.join(path, '')
    return path

def make_url(url):
    if not url.startswith('/'):
        url = '/' + url
    if not url.endswith('/'):
        url = url + '/'
    return url

def get_app_media_paths(admin_media_url, admin_media_path):
    # At compile time, cache the directories to search.
    fs_encoding = sys.getfilesystemencoding() or sys.getdefaultencoding()
    app_media_paths = {}

    for app in settings.INSTALLED_APPS:
        i = app.rfind('.')
        if i == -1:
            m, a = app, None
        else:
            m, a = app[:i], app[i+1:]
        try:
            if a is None:
                mod = __import__(m, {}, {}, [])
            else:
                mod = getattr(__import__(m, {}, {}, [a]), a)
        except ImportError, e:
            raise ImproperlyConfigured, 'ImportError %s: %s' % (app, e.args[0])
        media_dir = os.path.join(os.path.dirname(mod.__file__), 'media')
        if mod == admin:
            continue
        if os.path.isdir(media_dir):
            for dir in os.listdir(media_dir):
                if dir == '.svn':
                    continue
                url = dir.decode(fs_encoding) + '/'
                if url not in app_media_paths:
                    app_media_paths[url] = os.path.join(media_dir, dir, '').decode(fs_encoding)
    
    # It won't change, so convert it to a tuple to save memory.
    app_media_paths = tuple( [ (url, path) for url, path in app_media_paths.iteritems() ] )
    return app_media_paths
