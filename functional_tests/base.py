from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import sys

User = get_user_model()


class FunctionalTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super(FunctionalTest, cls).setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super(FunctionalTest, cls).tearDownClass()

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_page_title_and_header(self, url=None, title=None, header=None):
        """Checks if a page have specified title and header.
        :param url: Relative path to page, with start and end sash if None use current page (default None)
        :param title: Text in browser title (default: None)
        :param header: Text in main page heading (default: None)
        """
        if url is not None:
            self.browser.get('%s%s' % (self.server_url, url))
        if title is not None:
            self.assertIn(title, self.browser.title)

        header_text = self.browser.find_element_by_class_name('page-header').text
        if header is not None:
            self.assertIn(header, header_text)

    def check_notification_message(self, message, tag='success'):
        """
        Checks for a notification message in page.

        :param message: Text in message
        :param tag: Message tag level in lowercase (default: success)
        """
        messages_html_items = self.browser.find_elements_by_class_name('alert')
        self.assertEqual(len(messages_html_items), 1)
        self.assertIn('alert-%s' % tag, messages_html_items[0].get_attribute('class'))
        self.assertIn(message, messages_html_items[0].text)

    def check_breadcrumbs(self, items):
        """
        Check for breadcrumbs in current page.

        :param items: list of tuple for items in breadcrumb, each tuple contain:
            0: Visible text displayed
            1: url: Last portion of url (empty for current active item)
        """
        breadcrumbs = self.browser.find_element_by_class_name('breadcrumb')
        # TODO: Check breadcrumb items order
        for item in items:
            if len(item) > 1:  # Has url
                breadcrumb_item = breadcrumbs.find_element_by_link_text(item[0])
                self.assertTrue(breadcrumb_item.get_attribute('href').endswith(item[1]))
            else:
                breadcrumb_item_text = breadcrumbs.find_element_by_css_selector('li.active').text
                self.assertEqual(breadcrumb_item_text, item[0])

    def get_menu_item(self, menu_path=None):
        if menu_path is None:
            menu_path = ("Dashboards",)
        else:
            submenu = self.browser.find_element_by_css_selector('nav .mimics.dropdown .dropdown-menu')
            if not submenu.is_displayed():
                # Display submenu
                self.browser.find_element_by_link_text('Dashboards').click()

        return self.browser.find_element_by_link_text(menu_path[-1])

    def goto_menu_item(self, menu_path):
        self.get_menu_item(menu_path).click()

    def create_user_with_permission(self, permissions=None, **credentials):
        """
        Creates a user and add one or more permissions.

        :type permissions: permission codename (or list of codename) to add to user
        """
        user = User.objects.create_user(**credentials)
        if permissions is not None:
            if not isinstance(permissions, (list, tuple)):
                permissions = (permissions,)
            perms = Permission.objects.filter(codename__in=permissions)
            user.user_permissions.add(*perms)
        return user