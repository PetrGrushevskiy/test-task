import names


class Account:

    def __init__(self, app):
        self.app = app

    def update_account(self, first_name=None, last_name=None):
        driver = self.app.driver
        driver.find_element_by_id("firstName").clear()
        driver.find_element_by_id("firstName").send_keys(f"{first_name if first_name else names.get_first_name()}")
        driver.find_element_by_id("lastName").clear()
        driver.find_element_by_id("lastName").send_keys(f"{last_name if last_name else names.get_last_name()}")
        driver.find_element_by_xpath("//div[@id='kc-form-buttons']/div/button[text()='Save']").click()
