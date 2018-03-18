import sys,time
sys.path.append('./page_object')
from page_obj.base import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from models.dataFile import getDataFile

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
    # 新建讲座直播话题页面###########
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

    # 创建音视频录播课程
    audioAndVideoGraTopicname_loc = (By.XPATH,".//*[@id='app']/div/div[1]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[2]/div/input")
    # 课程封面
    topicPic_loc = (By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div/div[2]/div[2]/form/div[2]/div[2]/div/span[2]/div/div/input[1]')
    videoGra_loc = (By.XPATH,".//*[@id='app']/div/div[1]/div/div[2]/div/div[2]/div[2]/form/div[3]/div[2]/div/div/label[1]")
    audioGra_loc = (By.XPATH,".//*[@id='app']/div/div[1]/div/div[2]/div/div[2]/div[2]/form/div[3]/div[2]/div/div/label[2]")
    channelbutton_loc = (By.XPATH,".//*[@id='app']/div/div[1]/div/div[2]/div/div[2]/div[2]/form/div[4]/div[2]/div/div[1]/label[1]")
    campleButton_loc = (By.XPATH,".//*[@id='app']/div/div[1]/div/div[2]/div/div[2]/div[2]/form/div[4]/div[2]/div/div[1]/label[2]")
    channelSelectbutton_loc = (By.XPATH,".//*[@id='from-channel']/div/div/div/div[1]")
    campleSelectButton_loc = (By.XPATH,".//*[@id='from-camp']/div/div/div/div[1]")
    channell_loc = (By.XPATH,".//*[@id='from-channel']/div[2]/div/div/div/ul/li[1]")
    campe_loc = (By.XPATH,".//*[@id='from-camp']/div[2]/div/div/div/ul/li[1]")
    singleSoleInChannel_loc = (By.XPATH,".//*[@id='from-channel']/label/span[1]/input")
    singleSolePrice_loc = (By.XPATH,".//*[@id='app']/div/div[1]/div/div[2]/div/div[2]/div[2]/form/div[4]/div[2]/div/div[3]/span/span/input")
    # 添加图片按钮
    liveIntroPictureButton_loc = (By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div/div[2]/div[2]/form/div[5]/div[2]/div/div[1]/div/input[1]')
    liveIntroTextButton_loc = (By.XPATH,".//*[@id='app']/div/div[1]/div/div[2]/div/div[2]/div[2]/form/div[5]/div[2]/div/div[2]")
    liveIntroText_loc = (By.XPATH,".//*[@id='app']/div/div[1]/div/div[2]/div/div[2]/div[2]/form/div[5]/div[2]/div/section/div/textarea")
    liveIntroPicButton_loc = (By.XPATH,".//*[@id='app']/div/div[1]/div/div[2]/div/div[2]/div[2]/form/div[5]/div[2]/div/div[1]/div/input[1]")
    saveButton_loc = (By.XPATH,".//*[@id='app']/div/div[1]/div/div[2]/div/div[2]/div[2]/form/div[6]/div/div/button")
    # 上传视频按钮
    sendVideoButton_loc = (By.XPATH,'//*[@id="uploader"]/div/input[1]')
    # 保存视频图文创建
    saveVideoGra_loc = (By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div/div[2]/div[2]/form/div[6]/div/div/button')
    # 上传成功，是否去往系列课话题列表页按钮
    backTopicListButton_loc = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[2]/button[2]")

# 创建音视频互动话题
    # 课程主题
    videoTopicName_loc = (By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[2]/div/input')
    # 课程封面
    videoTopic_loc = (By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div/div[2]/div[2]/form/div[2]/div[2]/div/span[2]/div/div/input[1]')
    # 直播类型
    video_loc = (By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div/div[2]/div[2]/form/div[3]/div[2]/div/div[1]/label[1]')
    # 直播时间

    #获取单课列表面包屑text
    def getTopicTitleText(self):
        return self.wait_element(*self.topicTitle_loc).text
    # ######################新建讲座直播话题##############################
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

    # ###########################新建幻灯片直播话题################################
    def createPptTopic(self,topicName):
        self.wait_element(*self.createTopicButton_loc).click()
        nowHandle = self.driver.current_window_handle
        self.wait_element(*self.pptTopic_loc).click()
        allHandles = self.driver.window_handles
        for i in allHandles:
            if i != nowHandle:
                self.driver.switch_to.window(i)
                # 课程主题
                text = str(topicName)+str(time.time())
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
    def createPptTopicFree(self):
        self.createPptTopic(topicName="幻灯片直播话题-免费")
        # 开启介绍页说明
        self.wait_element(*self.openIntroduction_loc).click()
        # 点击完成按钮
        self.wait_element(*self.finishTopicButton_loc).click()
    # 新建讲座直播话题-加密
    def createPptTopicEncrypted(self):
        self.createPptTopic(topicName="幻灯片直播话题-加密")
        # 选择加密话题
        self.wait_element(*self.encryptTopic_loc).click()
        # 输入密码
        self.wait_element(*self.pwdText_loc).send_keys("123456")
        # 完成
        self.wait_element(*self.finishTopicButton_loc).click()
    # 新建讲座直播话题-收费
    def createPptTopicCharge(self):
        self.createPptTopic(topicName="幻灯片直播话题-收费")
        # 选择收费话题
        self.wait_element(*self.chargeTopic_loc).click()
        # 输入话题价格
        self.wait_element(*self.priceText_loc).send_keys("1")
        # 开启自动分销
        self.wait_element(*self.openAutoDistributeButton_loc).click()
        #输入自动分销比例
        self.wait_element(*self.distributePer_loc).send_keys(10)
        self.wait_element(*self.finishTopicButton_loc).click()

    # ############################新建音视频图文话题###########################
    # 新建系列课内的视频图文话题
    def createVideoGraTopic(self):
        self.wait_element(*self.createTopicButton_loc).click()
        self.wait_element(*self.audioAndVideoGra_loc).click()
        # 课程主题
        self.wait_element(*self.audioAndVideoGraTopicname_loc).send_keys("这个是视频图文话题啊"+str(time.time()))
        # 上传课程封面
        topicPic = getDataFile("测试图片-sportguy1.jpg")
        self.wait_element(*self.topicPic_loc).send_keys(topicPic)
        # 课程类型
        self.wait_element(*self.videoGra_loc).click()
        # 收费类型
        self.wait_element(*self.channelbutton_loc).click()
        # 选择第一个系列课（这里不是select标签）
        self.wait_element(*self.channelSelectbutton_loc).click()
        self.wait_element(*self.channell_loc).click()
        # 选择系列课内单买
        self.wait_element(*self.singleSoleInChannel_loc).click()
        self.wait_element(*self.singleSolePrice_loc).send_keys('1')
        # 直播概要-图片
        liveIntroPicture = getDataFile("测试图片-sportguy2.jpg")
        self.wait_element(*self.liveIntroPictureButton_loc).send_keys(liveIntroPicture)
        # 直播概要-添加文字
        self.wait_element(*self.liveIntroTextButton_loc).click()
        self.wait_element(*self.liveIntroText_loc).send_keys('这个是视频图文话题啊！')
        # 保存
        self.wait_element(*self.saveButton_loc).click()
        # 上传视频  是input表单直接直接使用send_keys()
        video = getDataFile("测试视频-sportguy.mp4")
        self.wait_element(*self.sendVideoButton_loc).send_keys(video)
        time.sleep(1)
        # 点击返回话题列表页面
        self.wait_element(*self.backTopicListButton_loc).click()

    # 新建系列课内的音频图文话题
    def createAudioGra(self):
        self.wait_element(*self.createTopicButton_loc).click()
        self.wait_element(*self.audioAndVideoGra_loc).click()
        # 课程主题
        self.wait_element(*self.audioAndVideoGraTopicname_loc).send_keys("音频图文话题"+str(time.time()))
        # 上传课程封面
        topicPic = getDataFile("测试图片-sportguy5.jpg")
        self.wait_element(*self.topicPic_loc).send_keys(topicPic)
        # 课程类型
        self.wait_element(*self.audioGra_loc).click()
        # 收费类型
        self.wait_element(*self.channelbutton_loc).click()
        # 选择第一个系列课（这里不是select标签）
        self.wait_element(*self.channelSelectbutton_loc).click()
        self.wait_element(*self.channell_loc).click()
        # 选择系列课内单买
        self.wait_element(*self.singleSoleInChannel_loc).click()
        self.wait_element(*self.singleSolePrice_loc).send_keys('999')
        # 直播概要-图片
        liveIntroPicture = getDataFile("测试图片-sportguy5.jpg")
        self.wait_element(*self.liveIntroPictureButton_loc).send_keys(liveIntroPicture)
        # 直播概要-添加文字
        self.wait_element(*self.liveIntroTextButton_loc).click()
        time.sleep(2)
        self.wait_element(*self.liveIntroText_loc).send_keys('这个是yinp@#$%^&*lfjafjajs ;ljjdf ja;ls dljsf图文话题啊！')
        # 保存
        self.wait_element(*self.saveButton_loc).click()
        # 上传视频  是input表单直接直接使用send_keys()
        audio = getDataFile("测试音频-sportguy.mp3")
        self.wait_element(*self.sendVideoButton_loc).send_keys(audio)
        time.sleep(1)
        # 点击返回话题列表页面
        self.wait_element(*self.backTopicListButton_loc).click()

    # 新建打卡训练营内的视频图文话题
    def createVideoGraTopicCamp(self):
        self.wait_element(*self.createTopicButton_loc).click()
        self.wait_element(*self.audioAndVideoGra_loc).click()
        # 课程主题
        self.wait_element(*self.audioAndVideoGraTopicname_loc).send_keys("这个是视频图文话题啊"+str(time.time()))
        # 上传课程封面
        topicPic = getDataFile("测试图片-sportguy1.jpg")
        self.wait_element(*self.topicPic_loc).send_keys(topicPic)
        # 课程类型
        self.wait_element(*self.videoGra_loc).click()
        # 收费类型
        self.wait_element(*self.campleButton_loc).click()
        # 选择第一个系列课（这里不是select标签）
        self.wait_element(*self.campleSelectButton_loc).click()
        self.wait_element(*self.campe_loc).click()
        # 直播概要-图片
        liveIntroPicture = getDataFile("测试图片-sportguy2.jpg")
        self.wait_element(*self.liveIntroPictureButton_loc).send_keys(liveIntroPicture)
        time.sleep(3)
        # 直播概要-添加文字
        self.wait_element(*self.liveIntroTextButton_loc).click()
        self.wait_element(*self.liveIntroText_loc).send_keys('这个是视频图文话题啊！')
        # 保存
        self.wait_element(*self.saveButton_loc).click()
        # 上传视频  是input表单直接直接使用send_keys()
        video = getDataFile("测试视频-sportguy.mp4")
        self.wait_element(*self.sendVideoButton_loc).send_keys(video)
        time.sleep(1)
        # 点击返回话题列表页面
        self.wait_element(*self.backTopicListButton_loc).click()
    # 新建打卡训练营内的视频图文话题
    def createAudioGraTopicCamp(self):
        self.wait_element(*self.createTopicButton_loc).click()
        self.wait_element(*self.audioAndVideoGra_loc).click()
        # 课程主题
        self.wait_element(*self.audioAndVideoGraTopicname_loc).send_keys("音频图文￥$%^#@图文话题啊"+str(time.time()))
        # 上传课程封面
        topicPic = getDataFile("测试图片-sportguy2.jpg")
        self.wait_element(*self.topicPic_loc).send_keys(topicPic)
        # 课程类型
        self.wait_element(*self.audioGra_loc).click()
        # 收费类型
        self.wait_element(*self.campleButton_loc).click()
        # 选择第一个系列课（这里不是select标签）
        self.wait_element(*self.campleSelectButton_loc).click()
        self.wait_element(*self.campe_loc).click()
        # 直播概要-图片
        liveIntroPicture = getDataFile("测试图片-sportguy1.jpg")
        self.wait_element(*self.liveIntroPictureButton_loc).send_keys(liveIntroPicture)
        time.sleep(3)
        # 直播概要-添加文字
        self.wait_element(*self.liveIntroTextButton_loc).click()
        self.wait_element(*self.liveIntroText_loc).send_keys('这个是#%*^%频图文话题啊！')
        # 保存
        self.wait_element(*self.saveButton_loc).click()
        # 上传视频  是input表单直接直接使用send_keys()
        video = getDataFile("测试音频-sportguy.mp3")
        self.wait_element(*self.sendVideoButton_loc).send_keys(video)
        time.sleep(1)
        # 点击返回话题列表页面
        self.wait_element(*self.backTopicListButton_loc).click()

    # 新建视频互动话题-系列课内
    def createVideoTopicChannell(self):
        self.wait_element(*self.createTopicButton_loc).click()
        self.wait_element(*self.audioAndVideoTopic_loc).click()
        # 课程主题
        self.wait_element(*self.videoTopicName_loc).send_keys('视频互动话题-系列课内话题#￥…')
        # 上传课程封面
        topicPic = getDataFile("测试图片-sportguy1.jpg")
        self.wait_element(*self.videoTopic_loc).send_keys(topicPic)
        # 选择直播类型
        self.wait_element(*self.video_loc).click()