from django.core.urlresolvers import reverse
from django.forms.models import inlineformset_factory, modelform_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from config.grandma_setup.models import ConfigSettings, ConfigSite, ConfigRedirect

def index(request):
    config_settings = ConfigSettings.objects.get_settings()
    site_formset_class = inlineformset_factory(ConfigSettings, ConfigSite)
    redirect_formset_class = inlineformset_factory(ConfigSettings, ConfigRedirect)

    if request.method == 'POST':
        site_formset = site_formset_class(data=request.POST, files=request.FILES, instance=config_settings)
        redirect_formset = redirect_formset_class(data=request.POST, files=request.FILES, instance=config_settings)
        if site_formset.is_valid() and redirect_formset.is_valid():
            site_formset.save()
            redirect_formset.save()
            return HttpResponseRedirect(reverse('custom'))
    else:
        site_formset = site_formset_class(instance=config_settings)
        redirect_formset = redirect_formset_class(instance=config_settings)
    return render_to_response('config/grandma/index.html', {
        'site_formset': site_formset,
        'redirect_formset': redirect_formset,
    }, context_instance=RequestContext(request))
