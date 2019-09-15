from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from Constants import LocatorMode
from .BasePage import BasePage
from UIMap import HomePageMap
import time



class MainPage(object):

    def __init__(self, driver):
        super(MainPage, self).__init__(driver)

    def _input_new_word(self, input):
        input_element = BasePage.find_element(self, "xpath", HomePageMap['InputXpath'])
        input_element.click()
        action = ActionChains(self.driver)
        action.send_keys_to_element(input_element, input)
        action.perform()

    def _customize_click(self):
        line_element = BasePage.find_element(self, "xpath", HomePageMap['CustomizeXpath'])
        line_element.click()

    def _input_line_no(self):
        no = 1
        input_bn = BasePage.find_element(self, "cssSelector", HomePageMap['LineCSS'])
        BasePage.accept_alert(self)
        input_bn.click()
        input_bn.clear()

        # Accept the alert
        BasePage.accept_alert(self)

        #Input line number and enter
        action = ActionChains(self.driver)
        action.send_keys_to_element(input_bn, no)
        action.key_down(Keys.ENTER).key_up(Keys.ENTER)
        action.perform()

    def _handle_input(self, input):

        # input_list
        input_ls = []

        # Make input become a list, 4 words as an element
        # input = "一二三四五六七八酒三田醫生媽媽爸爸哥哥姊姊" // Test file

        four_word = ""
        for i in range(0, len(input), 4):
            four_word += input[i:i+4]
            input_ls.append(four_word)
            four_word = ""
        return input_ls

    def _clear_inputted_words(self):
        input_element = BasePage.find_element(self, "xpath", HomePageMap['InputXpath'])
        input_element.clear()

    def _allow_flash(self):
        # Solution: https://stackoverflow.com/questions/51967309/activate-flash-in-chrome-selenium-with-python?rq=1
        actions = ActionChains(self.driver)
        actions = actions.send_keys(Keys.TAB * 21)
        actions = actions.send_keys(Keys.SPACE)
        actions = actions.send_keys("a")
        actions = actions.send_keys(Keys.ENTER)
        actions.perform()

    def _save_to_pdf(self):
        # This is workaround method since it is difficult to click the print button in flash content.
        actions = ActionChains(self.driver)

        # Right Click
        actions = actions.move_by_offset(219, 60)
        actions = actions.context_click()
        time.sleep(5)
        actions = actions.context_click()
        # self.driver.execute_script("document.getElementById('flash').click();")

        # Click print button by arrow Down button 4 times
        actions = actions.send_keys(Keys.ARROW_DOWN)
        actions = actions.send_keys(Keys.ARROW_DOWN)
        actions = actions.send_keys(Keys.ARROW_DOWN)
        actions = actions.send_keys(Keys.ARROW_DOWN)
        actions = actions.send_keys(Keys.ARROW_DOWN)
        actions = actions.send_keys(Keys.ENTER)
        #
        # # Focus on Save Destination by TAB once
        # actions = actions.send_keys(Keys.TAB)
        #
        # # Save to PDF
        # actions = actions.send_keys("s")
        #
        # # Press Save button by mouse click once + TAB twice
        # actions = actions.context_click()
        # actions = actions.send_keys(Keys.TAB)

        actions.perform()





