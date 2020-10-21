from 学习.selenium.Base import Base
from time import sleep

class TestWindow(Base):
    def test_window(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_xpath('//*[@id="u1"]/a').click()
        self.driver.find_element_by_xpath('//*[@id="passport-login-pop-dialog"]/div/div/div/div[3]/a').click()
        # print(self.driver.current_window_handle)
        window = self.driver.window_handles
        self.driver.switch_to_window(window[-1])
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("username")

        self.driver.switch_to_window(window[0])
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__footerULoginBtn"]').click()
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__userName"]').send_keys("username")
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__password"]').send_keys("password")
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__submit"]').click()
