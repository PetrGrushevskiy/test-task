from ui.pages.base_page import BasePage
from ui.pages.registration import Registration
from ui.pages.wizard import Wizard
from ui.pages.dashboard import DashBoard
from ui.pages.account import Account

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.base_page = BasePage(self)
        self.registration = Registration(self)
        self.wizard = Wizard(self)
        self.dashboard = DashBoard(self)
        self.account = Account(self)

    def wait_until_title_is(self, title: str = None):
        WebDriverWait(self.driver, 60).until(EC.title_is(title))

    def expand_shadow_element(self, el):
        shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', el)
        return shadow_root
