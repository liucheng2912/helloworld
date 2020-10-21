from selenium import webdriver
from time import sleep
class Test1():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # 隐式等待 5s之内对元素查找 轮询查找（默认0.5秒）元素是否出现  全局设置
        self.driver.implicitly_wait(5)
        # 直接等待  time.sleep(3)  强制等待 线程休眠一定时间
        # 显示等待  代码中定义等待条件，条件发生时才继续执行代码
            # WebDriveWait 配置unitl() 和until not() 方法，根据判断条件进行等待
            # 程序每隔一段时间（默认0.5秒）进行条件判断，如果条件成立，则执行下步，否则继续等待，直到超过设置的最长时间

    def teardown(self):
        self.driver.quit()

    def test_1(self):
        self.driver.get("https://testerhome.com")
        self.driver.find_element_by_link_text("社团").click()

