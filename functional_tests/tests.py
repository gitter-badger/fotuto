from django.test import LiveServerTestCase
from selenium import webdriver


class UsersTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_visitors_cant_view_login_form_only(self):
        self.fail('Create this test!')

    def test_supervisor_can_view_mimics_and_charts(self):
        # A visitor go to ISU-SCADA homepage
        self.browser.get(self.live_server_url)

        # Visitor notice page title and header mention "ISU-SCADA"
        self.assertIn("ISU-SCADA", self.browser.title)

        # A login form is shown
        # Since visitor have supervisor credentials he type it and proceed to log-in
        # TODO: Test login form

        # Then default mimic page is shown

        # Page title and header mention "Mimics"
        self.check_page_title_and_header(title="Mimics", header="Mimics")

        # A welcome message and the operator's name
        welcome_text = self.browser.find_element_by_id('welcome').text
        self.assertEqual("Welcome Elpidio", welcome_text)

        # Menus displays options to view items
        # TODO: If there are more than 1 mimic window no submenu is shown, else list of windows is shown, the same for
        #   History Charts

        # Link to mimic page is active
        menu_active = self.browser.find_element_by_css_selector('nav li.active')
        self.assertEqual("Mimics", menu_active.text)

        # A link to chart page
        menu_chart_link = self.browser.find_element_by_link_text('History charts')
        self.assertTrue(menu_chart_link.get_attribute('href').endswith('/history/'))

        # Following elements appears in the content:

        # A device name is shown
        device_name = self.browser.find_elements_by_css_selector('.mimic .title')[0].text
        self.assertEqual("Router", device_name)

        # A variable value indicator and variable's name
        var_item = self.browser.find_elements_by_css_selector('.mimic .var')[0]
        self.assertEqual("ON", var_item.text)
        self.assertEqual("Working", var_item.get_attribute('title'))

        # A message with last update timestamp
        last_updated_text = self.browser.find_element_by_id('last_updated_notificaion').text
        self.assertIn("Last updated: ", last_updated_text)
        # TODO: Check for the time

        # He notice last update timestamp changed every 3 seconds
        # Then he want to view the chart and click on the link
        # Page is updates with new elements:
        # Chart area is shown
        # An input box to enter a date
        # He notice data plotted in chart change on every update
        # He want to see yesterday chart and enter a date for yesterday in the input box and submit
        # Then Chart area is shown with new data
        self.fail('Finish the test!')

    def test_operator_can_add_vars_to_view(self):
        # A operator go to add var page
        self.browser.get('%s/vars/add/' % self.live_server_url)

        # A login form is shown
        # Operator type his credential and proceed to log-in
        # TODO: Test login form

        # Since there is not devices to attach the variable it is redirected to add a device
        # He notes enter device first notification
        self.check_notification_message("Please, add a device first", 'info')
        # He notes Add Device page
        self.check_page_title_and_header(title="Add Device", header="Add Device")

        # Enter device data
        device_name = 'Router'
        input_name = self.browser.find_element_by_id('id_name')
        # TODO: self.assertEqual(input_name.get_attribute('placeholder'), 'Name of the Device')
        input_name.send_keys(device_name)
        input_name = self.browser.find_element_by_id('id_address')
        input_name.send_keys('1234')

        # Submit form to add device
        btn_submit = self.browser.find_element_by_css_selector('.btn-primary')
        btn_submit.click()

        # He notice the added device confirmation message
        self.check_notification_message("Device was added")

        # Operator goes to add var page
        # TODO: Use menu to find link?
        self.browser.get('%s/vars/add/' % self.live_server_url)
        self.check_page_title_and_header(title="Add Variable", header="Add Variable")

        # Breadcrumbs (Home > Mimics > Variable > Add new)
        breadcrumbs_item = self.browser.find_element_by_class_name('breadcrumb')
        breadcrumb_vars = breadcrumbs_item.find_element_by_link_text('Variables')
        self.assertTrue(breadcrumb_vars.get_attribute('href').endswith('/vars/'))
        breadcrumb_current_text = breadcrumbs_item.find_element_by_css_selector('li.active').text
        self.assertEqual("Add new", breadcrumb_current_text)

        # TODO: Pass following areas that an operator can view to other test
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
        # * History -> Add -> Chart
        # * History -> Manage -> Charts

        # Enter variable data
        var_name = 'Low Battery'
        input_name = self.browser.find_element_by_id('id_name')
        # TODO: self.assertEqual(input_name.get_attribute('placeholder'), 'Name of the variable')
        input_name.send_keys(var_name)
        select_type = self.browser.find_element_by_id('id_var_type')
        # TODO: check value is boolean
        select_device = self.browser.find_element_by_id('id_device')
        # TODO: check value is a valid device

        # Submit form to add var
        btn_submit = self.browser.find_element_by_css_selector('.btn-primary')
        btn_submit.click()

        # It is redirected to var list
        # Confirmation message is shown
        self.check_notification_message("Variable was added")

        # In the list appears new var added
        table = self.browser.find_element_by_class_name('table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any('var_name' in row.text for row in rows)
        )
        # Add new added variable to default view
        # Go to view
        # Then new variable is shown

        # Mimic window should have options to add/remove/reorder vars

        # Then default mimic page is shown and following elements appears in the content:
        self.fail('Finish this test!')

    def check_page_title_and_header(self, url=None, title=None, header=None):
        """Checks if a page have specified title and header.
        :param url: Relative path to page, with start and end sash if None use current page (default None)
        :param title: Text in browser title (default: None)
        :param header: Text in main page heading (default: None)
        """
        if url is not None:
            self.browser.get('%s%s' % (self.live_server_url, url))
        if title is not None:
            self.assertIn(title, self.browser.title)

        header_text = self.browser.find_element_by_id('header_text').text
        if header is not None:
            self.assertIn(header, header_text)

    def check_notification_message(self, message, tag='success'):
        var_added_confirmation = self.browser.find_element_by_class_name('alert')
        self.assertIn('alert-%s' % tag, var_added_confirmation.get_attribute('class'))
        self.assertIn(message, var_added_confirmation.text)