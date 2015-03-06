from fotutils.forms import ModelFormWithSlugBase
from windows.models import Window


class WindowForm(ModelFormWithSlugBase):

    class Meta(ModelFormWithSlugBase.Meta):
        model = Window

    def __init__(self, *args, **kwargs):
        super(WindowForm, self).__init__(*args, **kwargs)
        self.fields['title'].required = False

    def clean_slug(self):
        """
        Auto-generate slug from title if left in blank.
        """
        return self.generate_slug_from_field(target_field='title', default_value="Untitled")

    def clean_title(self):
        return self.cleaned_data['title'] or "Untitled"