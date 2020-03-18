class DashBoard:

    def __init__(self, app):
        self.app = app

    def open_personal_settings(self):
        driver = self.app.driver
        root = driver.find_element_by_tag_name("bzm-header")
        shadow_root = self.app.expand_shadow_element(root)

        shadow_root.find_element_by_css_selector("div.dropdown-toggle").click()
        shadow_root.find_element_by_css_selector("a.dropdown-menu-item").click()
