from django.views.generic import CreateView
from mimics.models import Mimic


class MimicManageView(CreateView):
    model = Mimic