from django.contrib.auth.models import AnonymousUser
from selenium.common.exceptions import NoSuchElementException
from functional_tests.base import FunctionalTest


class PermissionTest(FunctionalTest):
    message_no_such_element = "Unable to locate menu grouper '%s'."

    def setUp(self):
        super(PermissionTest, self).setUp()

        # Create Visitor user
        self.visitor = AnonymousUser()

        # Create User without privileges
        self.registered_data = {'username': 'registered', 'password': 'demo'}
        self.registered = self.create_user_with_permission(**self.registered_data)

        # Create Assistant user
        self.assistant_data = {'username': 'assistant', 'password': 'demo'}
        assistant_permissions = (
            'view_var', 'view_device', 'view_mimic', 'view_window'
        )
        self.assistant = self.create_user_with_permission(assistant_permissions, **self.assistant_data)

        # Create Operator user
        self.operator_data = {'username': 'operator', 'password': 'demo'}
        operator_permissions = (
            'add_var', 'view_var', 'change_var', 'delete_var', 'set_var'
            'add_device', 'view_device', 'change_device', 'delete_device',
            'add_mimic', 'view_mimic', 'change_mimic', 'delete_mimic',
            'add_window', 'view_window', 'change_window', 'delete_window'
        )
        self.operator = self.create_user_with_permission(operator_permissions, **self.operator_data)

        # Create Inactive user with operator privileges
        # TODO: Inactive user
        self.inactive_data = {'username': 'inactive', 'password': 'demo'}
        self.inactive = self.create_user_with_permission(operator_permissions, **self.inactive_data)

    def test_inactived_cant_do_nothing(self):
        pass

    def test_non_operators_cant_add_objects(self):
        pass

    def test_operator_can_add_objects(self):
        pass

    def test_only_operator_and_assistant_can_view_objects(self):
        pass

    def test_non_operator_and_assistant_cant_view_objects(self):
        pass

    def test_operator_and_assistant_groups_exists_with_permissions(self):
        pass

    def test_new_created_users_are_in_assistant_group(self):
        pass

    def test_public_window_can_view_by_visitor_and_registered(self):
        pass

    def test_private_window_can_viewed_by_assistant_and_operator(self):
        pass

    def test_visitor_registered_menu(self):
        pass

    def test_assistant_menu(self):
        # A assistant logs in
        self.user_login(**self.assistant_data)

        # He notice some menu items:
        # Menu "Dashboards"
        self.get_menu_item()
        # Menu "Dashboards" -> "List"
        self.get_menu_grouper(("List",))
        # Menu "Dashboards" -> "List" -> "Mimics"
        self.get_menu_item(("List", "Mimics"))
        # Menu "Dashboards" -> "List" -> "Windows"
        self.get_menu_item(("List", "Windows"))
        # Menu "Dashboards" -> "List" -> "Devices"
        self.get_menu_item(("List", "Devices"))
        # Menu "Dashboards" -> "List" -> "Vars"
        self.get_menu_item(("List", "Vars"))
        # No menu "Dashboards" -> "Add"
        self.assertRaisesMessage(
            NoSuchElementException,
            self.message_no_such_element % "Add",
            self.get_menu_grouper,
            ("Add",)
        )
        # No menu "Dashboards" -> "Public"
        self.assertRaisesMessage(
            NoSuchElementException,
            self.message_no_such_element % "Public",
            self.get_menu_grouper,
            ("Public",)
        )
        # No menu "Dashboards" -> "Restricted"
        self.assertRaisesMessage(
            NoSuchElementException,
            self.message_no_such_element % "Restricted",
            self.get_menu_grouper,
            ("Restricted",)
        )
        # Add public View
        # Menu "Dashboards" -> "Public" -> <Windows name>
        # Add protected View
        # Menu "Dashboards" -> "Restricted" -> <Windows name>
        # Menu "Help"
        # TODO: Complete this test!

    def test_operator_menu(self):
        # An Operator logs in
        self.user_login(**self.operator_data)

        # He notice some menu items:
        # Menu "Dashboards"
        self.get_menu_item()
        # Menu "Dashboards" -> "Manage"
        self.get_menu_grouper(("Manage",))
        # Menu "Dashboards" -> "Manage" -> "Mimics"
        self.get_menu_item(("Manage", "Mimics"))
        # Menu "Dashboards" -> "Manage" -> "Windows"
        self.get_menu_item(("Manage", "Windows"))
        # Menu "Dashboards" -> "Manage" -> "Devices"
        self.get_menu_item(("Manage", "Devices"))
        # Menu "Dashboards" -> "Manage" -> "Vars"
        self.get_menu_item(("Manage", "Vars"))
        # Menu "Dashboards" -> "Add"
        self.get_menu_grouper(("Add",))
        # Menu "Dashboards" -> "Add" -> "Mimic"
        self.get_menu_item(("Add", "Mimic"))
        # Menu "Dashboards" -> "Add" -> "Window"
        self.get_menu_item(("Add", "Window"))
        # Menu "Dashboards" -> "Add" -> "Device"
        self.get_menu_item(("Add", "Device"))
        # Menu "Dashboards" -> "Add" -> "Vars"
        self.get_menu_item(("Add", "Var"))
        # No menu "Dashboards" -> "Public"
        self.assertRaisesMessage(
            NoSuchElementException,
            self.message_no_such_element % "Public",
            self.get_menu_grouper,
            ("Public",)
        )
        # No menu "Dashboards" -> "Restricted"
        self.assertRaisesMessage(
            NoSuchElementException,
            self.message_no_such_element % "Restricted",
            self.get_menu_grouper,
            ("Restricted",)
        )
        # Add public View
        # Menu "Dashboards" -> "Public" -> <Windows name>
        # Add protected View
        # Menu "Dashboards" -> "Restricted" -> <Windows name>
        # Menu "Help"
        # TODO: Complete this test!

    def get_menu_grouper(self, menu_path=None):
        """
        Return a menu group item.

        :param menu_path: tuple with consecutively hierarchy menu texts
        :return: selenium web element of the menu or raise NoSuchElementException exception
        """
        if menu_path is None:
            menu_path = ("Dashboards",)
        else:
            submenu = self.browser.find_element_by_css_selector('nav .mimics.dropdown .dropdown-menu')
            if not submenu.is_displayed():
                # Display submenu
                self.browser.find_element_by_link_text('Dashboards').click()

        groupers = self.browser.find_elements_by_css_selector('li.dropdown-header')
        for grouper in groupers:
            if grouper.text == menu_path[-1]:
                return grouper
        # if not found raise exception
        raise NoSuchElementException(self.message_no_such_element % menu_path[-1])
