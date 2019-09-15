from selenium import webdriver
from Constants import TT_Constants


class BestTestCase(object):

    def setup(self):

        if TT_Constants["Browser"] == 'firefox':
            self.driver = webdriver.Firefox()
            self.driver.maximize.window()
        elif TT_Constants["Browser"] == 'chrome':
            # Allow flash in chrome
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--disable-features=EnableEphemeralFlashPermission")

            chrome_prefs = {"profile.default_content_setting_values.plugins": 1,
                            "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
                            "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,
                            "PluginsAllowedForUrls": "http://cn.yes-chinese.com/zh-cn/tzg/view.jsp"}

            chrome_options.add_experimental_option("prefs", chrome_prefs)

            self.driver = webdriver.Chrome(chrome_options=chrome_options, service_log_path='NUL')

        # self.driver.maximize.window()
        elif TT_Constants["Browser"] == 'ie':
            self.driver = webdriver.Ie()
            self.driver.maximize.window()
        else:
            raise Exception("This browser is not supported at the moment.")

    def navigate_to_page(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def tearDown(self):
        self.driver.quit()
