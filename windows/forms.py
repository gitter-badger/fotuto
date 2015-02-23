from django import forms
from django.utils.text import slugify
from windows.models import Window


class WindowForm(forms.ModelForm):

    class Meta:
        model = Window
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(WindowForm, self).__init__(*args, **kwargs)
        self.fields['slug'].required = False

    def clean_slug(self):
        """
        Auto-generate slug from name if left in blank.

        If slug exist, try by incrementing a suffix.
        """
        # TODO: Refactor this
        data = self.cleaned_data['slug']
        if data == '':
            data = slugify(self.cleaned_data['name'])
            # Validate unique
            slug_exists_count = self._meta.model.objects.filter(slug__regex=r'^%s(-\d+)?$' % data).count()
            if slug_exists_count:
                data += '-%s' % slug_exists_count
        return data