# django-config
INSTALLED_APPS += ['config']

CONFIG_SITES = [{% for site in config_settings.sites.all %}
    '{{ site.site }}', {% endfor %}
]
CONFIG_REDIRECTS = [{% for site in config_settings.redirects.all %}
    '{{ site.site }}', {% endfor %}
]

{% for app in config_settings.appmedia.all %}
CONFIG_APP_MEDIA = {
    '{{ app.appname }}': [
        ('{{ app.source }}', '{{ app.target }}',),
    ],
}
{% endfor %}
