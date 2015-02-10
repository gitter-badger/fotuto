from django.views.generic import CreateView
from vars.forms import VarForm
from vars.models import Var


class VarCreateView(CreateView):
    """Add new var"""
    model = Var
    form_class = VarForm
