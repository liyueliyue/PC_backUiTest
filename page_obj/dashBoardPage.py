import sys
sys.path.append('./page_obj')
from page_obj.base import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class DashBoard(Page):
    '''仪表盘页面类'''
    hover_loc = (By.XPATH,".//*[@id='app']/div/div[1]/div/div[1]/div/div/div/a")
    switchLive_loc = (By.XPATH,"html/body/div[2]/div/div/ul/li[3]/a")
    loginout_loc = (By.XPATH,"html/body/div[2]/div/div/ul/li[4]/a")
    copyUrl_loc = (By.XPATH,".//*[@id='app']/div/div[1]/div/div[2]/div/div[2]/div[2]/header/ul/li[3]/span")
    copyUrlText_loc = (By.XPATH,"html/body/div[3]/div/span/div/div/div/span")
    enterLive_loc = (By.XPATH,".//*[@id='app']/div/div[1]/div/div[2]/div/div[2]/div[2]/header/ul/li[3]/a[2]")
# 左边标签栏
    # 课程列表
    courseList_loc = (By.XPATH,".//*[@id='app']/div/div[1]/div/div[2]/div/div[1]/div/ul/li[2]/div")
    # 单课列表
    topicList_loc = (By.XPATH,".//*[@id='/course-list$Menu']/li[1]/a")
    # 系列课列表
    channelList_loc = (By.XPATH,".//*[@id='/course-list$Menu']/li[2]/a")
    # 打卡训练营列表
    campList_loc = (By.XPATH,".//*[@id='/course-list$Menu']/li[3]/a")



    # 头像hover
    def headHover(self):
        loc = self.wait_element(*self.hover_loc)
        return ActionChains(self.driver).move_to_element(loc).perform()
    # 切换直播间
    def switchLive(self):
        self.headHover()
        return self.wait_element(*self.switchLive_loc).click()
    # 退出登录
    def loginout(self):
        self.headHover()
        return self.wait_element(*self.loginout_loc).click()
    # 复制链接
    def copyUrl(self):
        return self.wait_element(*self.copyUrl_loc).click()
    # 复制链接提示成功文案
    def copyUrlText(self):
        return self.wait_element(*self.copyUrlText_loc).text
    # 进入直播间
    def enterLive(self):
        return self.wait_element(*self.enterLive_loc).click()

# 课程列表
    def courseList(self):
        return self.wait_element(*self.courseList_loc).click()
    # 进入单课列表
    def topicList(self):
        self.courseList()
        sleep(1)
        return ActionChains(self.driver).click(self.wait_element(*self.topicList_loc).click()).perform()
    # 进入系列课列表
    def channelList(self):
        self.courseList()
        sleep(1)
        return ActionChains(self.driver).click(self.wait_element(*self.channelList_loc).click()).perform()

    # 进入打卡训练营列表
    def campList(self):
        self.courseList()
        sleep(1)
        return ActionChains(self.driver).click(self.wait_element(*self.campList_loc).click()).perform()
