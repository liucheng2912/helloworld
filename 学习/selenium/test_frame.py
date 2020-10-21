from 学习.selenium.Base import Base

class TestFrame(Base):
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        # 切换到frame 括号内是frame的id
        # self.driver.switch_to.frame("iframeResult")
        self.driver.switch_to_frame("iframeResult")
        print(self.driver.find_element_by_id("draggable"))
        # 切换回frame的上一级
        self.driver.switch_to.parent_frame()
        # 切换回默认的布局
        # self.driver.switch_to.default_content()
        print(self.driver.find_element_by_id("submitBTN"))