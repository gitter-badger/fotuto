from django.views.generic import CreateView
from vars.models import Var


class VarCreateView(CreateView):
    """Add new var"""
    model = Var
