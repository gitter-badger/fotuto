from unittest import skip

from .base import FunctionalTest


class AssistantTest(FunctionalTest):
    @skip("skip assistant_can_view_mimics_and_charts")
    def test_assistant_can_view_mimics_and_charts(self):
        # A visitor go to Fotuto homepage
        self.browser.get(self.server_url)

        # Visitor notice page title and header mention "Fotuto"
        self.assertIn("Fotuto", self.browser.title)

        # A login form is shown
        # Since visitor have assistant credentials he type it and proceed to log-in
        # TODO: Test login form

        # Then default mimic page is shown

        # Page title and header mention "Mimics"
        # TODO: Complete this test
        self.check_page_title_and_header(title="Mimics", header="Mimics")

        # A welcome message and the operator's name
        welcome_text = self.browser.find_element_by_id('welcome').text
        self.assertEqual("Welcome Elpidio", welcome_text)

        # Menus displays options to view items
        # TODO: If there are more than 1 mimic window no submenu is shown, else list of windows is shown, the same for
        # History Charts

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
        # TODO: Finish the test!