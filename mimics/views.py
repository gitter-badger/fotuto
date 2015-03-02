from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView
from mimics.models import Mimic
from windows.models import Window


class MimicManageView(SuccessMessageMixin, CreateView):
    model = Mimic
    template_name = 'mimics/mimic_manage_form.html'
    success_message = "Mimic was added."

    def get_success_url(self):
        return reverse('mimic_manage_window', args=(self.window.slug,))

    def get_initial(self):
        """
        Add window field.
        """
        initial = self.initial.copy()
        self.window = get_object_or_404(Window, slug=self.kwargs.get('window'))
        initial['window'] = self.window.pk
        return initial

    def get_context_data(self, **kwargs):
        context = super(MimicManageView, self).get_context_data(**kwargs)
        context['window'] = self.window
        return context