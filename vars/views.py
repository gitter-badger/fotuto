from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from vars.forms import VarForm
from vars.models import Var


class VarCreateView(CreateView):
    """Add new var"""
    model = Var
    form_class = VarForm
    success_url = reverse_lazy('var_list')
