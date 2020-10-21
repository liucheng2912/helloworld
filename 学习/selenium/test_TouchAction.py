from selenium import webdriver
from selenium.webdriver import TouchActions
from time import sleep


class TestTouchActon:
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c',False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_touch(self):
        self.driver.get("http://www.baidu.com")
        ele = self.driver.find_element_by_id("kw")
        ele2= self.driver.find_element_by_id("su")
        ele.send_keys("test")

        action = TouchActions(self.driver)
        action.tap(ele2)
        action.perform()
        sleep(3)

        action.scroll_from_element(ele,0,10000)
        action.perform()
        sleep(3)