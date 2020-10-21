from selenium import webdriver
import pytest
import os
# 调用的时候,命令行  browser=chrome pytest base.py
class Base():
    def setup(self):
        browser = os.getenv("browser")
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'headless':
            self.driver = webdriver.phantomjs
        else:
            self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    @pytest.mark.skip
    def teardown(self):
        self.driver.quit()