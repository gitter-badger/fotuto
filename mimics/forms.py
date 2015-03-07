from django import forms
from django.forms.widgets import HiddenInput
from mimics.models import Mimic


class MimicManageForm(forms.ModelForm):
    class Meta:
        model = Mimic
        fields = '__all__'
        widgets = {
            'window': HiddenInput
        }