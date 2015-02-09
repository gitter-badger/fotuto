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
        self.fail('Finish the test!')

        # A login form is shown
        # Since visitor have supervisor credentials he type it and proceed to log-in
        # Then default mimic page is shown and following elements appears in the content:
        # Title page mention "Mimics"
        # A welcome message and the operator's name
        # A device name day
        # A variable value indicator and variable's name
        # A message with last update timestamp
        # A link to chart page
        # He notice last update timestamp changed every 3 seconds
        # Then he want to view the chart and click on the link
        # Page is updates with new elements:
        # Chart area is shown
        # An input box to enter a date
        # He notice data plotted in chart change on every update
        # He want to see yesterday chart and enter a date for yesterday in the input box and submit
        # Then Chart area is shown with new data

if __name__ == '__main__':
    unittest.main()