from django import forms
from django.utils.text import slugify
from vars.models import Var


class VarForm(forms.ModelForm):

    slug = forms.SlugField(max_length=25, required=False)

    class Meta:
        model = Var
        fields = '__all__'

    def clean_slug(self):
        """
        Auto-generate slug from name if left in blank.

        If slug exist, try by incrementing a suffix.
        """
        data = self.cleaned_data['slug']
        if data == '':
            data = slugify(self.cleaned_data['name'])
            # Validate unique
            slug_exists_count = self._meta.model.objects.filter(slug__regex=r'^%s(-\d+)?$' % data).count()
            if slug_exists_count:
                data += '-%s' % slug_exists_count
        return data