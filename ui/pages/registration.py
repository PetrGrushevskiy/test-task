import names
import time


class Registration:

    def __init__(self, app):
        self.app = app

    def register_new_user(self, first_name=None, last_name=None, email=None, company=None):
        driver = self.app.driver
        driver.find_element_by_id("firstName").send_keys(f"{first_name if first_name else names.get_first_name()}")
        driver.find_element_by_id("lastName").send_keys(f"{last_name if last_name else names.get_last_name()}")
        driver.find_element_by_id("email").send_keys(
            f"{email if email else f'peter.hrushevski+{int(time.time())}@blazemeter.com'}")
        driver.find_element_by_id("user.attributes.company").send_keys(f"{company if company else 'Test'}")
        driver.find_element_by_xpath("//div[@id='kc-form-buttons']//input[@type='submit']").click()

        self.app.wait_until_title_is("Welcome Wizard")
        assert driver.current_url.endswith("/welcome-wizard/http")
