from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy, reverse
from django.utils.datetime_safe import datetime
from django.views.generic import CreateView, DetailView
from django.views.generic.base import RedirectView
from rest_framework import viewsets

from .forms import WindowForm
from .models import Window
from .serializers import WindowSerializer


class WindowDefaultView(RedirectView):
    permanent = False
    pattern_name = 'window_details'

    def get_redirect_url(self, *args, **kwargs):
        """Find default window and display it else display add window page with a message."""
        # FIXME: This should ask for a explicit default window instead first window
        default_window = Window.objects.first()
        if default_window is None:
            messages.info(self.request, "No Windows were found. Add new Window from here.")
            return reverse('window_add')
        else:
            kwargs['slug'] = default_window.slug
            return super(WindowDefaultView, self).get_redirect_url(*args, **kwargs)


class WindowDetailView(DetailView):
    """Display a windows with mimics"""
    model = Window

    def get_context_data(self, **kwargs):
        context = super(WindowDetailView, self).get_context_data(**kwargs)
        context['timestamp'] = datetime.now().replace(microsecond=0)
        return context


class WindowCreateView(SuccessMessageMixin, CreateView):
    model = Window
    form_class = WindowForm
    success_url = reverse_lazy('window_list')
    success_message = "Window was added."


class WindowViewSet(viewsets.ModelViewSet):
    queryset = Window.objects.all()
    serializer_class = WindowSerializer

