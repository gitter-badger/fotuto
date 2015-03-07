from django.contrib import messages
from django.core.urlresolvers import resolve
from django.test import TestCase
from vars.forms import VarForm, DeviceForm
from vars.models import Device, Var


class DeviceAddTest(TestCase):
    maxDiff = None
    device_add_url = '/devices/add/'

    def test_add_url_resolves_to_create_view(self):
        found = resolve(self.device_add_url)
        self.assertEqual(found.func.func_name, 'DeviceCreateView')

    def test_add_page_render_device_form_template(self):
        response = self.client.get(self.device_add_url)
        self.assertTemplateUsed(response, 'vars/device_form.html')

    def test_add_page_uses_device_form(self):
        response = self.client.get(self.device_add_url)
        self.assertIsInstance(response.context['form'], DeviceForm)

    def test_add_device_can_save_a_post_request(self):
        self.client.post(self.device_add_url, data={'name': 'Device 1 name', 'address': '1234'})
        self.assertEqual(Device.objects.count(), 1)
        new_device = Device.objects.first()
        self.assertEqual(new_device.name, 'Device 1 name')

    def test_add_device_message(self):
        response = self.client.post(self.device_add_url, data={'name': 'Device 1 name', 'address': '1234'})
        messages_list = list(messages.get_messages(response.wsgi_request))
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(messages_list[0].level_tag, 'success')
        self.assertIn(messages_list[0].message, 'Device was added.')

    def test_add_device_page_redirects_after_POST(self):
        response = self.client.post(self.device_add_url, data={'name': 'Device 1 name', 'address': '1234'})
        self.assertRedirects(response, '/devices/')

    def test_add_device_print_message(self):
        response = self.client.post(self.device_add_url, data={'name': 'Device 1 name', 'address': '1234'})
        response_redirected = self.client.get(response.url)
        self.assertIn('Device was added.', response_redirected.rendered_content)

    def test_autogenerate_slug_field(self):
        device = self.save_device_form(name="Some Device Name", address='1234')
        self.assertEqual(device.slug, 'some-device-name')

    def test_autogenerate_slug_field_must_be_unique(self):
        device_name = "Unique name"

        device1 = self.save_device_form(name=device_name, address='1')
        device2 = self.save_device_form(name=device_name, address='2')
        self.assertEqual(device2.slug, '%s-%s' % (device1.slug, device2.pk - 1))

        device3 = self.save_device_form(name=device_name, address='3')
        self.assertEqual(device3.slug, '%s-%s' % (device1.slug, device3.pk - 1))

    def save_device_form(self, **device_data):
        """Fill :class:`~vars.forms.DeviceForm` with data specified and return instance."""
        device_form = DeviceForm(data=device_data)
        return device_form.save()


class DeviceListTest(TestCase):
    def test_list_url_resolves_to_list_view(self):
        found = resolve('/devices/')
        self.assertEqual(found.func.func_name, 'ListView')


class VarAddTest(TestCase):
    maxDiff = None
    var_add_url = '/vars/add/'

    def setUp(self):
        # a device is required for a var
        self.device, create = Device.objects.get_or_create(name="Device 1", slug="device-1", model="111", address="123")

    def test_add_url_resolves_to_create_view(self):
        found = resolve(self.var_add_url)
        self.assertEqual(found.func.func_name, 'VarCreateView')

    def test_add_page_render_var_form_template(self):
        response = self.client.get(self.var_add_url)
        self.assertTemplateUsed(response, 'vars/var_form.html')

    def test_add_page_uses_var_form(self):
        response = self.client.get(self.var_add_url)
        self.assertIsInstance(response.context['form'], VarForm)

    def test_add_var_require_device_create_message(self):
        # Remove all devices
        Device.objects.all().delete()
        response = self.client.get(self.var_add_url)
        messages_list = list(messages.get_messages(response.wsgi_request))
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(messages_list[0].level_tag, 'info')
        self.assertIn(messages_list[0].message, 'Please, add a device first.')

    def test_add_var_require_device_redirect(self):
        # Remove all devices
        Device.objects.all().delete()
        response = self.client.get(self.var_add_url)
        self.assertRedirects(response, '/devices/add/')

    def test_add_var_require_device_print_message(self):
        # Remove all devices
        Device.objects.all().delete()
        response = self.client.get(self.var_add_url)
        response_redirected = self.client.get(response.url)
        self.assertIn('Please, add a device first.', response_redirected.rendered_content)

    def test_add_var_can_save_a_post_request(self):
        self.client.post(self.var_add_url, data={'name': 'Var 1 name', 'device': self.device.pk})
        self.assertEqual(Var.objects.count(), 1)
        new_var = Var.objects.first()
        self.assertEqual(new_var.name, 'Var 1 name')

    def test_add_var_page_redirects_after_POST(self):
        response = self.client.post(self.var_add_url, data={'name': 'Var 1 name', 'device': self.device.pk})
        self.assertRedirects(response, '/vars/')

    def test_add_var_message(self):
        response = self.client.post(self.var_add_url, data={'name': 'Var 1 name', 'device': self.device.pk})
        messages_list = list(messages.get_messages(response.wsgi_request))
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(messages_list[0].level_tag, 'success')
        self.assertIn(messages_list[0].message, 'Variable was added.')

    def test_add_var_print_message(self):
        response = self.client.post(self.var_add_url, data={'name': 'Var 1 name', 'device': self.device.pk})
        response_redirected = self.client.get(response.url)
        self.assertIn('Variable was added.', response_redirected.rendered_content)

    def test_autogenerate_slug_field(self):
        var = self.save_var_form(name="Some Var Name")
        self.assertEqual(var.slug, 'some-var-name')

    def test_autogenerate_slug_field_must_be_unique(self):
        var_name = "Unique name"

        var1 = self.save_var_form(name=var_name)
        var2 = self.save_var_form(name=var_name)
        self.assertEqual(var2.slug, '%s-%s' % (var1.slug, var2.pk - 1))

        var3 = self.save_var_form(name=var_name)
        self.assertEqual(var3.slug, '%s-%s' % (var1.slug, var3.pk - 1))

    def save_var_form(self, **var_data):
        """Fill :class:`~var.forms.VarForm` with data specified and return instance."""
        if 'device' not in var_data:
            var_data['device'] = self.device.pk
        var_form = VarForm(data=var_data)
        return var_form.save()


class VarListTest(TestCase):
    def setUp(self):
        # Var require a device
        self.device, create = Device.objects.get_or_create(name="Device 1", slug="device-1", model="111", address="123")

    def test_list_url_resolves_to_list_view(self):
        found = resolve('/vars/')
        self.assertEqual(found.func.func_name, 'ListView')

    def test_uses_template(self):
        response = self.client.get('/vars/')
        self.assertTemplateUsed(response, 'vars/var_list.html')

    def test_displays_all_vars(self):
        Var.objects.create(name="First Var Name", slug="var1", device=self.device)
        Var.objects.create(name="Second Var Name", slug="var2", device=self.device)
        response = self.client.get('/vars/')
        self.assertContains(response, "First Var Name")
        self.assertContains(response, "Second Var Name")