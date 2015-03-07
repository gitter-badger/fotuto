from fotutils.tests import ModelTestHelper
from mimics.models import Mimic
from windows.models import Window


class MimicModelTest(ModelTestHelper):
    def setUp(self):
        # Mimics require a window
        self.window, create = Window.objects.get_or_create(slug="win1")

    def test_saving_and_retrieving_mimic(self):
        mimic1 = {'name': "First Mimic Name", 'window': self.window}
        mimic2 = {'name': "Second Mimic Name", 'window': self.window}
        # TODO: specify vars
        self.check_saving_and_retrieving_objects(model=Mimic, obj1_dict=mimic1, obj2_dict=mimic2)

    def test_require_window(self):
        self.check_require_field(model=Mimic, required_field='window', error_key='null')