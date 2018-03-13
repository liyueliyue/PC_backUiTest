import sys
sys.path.append('./page_obj')
from page_obj.base import Page
from selenium.webdriver.common.by import By
class SelectLive(Page):
    '''选择需要登录的直播间页面类'''
    myLive_loc = (By.XPATH,".//*[@id='app']/div/div[1]/div[2]/div/div/div[1]/div/div/div")
    manage_loc = (By.XPATH,".//*[@id='app']/div/div[1]/div[2]/div/div/div[2]/div/div")

    # 进入我的pc管理后台页面方法
    def enterMyPcHome(self):
        self.openPc()
        self.wait_element(*self.myLive_loc).click()
    # 进入我管理的PC管理后台页面
    def enterManagePcHome(self):
        self.openPc()
        self.wait_element(*self.manage_loc).click()
