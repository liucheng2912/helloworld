from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import pytest
from time import sleep

from selenium.webdriver.common.keys import Keys


class TestClick:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()


    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element(By.XPATH,'//input[@value="click me"]')
        element_rightclick = self.driver.find_element(By.XPATH,'//input[@value="right click me"]')
        element_doubleclick = self.driver.find_element(By.XPATH,'//input[@value="dbl click me"]')

        action=ActionChains(self.driver)
        action.click(element_click)
        action.context_click(element_rightclick)
        action.double_click(element_doubleclick)
        sleep(3)
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_moveto(self):
        self.driver.get("https://www.baidu.com/")
        ele = self.driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_drag(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        ele1 = self.driver.find_element_by_id("dragger")
        ele2 = self.driver.find_element_by_xpath("/html/body/div[2]")
        action = ActionChains(self.driver)
        action.drag_and_drop(ele1,ele2)
        action.perform()
        sleep(3)

    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele = self.driver.find_element_by_xpath("/html/body/label[1]/input")

        action = ActionChains(self.driver)
        action.click(ele)
        action.send_keys("username")
        action.send_keys(Keys.SPACE).pause(2)
        action.send_keys("tom").pause(2)
        action.send_keys(Keys.BACK_SPACE).pause(2)
        action.perform()
        sleep(2)

if __name__ == '__main__':
    pytest.main(["-v","-s"],TestClick)


