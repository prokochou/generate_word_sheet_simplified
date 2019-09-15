from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from abc import abstractmethod
from Constants import LocatorMode
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import gmtime, strftime



class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self._verify_page()

    @abstractmethod
    def _verify_page(self):
        """This method verifies that we are con the correct page."""

    def wait_for_element_visibility(self, waitTime, locatorMode, Locator):
        element = None
        if locatorMode == LocatorMode.ID:
            element = WebDriverWait(self.driver, waitTime). \
                until(EC.visibility_of_element_located((By.ID, Locator)))
        elif locatorMode == LocatorMode.NAME:
            element = WebDriverWait(self.driver, waitTime). \
                until(EC.visibility_of_element_located((By.NAME, Locator)))
        elif locatorMode == LocatorMode.XPATH:
            element = WebDriverWait(self.driver, waitTime). \
                until(EC.visibility_of_element_located((By.XPATH, Locator)))
        elif locatorMode == LocatorMode.CSS_SELECTOR:
            element = WebDriverWait(self.driver, waitTime). \
                until(EC.visibility_of_element_located((By.CSS_SELECTOR, Locator)))
        else:
            raise Exception("Unsupported locator strategy.")
        return element

    def wait_until_element_clickable(self, waitTime, locatorMode, Locator):
        element = None
        if locatorMode == LocatorMode.ID:
            element = WebDriverWait(self.driver, waitTime). \
                until(EC.element_to_be_clickable((By.ID, Locator)))
        elif locatorMode == LocatorMode.NAME:
            element = WebDriverWait(self.driver, waitTime). \
                until(EC.element_to_be_clickable((By.NAME, Locator)))
        elif locatorMode == LocatorMode.XPATH:
            element = WebDriverWait(self.driver, waitTime). \
                until(EC.element_to_be_clickable((By.XPATH, Locator)))
        elif locatorMode == LocatorMode.CSS_SELECTOR:
            element = WebDriverWait(self.driver, waitTime). \
                until(EC.element_to_be_clickable((By.CSS_SELECTOR, Locator)))
        else:
            raise Exception("Unsupported locator strategy.")
        return element

    def switch_to_window(self):
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)

    def goback_to_previous_window(self):
        window_before = self.driver.window_handles[0]
        self.driver.switch_to.window(window_before)

    def find_element(self, locatorMode, Locator):
        element = None
        if locatorMode == LocatorMode.ID:
            element = self.driver.find_element_by_id(Locator)
        elif locatorMode == LocatorMode.NAME:
            element = self.driver.find_element_by_name(Locator)
        elif locatorMode == LocatorMode.XPATH:
            element = self.driver.find_element_by_xpath(Locator)
        elif locatorMode == LocatorMode.CSS_SELECTOR:
            element = self.driver.find_element_by_css_selector(Locator)
        else:
            raise Exception("Unsupported locator strategy.")
        return element

    def fill_out_field(self, locatorMode, Locator, text):
        self.find_element(locatorMode, Locator).clear()
        self.find_element(locatorMode, Locator).send_keys(text)

    def click(self, waitTime, locatorMode, Locator):
        self.wait_until_element_clickable(waitTime, locatorMode, Locator).click()

    def accept_alert(self):
        action = ActionChains(self.driver)
        action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

    def screenshot(self, filename):
        self.driver.save_screenshot(filename)

    def timestamp(self):
        return strftime("%Y-%m-%d %H:%M:%S", gmtime())



class IncorrectPageExpection(Exception):
    """ The expection should be thrown when the page cannot be displayed. """
