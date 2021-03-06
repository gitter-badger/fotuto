from fotutils.tests import ModelTestHelper
from vars.models import Device, Var


class DeviceModelTest(ModelTestHelper):
    model = Device

    def test_saving_and_retrieving_devices(self):
        dev1 = {'name': "First Device Name", 'slug': 'dev1', 'address': '1'}
        dev2 = {'name': "Second Device Name", 'slug': 'dev2', 'address': '2'}
        self.check_saving_and_retrieving_objects(obj1_dict=dev1, obj2_dict=dev2)

    def test_require_name(self):
        self.check_require_field(required_field='name', name="", slug='dev1', address='1')

    def test_require_slug(self):
        self.check_require_field(name="First Device Name", address='123')

    def test_unique_slug(self):
        dev1 = {'name': "First Device Name", 'address': '1'}
        dev2 = {'name': "Second Device Name", 'address': '2'}
        self.check_unique_field(obj1_dict=dev1, obj2_dict=dev2)

    def test_require_address(self):
        self.check_require_field(required_field='address', name="First Device Name", slug='dev1')

    def test_unique_address(self):
        dev1 = {'name': "First Device Name", 'slug': 'dev1'}
        dev2 = {'name': "Second Device Name", 'slug': 'dev2'}
        self.check_unique_field(unique_field='address', obj1_dict=dev1, obj2_dict=dev2)

    def test_string_representation(self):
        self.check_string_representation("Device Name", name="Device Name", address='1')

    def test_list_ordering(self):
        dev1 = Device.objects.create(name="2", slug='dev2', address='2')
        dev2 = Device.objects.create(name="Dev 1", slug='dev1', address='1')
        dev3 = Device.objects.create(name="D3", slug='dev3', address='3')
        self.assertEqual(list(Device.objects.all()), [dev1, dev2, dev3])


class VarModelTest(ModelTestHelper):
    model = Var

    def setUp(self):
        # Var require a device
        self.device, create = Device.objects.get_or_create(name="Device 1", slug="device-1", model="111", address="123")

    def test_saving_and_retrieving_vars(self):
        var1 = {'name': "First Var Name", 'slug': 'var1', 'device': self.device}
        var2 = {'name': "Second Var Name", 'slug': 'var2', 'device': self.device}
        self.check_saving_and_retrieving_objects(obj1_dict=var1, obj2_dict=var2)

    def test_require_name(self):
        self.check_require_field(required_field='name', name="", slug='var1', device=self.device)

    def test_require_slug(self):
        self.check_require_field(name="Var Name", device=self.device)

    def test_unique_slug(self):
        var1 = {'name': "First Var Name", 'device': self.device}
        var2 = {'name': "Second Var Name", 'device': self.device}
        self.check_unique_field(obj1_dict=var1, obj2_dict=var2)

    def test_require_device(self):
        self.check_require_field(required_field='device', error_key='null', name="Var Name", slug='var1')

    def test_string_representation(self):
        var_name_attr = "Var name"
        var_name = "[%s] %s" % (self.device.slug, var_name_attr)
        self.check_string_representation(var_name, name=var_name_attr, device=self.device)

    def test_list_ordering(self):
        device2 = Device.objects.create(name="Dev2", slug='dev2', address='2')
        var1 = Var.objects.create(name="Var 1", slug='v1', active=False, device=self.device)
        var2 = Var.objects.create(name="2", slug='v2', device=device2)
        var3 = Var.objects.create(name="2", slug='v3', device=self.device)
        var4 = Var.objects.create(name="V3", slug='v4', device=self.device)
        right_ordered_list = [
            var3,  # first var of first device
            var4,  # second var of first device
            var2,  # Second device
            var1   # Inactive vars at bottom
        ]
        self.assertEqual(list(Var.objects.all()), right_ordered_list)

