from django import forms
from django.forms import HiddenInput
from django.utils.text import slugify


class ModelFormWithSlugBase(forms.ModelForm):
    """Base ModelForm form models with a slug field."""

    class Meta:
        fields = '__all__'
        widgets = {
            'slug': HiddenInput
        }

    def __init__(self, *args, **kwargs):
        super(ModelFormWithSlugBase, self).__init__(*args, **kwargs)
        self.fields['slug'].required = False

    def clean_slug(self):
        """
        Auto-generate slug from name if left in blank.
        """
        return self.generate_slug_from_field()

    def generate_slug_from_field(self, target_field='name', default_value=None):
        """
        Auto-generate slug from a field if left in blank. Call this in clean_slug method.

        If slug exist, try by incrementing a suffix number.

        :param target_field: field name of the target field to generate slug (default: 'name')
        :param default_value: if subclass form provides a default value for target_field, specify it in this
            param (default: None)

        Usage::
            class YourModelForm(ModelFormWithSlugBase):

                class Meta(ModelFormWithSlugBase.Meta):
                    model = YOUR_MODEL

                def clean_slug(self):
                    return self.generate_slug_from_field('name')
        """
        data = self.cleaned_data['slug'] or slugify(self.cleaned_data[target_field]) or default_value
        # Validate unique
        slug_exists_count = self._meta.model.objects.filter(slug__regex=r'^%s(-\d+)?$' % data).count()
        if slug_exists_count:
            data += '-%s' % slug_exists_count
        return data
