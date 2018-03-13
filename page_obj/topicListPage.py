import sys,time
sys.path.append('./page_object')
from page_obj.base import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class TopicList(Page):
    """单课列表页面类"""
    # 单课列表面包屑
    topicTitle_loc = (By.XPATH,".//*[@id='app']/div/div[1]/div/div[2]/div/div[2]/div[1]/span[2]/span[1]/a")
    # 新建单课按钮
    createTopicButton_loc = (By.XPATH,".//*[@id='app']/div/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/button")
# 选择单课类型
    audioAndVideoGra_loc = (By.XPATH,".//*[@id='app']/div/div[1]/div/div[2]/div/div[2]/div[2]/section[1]/a")
    lectureTopic_loc = (By.XPATH,".//*[@id='app']/div/div[1]/div/div[2]/div/div[2]/div[2]/section[2]/a")
    pptTopic_loc = (By.XPATH,".//*[@id='app']/div/div[1]/div/div[2]/div/div[2]/div[2]/section[3]/a")
    audioAndVideoTopic_loc = (By.XPATH,".//*[@id='app']/div/div[1]/div/div[2]/div/div[2]/div[2]/section[4]/a")
# 新建讲座直播话题页面
    topicName_loc = (By.ID,"topic-title-edit")
    startTime_loc = (By.XPATH,"html/body/div[1]/div[1]/ul[1]/li[2]/span/input")
    # 时间控件弹窗
    timeControlWindow_loc = (By.XPATH,"/html/body/div[7]/div/div[2]")
    ensureStartTime_loc = (By.XPATH,"/html/body/div[7]/div/div[2]/div/div[4]/div[2]/div")
    nextStep_loc = (By.XPATH,"/html/body/div[1]/div[1]/div/a")
    openIntroduction_loc = (By.XPATH,"/html/body/div[1]/div[2]/dl/dd/div[1]/div/span[1]/span")
    finishTopicButton_loc = (By.XPATH,"/html/body/div[1]/div[2]/div/a[2]")
    # 加密话题
    encryptTopic_loc = (By.XPATH,"/html/body/div[1]/div[2]/dl/dt/span[2]")
    pwdText_loc = (By.XPATH,"/html/body/div[1]/div[2]/dl/dd/div[2]/div/input")
    # 收费话题
    chargeTopic_loc = (By.NAME,"password_ticket")
    priceText_loc = (By.XPATH,"/html/body/div[1]/div[2]/dl/dd/div[3]/div/div[1]/span[2]/input")
    openAutoDistributeButton_loc = (By.XPATH,"/html/body/div[1]/div[2]/dl/dd/div[3]/div/span/span")
    distributePer_loc = (By.XPATH,"/html/body/div[1]/div[2]/dl/dd/div[3]/div/div[2]/span[2]/input")


    #获取单课列表面包屑text
    def getTopicTitleText(self):
        return self.wait_element(*self.topicTitle_loc).text
    # 新建讲座直播话题
    def createLectureTopic(self,topicname):
        self.wait_element(*self.createTopicButton_loc).click()
        nowHandle = self.driver.current_window_handle
        self.wait_element(*self.lectureTopic_loc).click()
        allHandles = self.driver.window_handles
        for i in allHandles:
            if i != nowHandle:
                self.driver.switch_to.window(i)
                # 课程主题
                text = str(topicname)+str(time.time())
                # js = "var sum=document.get_element_by_id('topic-title-edit');sum.value='" + text + "';"
                # self.execute_js(src=js)
                self.wait_element(*self.topicName_loc).send_keys(text)
                # 开始时间，鼠标左键单击操作
                time.sleep(1)
                ActionChains(self.driver).click(self.wait_element(*self.startTime_loc)).perform()
                # 处理弹窗,当弹窗可见后，执行选择时间操作
                while self.wait_element(*self.timeControlWindow_loc).is_displayed():
                    time.sleep(1)
                    self.wait_element(*self.ensureStartTime_loc).click()
                    time.sleep(1)
                    break
                # 下一步
                return self.wait_element(*self.nextStep_loc).click()
    # 新建讲座直播话题-免费
    def createLectureTopicFree(self):
        self.createLectureTopic(topicname="讲座直播话题-免费")
        # 开启介绍页说明
        self.wait_element(*self.openIntroduction_loc).click()
        # 点击完成按钮
        self.wait_element(*self.finishTopicButton_loc).click()

    # 新建讲座直播话题-加密
    def createLectureTopicEncrypted(self):
        self.createLectureTopic(topicname="讲座直播话题-加密")
        # 选择加密话题
        self.wait_element(*self.encryptTopic_loc).click()
        # 输入密码
        self.wait_element(*self.pwdText_loc).send_keys("123456")
        # 完成
        self.wait_element(*self.finishTopicButton_loc).click()
    # 新建讲座直播话题-收费
    def createLectureTopicCharge(self):
        self.createLectureTopic(topicname="讲座直播话题-收费")
        # 选择收费话题
        self.wait_element(*self.chargeTopic_loc).click()
        # 输入话题价格
        self.wait_element(*self.priceText_loc).send_keys("1")
        # 开启自动分销
        self.wait_element(*self.openAutoDistributeButton_loc).click()
        #输入自动分销比例
        self.wait_element(*self.distributePer_loc).send_keys(10)
        self.wait_element(*self.finishTopicButton_loc).click()