from selenium import webdriver
import unittest


class SupervisorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_visitors_cant_view_login_form_only(self):
        self.fail('Create this test!')

    def test_supervisor_can_view_mimics_and_charts(self):
        # A visitor go to ISU-SCADA homepage
        self.browser.get('http://localhost:8000')

        # Visitor notice page title and header mention "ISU-SCADA"
        self.assertIn("ISU-SCADA", self.browser.title)

        # A login form is shown
        # Since visitor have supervisor credentials he type it and proceed to log-in
        # TODO: Test login form

        # Then default mimic page is shown

        # Page title and header mention "Mimics"
        self.assertIn("Mimics", self.browser.title)
        header_text = self.browser.find_element_by_id('header_text').text
        self.assertIn("Mimics", header_text)

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
        self.browser.get('http://localhost:8000/vars/add/')

        # A login form is shown
        # Operator type his credential and proceed to log-in
        # TODO: Test login form

        # Operator is redirected to add var page
        self.assertIn("Add Variable", self.browser.title)
        header_text = self.browser.find_element_by_id('header_text').text
        self.assertIn("Add Variable", header_text)

        # Breadcrumbs (Home > Mimics > Variable > Add new)
        breadcrumbs_item = self.browser.find_element_by_class_name('breadcrumb')
        breadcrumb_vars = breadcrumbs_item.find_element_by_link_text('Variables')
        self.assertTrue(breadcrumb_vars.get_attribute('href').endswith('/vars/'))
        breadcrumb_current_text = breadcrumbs_item.find_element_by_css_selector('li.active').text
        self.assertEqual("Add new", breadcrumb_current_text)

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

        # It is redirected to vars list
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

if __name__ == '__main__':
    unittest.main()