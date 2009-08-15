import os
import sys

from django.conf import settings
from django.contrib import admin
from django.template.loader import render_to_string

def make_config(template_name):
    from config.settings import media_url, media_path, \
        admin_media_url, admin_media_path, project_name, project_file, \
        media_paths, sites, redirects, need_auth, settings
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

def import_model(name):
    i = name.rfind('.')
    if i == -1:
        m, a = name, None
    else:
        m, a = name[:i], name[i+1:]
    try:
        if a is None:
            model = __import__(m, {}, {}, [])
        else:
            model = getattr(__import__(m, {}, {}, [a]), a)
    except ImportError, e:
        raise ImproperlyConfigured, 'ImportError %s: %s' % (name, e.args[0])
    return model


def get_media_paths():
    # At compile time, cache the directories to search.
    fs_encoding = sys.getfilesystemencoding() or sys.getdefaultencoding()
    paths = {}

    apps = {}
    for model, value in getattr(settings, 'CONFIG_APP_MEDIA', {}).iteritems():
        apps[import_model(model)] = value 

    for app in settings.INSTALLED_APPS:
        model = import_model(app)
        media_dir = os.path.join(os.path.dirname(model.__file__), 'media')
        media_dir_decoded = media_dir.decode(fs_encoding)
        if model == admin:
            # django provide support for admin`s urls for DEBUG = True
            # lighttp config provide support  for admin`s urls for DEBUG = False
            continue
        if model in apps:
            for url, dir in apps[model]:
                url = make_url(url)
                if url not in paths:
                    paths[url] = make_path(os.path.join(media_dir_decoded, dir))
            continue
        if os.path.isdir(media_dir):
            for dir in os.listdir(media_dir):
                if dir == '.svn':
                    continue
                dir = dir.decode(fs_encoding)
                url = make_url(dir)
                if url not in paths:
                    paths[url] = make_path(os.path.join(media_dir_decoded, dir))

    # It won't change, so convert it to a tuple to save memory.
    paths = tuple( [ (url, path) for url, path in paths.iteritems() ] )
    return paths
