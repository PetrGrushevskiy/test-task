class Wizard:

    def __init__(self, app):
        self.app = app

    def skip_wizard(self):
        driver = self.app.driver
        driver.find_element_by_class_name("skip").click()
