from fotutils.tests import ModelTestHelper
from vars.models import Device, Var


class DeviceModelTest(ModelTestHelper):
    def test_saving_and_retrieving_devices(self):
        dev1 = {'name': "First Device Name", 'slug': 'dev1', 'address': '1'}
        dev2 = {'name': "Second Device Name", 'slug': 'dev2', 'address': '2'}
        self.check_saving_and_retrieving_objects(model=Device, obj1_dict=dev1, obj2_dict=dev2)

    def test_require_name(self):
        self.check_require_field(model=Device, required_field='name', name="", slug='dev1', address='1')

    def test_require_slug(self):
        self.check_require_field(model=Device, name="First Device Name", address='123')

    def test_unique_slug(self):
        dev1 = {'name': "First Device Name", 'address': '1'}
        dev2 = {'name': "Second Device Name", 'address': '2'}
        self.check_unique_field(model=Device, obj1_dict=dev1, obj2_dict=dev2)

    def test_require_address(self):
        self.check_require_field(model=Device, required_field='address', name="First Device Name", slug='dev1')

    def test_unique_address(self):
        dev1 = {'name': "First Device Name", 'slug': 'dev1'}
        dev2 = {'name': "Second Device Name", 'slug': 'dev2'}
        self.check_unique_field(model=Device, unique_field='address', obj1_dict=dev1, obj2_dict=dev2)

    def test_string_representation(self):
        self.check_string_representation(Device, "Device Name", name="Device Name", address='1')


class VarModelTest(ModelTestHelper):
    def setUp(self):
        # Var require a device
        self.device, create = Device.objects.get_or_create(name="Device 1", slug="device-1", model="111", address="123")

    def test_saving_and_retrieving_vars(self):
        var1 = {'name': "First Var Name", 'slug': 'var1', 'device': self.device}
        var2 = {'name': "Second Var Name", 'slug': 'var2', 'device': self.device}
        self.check_saving_and_retrieving_objects(model=Var, obj1_dict=var1, obj2_dict=var2)

    def test_require_name(self):
        self.check_require_field(model=Var, required_field='name', name="", slug='var1', device=self.device)

    def test_require_slug(self):
        self.check_require_field(model=Var, name="Var Name", device=self.device)

    def test_unique_slug(self):
        var1 = {'name': "First Var Name", 'device': self.device}
        var2 = {'name': "Second Var Name", 'device': self.device}
        self.check_unique_field(model=Var, obj1_dict=var1, obj2_dict=var2)

    def test_require_device(self):
        self.check_require_field(model=Var, required_field='device', error_key='null', name="Var Name", slug='var1')

    def test_string_representation(self):
        var_name_attr = "Var name"
        var_name = "[%s] %s" % (self.device.slug, var_name_attr)
        self.check_string_representation(Var, var_name, name=var_name_attr, device=self.device)