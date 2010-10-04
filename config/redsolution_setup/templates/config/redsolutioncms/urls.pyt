# ---- django-server-config ----

urlpatterns = patterns('', (r'^', include('config.urls'))) + urlpatterns
