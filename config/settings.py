import os
import sys

from django.conf import settings
from django.contrib import admin
from config.utils import make_path, make_url, get_app_media_paths

media_url = make_url(getattr(settings, 'MEDIA_URL'))
media_path = make_path(getattr(settings, 'MEDIA_ROOT'))

admin_media_url = make_url(getattr(settings, 'ADMIN_MEDIA_PREFIX'))
admin_media_path = make_path(os.path.join(os.path.dirname(admin.__file__), 'media'))

project_name = os.environ['DJANGO_SETTINGS_MODULE'].split('.')[0]
project_file = sys.argv[0]

project_url = getattr(settings, 'PROJECT_URL', '127.0.0.1:8000')
project_redirects = getattr(settings, 'PROJECT_REDIRECTS', [])
project_auth = getattr(settings, 'PROJECT_AUTH', False)

app_media_paths = get_app_media_paths(admin_media_url, admin_media_path)
