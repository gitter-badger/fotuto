from django.utils.datetime_safe import datetime
from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest


class OperatorTest(FunctionalTest):
    def test_operator_can_add_vars_to_window(self):
        # A operator go to add var page
        self.browser.get('%s/vars/add/' % self.server_url)

        # A login form with a message is shown
        # TODO: self.check_notification_message("Please, login as an operator to access to this page", 'warning')

        # Add user with permission to add var
        credentials = {'username': 'operator', 'password': '123'}
        self.create_user_with_permission(permissions='add_var', **credentials)

        # Operator type his credential and proceed to log-in
        input_username = self.browser.find_element_by_id('id_username')
        input_username.send_keys(credentials['username'])
        input_password = self.browser.find_element_by_id('id_password')
        input_password.send_keys(credentials['password'])
        btn_submit = self.browser.find_element_by_css_selector('button.btn-primary')
        btn_submit.click()

        # Check operator menu
        menu = self.get_menu_item()
        # self.assertEqual(len(menu.find_elements_by_tag_name('li')), 12)
        self.goto_menu_item(("Add", "Var"))
        # Operator have more options to customize the scada:
        # Menus:
        # * Mimics -> Add -> Window
        # * Mimics -> Add -> Device
        # * Mimics -> Add -> Var
        # * Mimics -> Add -> Mimic
        # * Mimics -> Manage -> Windows
        # * Mimics -> Manage -> Devices
        # * Mimics -> Manage -> Vars
        # * Mimics -> Manage -> Mimic
        # * Mimics -> Windows -> Window 1 Title
        # * Mimics -> Windows -> Window 2 Title
        # * ...
        # * Mimics -> Windows -> Window n Title
        # * History -> Add -> Chart
        # * History -> Manage -> Charts

        # Since there is not devices to attach a variable it is redirected to add a device
        # He notes Add Device page
        self.check_page_title_and_header(title="Add Device", header="Add Device")
        # He notice breadcrumbs (devices > add new)
        self.check_breadcrumbs((("Devices", '/devices/'), ("Add new",)))
        # He notes enter device first notification
        self.check_notification_message("Please, add a device first", 'info')

        # Enter device data
        device_name = 'Router'
        input_name = self.browser.find_element_by_id('id_name')
        # TODO: self.assertEqual(input_name.get_attribute('placeholder'), 'Name of the Device')
        input_name.send_keys(device_name)
        input_name = self.browser.find_element_by_id('id_address')
        input_name.send_keys('1234')

        # Submit form to add device
        btn_submit = self.browser.find_element_by_css_selector('button.btn-primary')
        btn_submit.click()

        # He notes Device list page
        self.check_page_title_and_header(title="Devices", header="Devices")
        # He notice breadcrumbs (devices)
        self.check_breadcrumbs((("Devices",),))
        # He notice the added device confirmation message
        self.check_notification_message("Device was added")

        # Operator goes to add var page
        self.goto_menu_item(("Add", "Var"))
        self.check_page_title_and_header(title="Add Variable", header="Add Variable")

        # He notice breadcrumbs (vars > add new)
        self.check_breadcrumbs((("Variables", '/vars/'), ("Add new",)))

        # Enter variable data
        var_name = 'Low Battery'
        input_var_name = self.browser.find_element_by_id('id_name')
        # TODO: self.assertEqual(input_name.get_attribute('placeholder'), 'Name of the variable')
        input_var_name.send_keys(var_name)
        # Select device
        select_var_device = self.browser.find_element_by_id('id_device')
        select_var_device.send_keys(Keys.ARROW_DOWN)
        # Specify a value
        input_var_value = self.browser.find_element_by_id('id_value')
        input_var_value.send_keys('1.0')

        # Submit form to add var
        btn_submit = self.browser.find_element_by_css_selector('button.btn-primary')
        btn_submit.click()

        # It is redirected to var list
        self.check_page_title_and_header(title="Variables", header="Variables")
        # He notice breadcrumbs (vars)
        self.check_breadcrumbs((("Variables",),))
        # Confirmation message is shown
        self.check_notification_message("Variable was added")

        # In the list appears new var added
        table = self.browser.find_element_by_class_name('table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(var_name in row.text for row in rows)
        )

        # Add new added variable to window
        # Since a new device with a variable was added, automatically new mimic with var was created
        # So create new window
        self.goto_menu_item(("Add", "Window"))
        self.check_page_title_and_header(title="Add Window", header="Add Window")
        # He notice breadcrumbs (windows > add new)
        self.check_breadcrumbs((("Windows", '/windows/'), ("Add new",)))

        # Enter window data
        window_title = 'Main window'
        input_title = self.browser.find_element_by_id('id_title')
        # TODO: self.assertEqual(input_name.get_attribute('placeholder'), 'Title of the window')
        input_title.send_keys(window_title)

        # Submit form to add window
        btn_submit = self.browser.find_element_by_css_selector('button.btn-primary')
        btn_submit.click()

        # Now he is in windows list page
        self.check_page_title_and_header(title="Windows", header="Windows")
        # He notice breadcrumbs
        self.check_breadcrumbs((("Windows",),))

        # So click in manage mimics button of a first
        # FIXME: This flow should be change in favor of a wizard
        button_manage_mimic = self.browser.find_elements_by_class_name('manage-mimics')[0]
        button_manage_mimic.click()

        # Now he is in manage mimics for the window page
        self.check_page_title_and_header(title="Manage Mimics", header="Manage Mimics")
        # He notice breadcrumbs (windows > Window.Title > Mimics)
        self.check_breadcrumbs((("Windows", '/windows/'), (window_title, '/windows/main-window/'), ("Mimics",),))

        # Add mimic to window
        mimic_name = "Router"
        input_mimic_name = self.browser.find_element_by_id('id_name')
        input_mimic_name.send_keys(mimic_name)
        # Specify var
        select_mimic_vars = self.browser.find_element_by_id('id_vars')
        select_mimic_vars.send_keys(Keys.ARROW_DOWN)
        # Left other mimic field with it default values
        # TODO: Enter position values and check them in window details page

        # Submit form to add mimic to window
        btn_submit = self.browser.find_element_by_css_selector('button.btn-primary')
        btn_submit.click()

        # TODO: Add mimic from device (use name and vars from device)

        # Confirmation message is shown
        self.check_notification_message("Mimic was added")

        # Go to window details page (using breadcrumbs)
        button_view = self.browser.find_elements_by_link_text(window_title)[0]
        button_view.click()

        # Now he is details window page
        self.check_page_title_and_header(title=window_title, header=window_title)
        # He notice breadcrumbs (windows > Window.Title)
        self.check_breadcrumbs((("Windows", '/windows/'), (window_title,),))

        # Then mimic for device with new variable is shown
        mimic_name_html = self.browser.find_elements_by_css_selector('.mimic .name')[0].text
        self.assertIn(mimic_name, mimic_name_html)

        # A variable value indicator and variable's name is shown
        var_item = self.browser.find_elements_by_css_selector('.mimic .var')[0]
        self.assertIn(var_name, var_item.text)
        self.assertEqual("1.0", var_item.find_element_by_class_name('value').text)

        # Last update timestamp is shown in page
        last_update_text = self.browser.find_element_by_css_selector('#last_updated_notificaion .value').text
        # Timestamp is close to now
        # TODO: Use human friendly format and/or django settings date and times format
        last_update_date = datetime.strptime(last_update_text, '%Y-%m-%d @ %H:%M:%S')
        now = datetime.now()
        # FIXME: date time must be tz aware
        self.assertAlmostEqual((now - last_update_date).total_seconds(), 0, delta=5)
        # TODO: replace delta 5 with a new window.refresh_interval field
        # some time later last update changes
        # If var value change some time later change is displayed
        self.fail("Complete test!")