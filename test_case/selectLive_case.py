import unittest
from models.function import insert_img
from models.driver import browser
from page_obj.selectLivePage import SelectLive
from time import sleep

class selectLiveTest(unittest.TestCase):
    """请选择要登录的直播间页面"""
    def setUp(self):
        self.driver = browser()
        self.sectLive = SelectLive(self.driver)
    def tearDown(self):
        self.driver.quit()
    def test1(self):
        '''进入我的pc管理后台主页'''
        self.sectLive.enterMyPcHome()
        sleep(1)
        insert_img(self.driver,'1我的直播间仪表盘首页.jpg')
        # 断言
        self.assertEqual(self.driver.current_url,"https://m.qlchat.com/video/admin/live/home?liveId=310000108181722")
    def test2(self):
        '''进入我管理的pc管理后台主页'''
        self.sectLive.enterManagePcHome()
        sleep(1)
        insert_img(self.driver,'2管理直播间仪表盘首页.jpg')
        # 断言
        self.assertEqual(self.driver.current_url,"https://m.qlchat.com/video/admin/live/home?liveId=210000381076170")
if __name__ == "__main__":
    unittest.main()