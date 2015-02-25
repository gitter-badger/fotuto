from django import forms
from mimics.models import Mimic


class MimicManageForm(forms.ModelForm):
    class Meta:
        model = Mimic
        fields = '__all__'