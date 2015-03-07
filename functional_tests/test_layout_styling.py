from .base import FunctionalTest


class LayoutAndStylingTest(FunctionalTest):
    def test_layout_and_styling(self):
        # For a simple layout and styling test check user area is near to top right corner
        # Visitor goes to the home page
        self.browser.get(self.server_url)
        # He notice user area is at top right
        user_area = self.browser.find_element_by_id('welcome')
        self.assertAlmostEqual(user_area.location['y'], 0, delta=20)