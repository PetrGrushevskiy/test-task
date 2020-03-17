class BasePage:

    def __init__(self, app):
        self.app = app

    def open_base_page(self):
        driver = self.app.driver
        driver.get("https://www.www-bm-qa-base.blazemeter.net/")

    def click_on_get_started(self):
        driver = self.app.driver
        driver.find_element_by_class_name("get_started_button").click()
        assert driver.title == "Register | Blazemeter", "Register page didn't open"
