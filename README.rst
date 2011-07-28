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
       # Enable backups with duply & duplicity (http://duplicity.nongnu.org)
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

If ``staticfiles`` is used there is no need to include ``config.urls`` in ``urlconf.py``. On the other hand, probably you will want to include ``staticfiles_urlpatterns()`` from staticfiles app (see: `django documentation <https://docs.djangoproject.com/en/dev/howto/static-files/#serving-static-files-in-development>`_ about it) ::

    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()

Duply/Duplicity backups
=======================

Django-server-config can automatically create backups configuration files.
It supports `duply <http://duply.net/>`_ (`duplicity <http://duplicity.nongnu.org/>`_) configuration scheme.
Duplicity is backup system written in python and using rsync algorithm and Duply is bash configuration wrapper for Duplicity.

Backup settings
----------------

**Security Note**

To start using backups you should specify path to main configuration file for duply. Django-server-config expects file in ``*.ini`` format. This file  
can contains secret passwords, so file supposed to be located somewhere in ``/etc/duply/conf.ini`` and belongs to root (superuser).

BACKUP_DUPLY_CONFIG
    Path to duply configuration file
BACKUP_TEMP_DIR
    Temp directory, where database backups will be located. Database dumps will be deleted from file system after each backup session. Default value: ``'/var/backups/postgres'``

**Only PostgreSQL database backups are supported!**

Duply configuration file
-------------------------

It is quite simple to configure duply.
You can create duply initial config simply from command line:::

   duply <profile> create

Then look at ~/.duply/<profile>/conf and follow comments.

Moreover, you can use ours config template::

    GPG_PW='**********'
    TARGET='s3+http://**********@com.mycompany.server/'
    SOURCE='/'
    MAX_AGE=1M
    MAX_FULL_BACKUPS=5
    MAX_FULLBKP_AGE=1W
    DUPL_PARAMS="$DUPL_PARAMS --full-if-older-than $MAX_FULLBKP_AGE " 
    VOLSIZE=50
    DUPL_PARAMS="$DUPL_PARAMS --volsize $VOLSIZE "

This template encrypts backups with GPG and uplaod to AmazonS3 bucket ``com.mycompany.server``.

Pay attention to the ``TAGET`` option. Django-server-config will **automatiocally** add project_name to ``TARGET``. E.g. rendered config will contain value::

    TARGET = s3+http://**********@com.mycompany.server/<myproject>

Consider trailing slash in ``*.ini`` config, django-server-config adds only ``myproject`` without slash.

History
========

* 0.1.0 - Initial commit
* 0.1.1 - Staticfiles support added
* 0.1.2 - Duply backups support

Classifiers:
-------------

`Utilities`_

.. _`Utilities`: http://www.redsolutioncms.org/classifiers/utilities