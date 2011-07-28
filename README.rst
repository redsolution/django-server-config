====================
django-server-config
====================

- Adds management command to make configs for your project.
  Now it can generate config for lighttpd, logrotate, monit and deploy scripts.
- Automatically recognizes media directories in 3-party applications and takes them into account.

Installation:
=============

In settings.py:
---------------

1. Put ``config`` to your ``INSTALLED_APPS``.

2. Set domain names for your project ::

    CONFIG_SITES = ['www.project-name.com', ]

3. Domains for which you want redirects to your site ::

    CONFIG_REDIRECTS = ['project-name.com', ]

4. Set path to media for unusual 3-party application ::

    CONFIG_APP_MEDIA = {
        'application-name': [
            ('media-root', 'media-url', ),
        ]
    }

Media folders with same name as application modulde will be added automatically.
For example, in ``tinymce`` module media files ::

    tinymce/
        media/
            tinymce/
                js/tinymce.js
                css/style.css
    
will be available at url

    /media/tinymce/js/tinymce.js
    /media/tinymce/css/style.js

In urls.py:
-----------

5. Add config to urls.py for serve static files in debug mode. Add it BEFORE ``django.views.static.serve`` ::

    if settings.DEBUG:
        urlpatterns += patterns('', (r'^', include('config.urls')))


In buildout.cfg:
----------------

6. If you are using zc.buildout, you can add to your parts ``make-config`` to make config files automaticaly::

    [make-config]
    recipe = iw.recipe.cmd
    on_install = true
    on_update = true
    cmds = sudo rm -f bin/init.d bin/lighttpd bin/logrotate bin/monit bin/*.py
       bin/django make_config init.d > bin/init.d
       bin/django make_config lighttpd > bin/lighttpd
       bin/django make_config logrotate > bin/logrotate
       bin/django make_config monit > bin/monit
       ; Enable backups with duply & duplicity (http://duplicity.nongnu.org)
       bin/django make_config duply_conf > bin/duply_conf
       bin/django make_config duply_pre > bin/duply_pre
       bin/django make_config duply_post > bin/duply_post
       bin/django make_config duply_exclude > bin/duply_exclude 
       
       bin/django make_config install.py > bin/install.py
       bin/django make_config uninstall.py > bin/uninstall.py
       bin/django make_config enable.py > bin/enable.py
       bin/django make_config disable.py > bin/disable.py
       
       sudo chown root:root bin/*
       sudo chmod ug=rw,o=r bin/*
       sudo chmod ug=rwx,o=rx bin/init.d bin/django bin/buildout
       echo Configs were saved to "bin/"

Staticfiles support
====================

Since 0.1.1 server-config supports ``django.contrib.staticfiles`` and ``staticfiles`` apps. If one of them present in ``INSTALLED_APPS``, config for webserver will be generated with appropriate rewrite rule.

If ``staticfiles`` is used there is no need to include ``config.urls`` in ``urlconf.py``. On the other hand, probably you will want to include ``staticfiles_urlpatterns()`` from staticfiles app (see: `django documentation <https://docs.djangoproject.com/en/dev/howto/static-files/#serving-static-files-in-development>`_
 about it) ::

    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()

History
========

* 0.1.0 - Initial commit
* 0.1.1 - Staticfiles support added

Classifiers:
-------------

`Utilities`_

.. _`Utilities`: http://www.redsolutioncms.org/classifiers/utilities