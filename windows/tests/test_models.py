from fotutils.tests import ModelTestHelper
from windows.models import Window


class WindowModelTest(ModelTestHelper):
    model = Window

    def test_saving_and_retrieving_windows(self):
        win1 = {'title': "First Window Title", 'slug': 'win1'}
        win2 = {'title': "Second Window Title", 'slug': 'win2'}
        self.check_saving_and_retrieving_objects(obj1_dict=win1, obj2_dict=win2)

    def test_require_slug(self):
        self.check_require_field(title="Some title")

    def test_unique_slug(self):
        win1 = {'title': "First Window Title"}
        win2 = {'title': "Second Window Title"}
        self.check_unique_field(obj1_dict=win1, obj2_dict=win2)

    def test_get_absolute_url(self):
        window = Window.objects.create(title="Some Window Title", slug="win")
        self.assertEqual(window.get_absolute_url(), '/windows/%s/' % (window.slug,))

    def test_string_representation(self):
        self.check_string_representation("Some Window Title", title="Some Window Title")