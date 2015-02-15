from django import http
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import CreateView
from vars.forms import VarForm
from vars.models import Var, Device


class VarCreateView(CreateView):
    """Add new var"""
    model = Var
    form_class = VarForm
    success_url = reverse_lazy('var_list')

    def dispatch(self, request, *args, **kwargs):
        if Device.objects.count() == 0:
            messages.info(request, "Please, add a device first.")
            return http.HttpResponseRedirect(reverse('device_add'))
        return super(VarCreateView, self).dispatch(request, *args, **kwargs)
