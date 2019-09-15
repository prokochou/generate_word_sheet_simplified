
import __init__
from Constants import TT_Constants
from BestTestCase import BestTestCase
from pages.BasePage import BasePage
from pages.MainPage import MainPage
import time
import unittest
import nose
from nose.plugins.attrib import attr


class NewWordInput(unittest.TestCase):

    def setUp(self):
        super(NewWordInput, self).setUp()
        BestTestCase.setup(self)
        # BestTestCase.navigate_to_page(self, TT_Constants["Base_URL"])

    @attr(priority="high")
    def test_input(self):
        # Enable flash
        BestTestCase.navigate_to_page(self, TT_Constants["Flash_URL"])
        MainPage._allow_flash(self)

        # Open file
        f = open("../word.txt", "r")
        word = f.read()

        # Go to Chinese input website
        BestTestCase.navigate_to_page(self, TT_Constants["Base_URL"])
        input_word = word
        input_ls = MainPage._handle_input(self, input_word)

        for i in range(len(input_ls)):
            MainPage._input_new_word(self, input_ls[i])
            MainPage._customize_click(self)
            MainPage._input_line_no(self)

            #TODO: Download files automatically (Flash content)
            # filename = "screenshot/image_" + BasePage.timestamp(self) + ".png"
            # BasePage.screenshot(self, filename)
            # MainPage._save_to_pdf(self)

            # # Go back to previous main page TODO:判斷是否有page2
            BasePage.goback_to_previous_window(self)

            # Clear inputted words
            MainPage._clear_inputted_words(self)

        # Download Manually
        time.sleep(2000)

    def tearDown(self):
        BestTestCase.tearDown(self)


if __name__ == '__main__':
    nose.main()
