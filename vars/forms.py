from django import forms
from vars.models import Var


class VarForm(forms.ModelForm):
    class Meta:
        model = Var
        fields = '__all__'

