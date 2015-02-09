from selenium import webdriver
import unittest


class SupervisorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_view_mimics_and_charts(self):
        # A visitor go to ISU-SCADA homepage
        self.browser.get('http://localhost:8000')

        # Visitor notice page title and header mention "ISU-SCADA"
        self.assertIn("ISU-SCADA", self.browser.title)

        # A login form is shown
        # Since visitor have supervisor credentials he type it and proceed to log-in
        # TODO: Test login form

        # Then default mimic page is shown and following elements appears in the content:

        # Page title and header mention "Mimics"
        self.assertIn("Mimics", self.browser.title)
        header_text = self.browser.find_element_by_id('header_text').text
        self.assertIn("Mimics", header_text)

        # A welcome message and the operator's name
        welcome_text = self.browser.find_element_by_id('welcome').text
        self.assertEqual("Welcome Elpidio", welcome_text)

        # A device name day
        device_name = self.browser.find_elements_by_css_selector('.widget .title')[0].text
        self.assertEqual("Router", device_name)

        # A variable value indicator and variable's name
        var_item = self.browser.find_elements_by_css_selector('.widget .var')[0]
        self.assertEqual("ON", var_item.text)
        self.assertEqual("Working", var_item.get_attribute('title'))

        # A message with last update timestamp
        last_updated_text = self.browser.find_element_by_id('last_updated_notificaion').text
        self.assertIn("Last updated: ", last_updated_text)
        # TODO: Check for the time

        # Link to mimic page is active
        menu_active_text = self.browser.find_element_by_css_selector('nav li.active').text
        self.assertEqual("Mimics", menu_active_text)

        # A link to chart page
        menu_chart_link = self.browser.find_element_by_link_text('History charts')
        self.assertTrue(menu_chart_link.get_attribute('href').endswith('/history/'))

        # He notice last update timestamp changed every 3 seconds
        # Then he want to view the chart and click on the link
        # Page is updates with new elements:
        # Chart area is shown
        # An input box to enter a date
        # He notice data plotted in chart change on every update
        # He want to see yesterday chart and enter a date for yesterday in the input box and submit
        # Then Chart area is shown with new data
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()