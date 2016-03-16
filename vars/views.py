from django import http
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from rest_framework import viewsets

from .forms import VarForm, DeviceForm
from .models import Var, Device
from .serializers import DeviceSerializer, VarSerializer


class DeviceCreateView(SuccessMessageMixin, CreateView):
    model = Device
    form_class = DeviceForm
    success_url = reverse_lazy('device_list')
    success_message = "Device was added."


class VarCreateView(SuccessMessageMixin, CreateView):
    """Add new var"""
    model = Var
    form_class = VarForm
    success_url = reverse_lazy('var_list')
    success_message = "Variable was added."

    @method_decorator(permission_required('vars.add_var'))
    def dispatch(self, request, *args, **kwargs):
        if Device.objects.count() == 0:
            messages.info(request, "Please, add a device first.")
            return http.HttpResponseRedirect(reverse('device_add'))
        return super(VarCreateView, self).dispatch(request, *args, **kwargs)


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class VarViewSet(viewsets.ModelViewSet):
    queryset = Var.objects.all()
    serializer_class = VarSerializer
    filter_fields = ('device', 'mimic', 'mimic__window')
