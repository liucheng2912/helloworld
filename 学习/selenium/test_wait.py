from selenium import webdriver
from time import sleep

from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://www.baidu.com")
        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_wait1(self):
        # self.driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys("霍格沃茨测试学院")
        # self.driver.find_element(By.ID, 'kw').send_keys("霍格沃茨测试学院")
        self.driver.find_element(By.CSS_SELECTOR, '#kw').send_keys("霍格沃茨测试学院")
        self.driver.find_element(By.ID, 'su').click()


    # def test_wait(self):
    #     self.driver.find_element(by.XPAHT,'//*[@title="归入各种类别的所有主题"]')
    #     sleep(3)
    #     print("hello")
    #     # 显示等待
    #     def wait(x):
    #         return len(self.driver.find_elements(By.XPATH,'//*[@class=table-heading"]')) >=1
    #     WebDriverWait(self.driver,10).until(wait).click()
    #     # 是否可以点击
    #     WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(By.XPATH,'class=table-heading"')).click()
