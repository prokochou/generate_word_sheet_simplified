# from selenium import webdriver
# import time
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# from nose.plugins.attrib import attr

# driver = webdriver.Chrome()
#
# driver.get("http://google.com")
# # driver.execute_script("window.alert('This is alert');")
# time.sleep(1)
#
# action = ActionChains(driver)
# action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
# time.sleep(1)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("chrome://settings/content/siteDetails?site=http://cn.yes-chinese.com/zh-cn/tzg/view.jsp")

actions = ActionChains(driver)
actions = actions.send_keys(Keys.TAB * 25)
actions = actions.send_keys(Keys.SPACE)
actions = actions.send_keys("a")
actions = actions.send_keys(Keys.ENTER)
time.sleep(5)
actions.perform()




driver.quit()