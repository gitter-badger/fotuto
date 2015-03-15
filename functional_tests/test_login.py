from selenium.common.exceptions import NoSuchElementException
from .base import FunctionalTest


class LoginTest(FunctionalTest):
    def setUp(self):
        super(LoginTest, self).setUp()
        # Create users to login
        self.supervisor_data = {'username': 'supervisor', 'password': 'demo'}
        self.operator_data = {'username': 'operator', 'password': 'demo'}
        self.operator = self.create_user_with_permission(**self.operator_data)
        self.supervisor = self.create_user_with_permission(**self.supervisor_data)

    def test_wrong_credentials(self):
        # A visitor try to logs with wrong password
        self.user_login(self.operator_data['username'], 'wrong-pass')

        # Wrong credential message is shown
        self.check_notification_message(
            "Please enter a correct username and password. Note that both fields may be case-sensitive.", 'danger'
        )

        # Check user isn't logged in
        self.check_user_logged_out()

    def test_login(self):
        # A visitor logs with operator credential
        self.user_login(self.operator_data['username'], self.operator_data['password'])

        # Operator notice hi is logged in
        self.check_user_logged_in(self.operator.username)

        # Operator logs out
        self.user_logout()

        # Other visitor logs in with supervisor credentials
        self.user_login(self.supervisor_data['username'], self.supervisor_data['password'])

        # Supervisor see that he is logged in
        self.check_user_logged_in(self.supervisor.username)

    def test_logout_page(self):
        # User log in
        self.user_login(self.supervisor_data['username'], self.supervisor_data['password'])
        # User logs out
        self.user_logout()

        # Logout page is shown
        self.check_page_title_and_header(title="Logout", header="Logout")
        # He notice breadcrumbs (Logout)
        self.check_breadcrumbs((("Logout",),))
        # A logout notification message is shown
        text_in_page = self.browser.find_element_by_tag_name('body').text
        self.assertIn("You has been logged out successfully.", text_in_page)

        # User notice he is logged out
        self.check_user_logged_out(self.operator.username)

    def get_signin_button(self):
        return self.browser.find_element_by_link_text('Sign In')

    def get_logout_button(self):
        # TODO: Move logout button to user popup menu
        return self.browser.find_element_by_link_text('Logout')

    def user_login(self, username, password):
        # A visitor goes to fotuto site and notices a "Sign in" button.
        self.browser.get(self.server_url)
        btn_signin = self.get_signin_button()
        self.assertTrue(btn_signin.is_displayed())
        btn_signin.click()

        # Login form appears
        self.check_page_title_and_header(title="Sign In", header="Sign In")
        # He notice breadcrumbs (Sign in)
        self.check_breadcrumbs((("Sign In",),))

        # Visitor logs with his credential
        input_user = self.browser.find_element_by_id('id_username')
        input_user.send_keys(username)
        input_pass = self.browser.find_element_by_id('id_password')
        input_pass.send_keys(password)
        btn_login = self.browser.find_element_by_css_selector('button.btn-login')
        btn_login.click()

    def user_logout(self):
        btn_logout = self.get_logout_button()
        btn_logout.click()

    def check_user_logged_in(self, username):
        # Logged in user see he is logged in
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertIn(username, navbar.text)  # TODO: Display his name if exist?

        # Sign in button disappears
        self.assertRaises(NoSuchElementException, self.get_signin_button)

        # Log out button is shown
        btn_logout = self.get_logout_button()
        self.assertTrue(btn_logout.is_displayed())

    def check_user_logged_out(self, username=None):
        text_in_page = self.browser.find_element_by_tag_name('body').text

        # User can't see him as logged
        if username is not None:
            self.assertNotIn(username, text_in_page)

        # Logout button disappears
        self.assertRaises(NoSuchElementException, self.get_logout_button)
        self.assertNotIn('Log out', text_in_page)

        # Sign in button is displayed
        btn_signin = self.get_signin_button()
        self.assertTrue(btn_signin.is_displayed())
        self.assertIn('Sign In', text_in_page)
