import unittest
from models.function import insert_img
from models.driver import browser
from page_obj.dashBoardPage import DashBoard
from time import sleep
from page_obj.selectLivePage import SelectLive

class dashBoard(unittest.TestCase):
    """仪表盘页面"""
    def setUp(self):
        self.driver = browser()
        self.dashboard = DashBoard(self.driver)
        self.selectLive = SelectLive(self.driver)
        self.selectLive.enterMyPcHome()
    def tearDown(self):
        self.driver.quit()
    def test_switchLive(self):
        '''切换直播间'''
        self.dashboard.headHover()
        self.dashboard.switchLive()
        sleep(1)
        insert_img(self.driver,"3选择直播间.jpg")
        # 断言
        self.assertEqual(self.driver.title,"选择直播间")
    def test_loginOut(self):
        '''退出登录'''
        self.dashboard.headHover()
        self.dashboard.loginout()
        sleep(1)
        insert_img(self.driver,"4登录.jpg")
        # 断言
        self.assertEqual(self.driver.title,"千聊Live管理后台 - 登录")
    def test_copyUrl(self):
        '''复制链接'''
        self.dashboard.copyUrl()
        sleep(1)
        insert_img(self.driver,"5复制链接.jpg")
        # 断言
        # self.assertEqual(self.dashboard.copyUrlText(),"复制成功")
    def test_enterLive(self):
        '''进入直播间'''
        # 获取当前页面的handle
        nowhandle = self.driver.current_window_handle
        self.dashboard.enterLive()
        allhandles = self.driver.window_handles
        for i in allhandles:
            if i != nowhandle:
                self.driver.switch_to_window(i)
                insert_img(self.driver, "6直播间主页.jpg")
                title = self.driver.title
                # 断言
                self.assertEqual(title,"右右大号的直播间xwv6ne！@#￥%……&*（asdfas说法")


if __name__ == "__main__":
    unittest.main()