from 学习.selenium.Base import Base
from time import sleep
import pytest
class TestJS(Base):
    @pytest.mark.skip
    def test_time(self):
        self.driver.get("https://www.12306.cn/index/")
        print(self.driver.execute_script("return document.getElementById('train_date').value"))
        sleep(5)
        date_js = "document.getElementById('train_date').removeAttribute('readonly')"
        self.driver.execute_script(date_js)
        sleep(2)
        date_js1 = "document.getElementById('train_date').value='2019-01-01'"
        self.driver.execute_script(date_js1)
        sleep(5)
        print(self.driver.find_element_by_id("train_date").text)

    def test_scroll(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.execute_script("document.getElementById('su').click()")
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        self.driver.find_element_by_xpath('//*[@id="page"]/div/a[10]').click()
        sleep(5)