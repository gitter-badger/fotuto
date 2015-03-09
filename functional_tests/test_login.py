from django.contrib.auth.models import User  # TODO: use setting.AUTH_USER_MODEL
from .base import FunctionalTest


class LoginTest(FunctionalTest):

    def setUp(self):
        super(LoginTest, self).setUp()
        # Create user to login
        self.operator = User.objects.create_user(username='operator', password='demo')

    def test_login(self):
        # A visitor goes to fotuto site and notices a "Sign in" button.
        self.browser.get(self.server_url)
        self.browser.find_element_by_class_name('btn-login').click()

        # Login form appears and visitor logs with hes credential
        input_user = self.browser.find_element_by_id('id_username')
        input_user.send_keys(self.operator.username)
        input_pass = self.browser.find_element_by_id('id_password')
        input_pass.send_keys(self.operator.password)

        # He can see that he is logged in
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertIn('operator', navbar.text)