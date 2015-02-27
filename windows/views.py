from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView
from windows.forms import WindowForm
from windows.models import Window


class WindowDetailView(DetailView):
    """Display a windows with mimics"""
    model = Window


class WindowCreateView(SuccessMessageMixin, CreateView):
    model = Window
    form_class = WindowForm
    success_url = reverse_lazy('window_list')
    success_message = "Window was added."

