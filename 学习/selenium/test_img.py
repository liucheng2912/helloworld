from 学习.selenium.Base import Base
from time import sleep

class TestImg(Base):
    def test_img(self):
        self.driver.get("https://image.baidu.com")
        self.driver.find_element_by_xpath('//*[@id="sttb"]/img[1]').click()
        self.driver.find_element_by_xpath('//*[@id="stfile"]').send_keys('E:\\work\\helloworld\\1.jpg')
        sleep(10)
