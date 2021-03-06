import unittest
from models.function import insert_img
from models.driver import browser
from page_obj.dashBoardPage import DashBoard
from time import sleep
from page_obj.selectLivePage import SelectLive
from page_obj.topicListPage import TopicList

class topicList(unittest.TestCase):
    """pc管理后台单课列表"""
    def setUp(self):
        self.driver = browser()
        self.dashboard = DashBoard(self.driver)
        self.selectLive = SelectLive(self.driver)
        self.selectLive.enterMyPcHome()
        self.topicList = TopicList(self.driver)
    def tearDown(self):
        self.driver.quit()
    def test_a_enterTopicList(self):
        '''进入单课列表'''
        self.dashboard.topicList()
        sleep(1)
        insert_img(self.driver,"7单课列表.jpg")
        # 断言
        self.assertEqual(self.topicList.getTopicTitleText(),'单课')
    def test_a1_createLectureTopic_free(self):
        '''新建讲座直播话题-免费'''
        self.dashboard.topicList()
        self.topicList.createLectureTopicFree()
        sleep(1)
        insert_img(self.driver,"8新建讲座直播话题-免费.jpg")
        # 断言
        self.assertIn("讲座直播话题-免费",self.driver.title)
    def test_a2_createLectureTopic_encrypt(self):
        '''新建讲座直播话题-加密'''
        self.dashboard.topicList()
        self.topicList.createLectureTopicEncrypted()
        sleep(1)
        insert_img(self.driver,"9新建讲座直播话题-加密.jpg")
        # 断言
        self.assertIn("讲座直播话题-加密",self.driver.title)
    def test_a3_createLectureTopic_charge(self):
        '''新建讲座直播话题-收费'''
        self.dashboard.topicList()
        self.topicList.createLectureTopicCharge()
        sleep(1)
        insert_img(self.driver,"10新建讲座直播话题-收费.jpg")
        # 断言
        self.assertIn("讲座直播话题-收费",self.driver.title)
    def test_b_createPptTopic_free(self):
        '''新建幻灯片直播话题-免费'''
        self.dashboard.topicList()
        self.topicList.createPptTopicFree()
        sleep(1)
        insert_img(self.driver,"11幻灯片直播话题-免费.jpg")
        # 断言
        self.assertIn("幻灯片直播话题-免费",self.driver.title)
    def test_b1_createPptTopic_encrypt(self):
        '''新建幻灯片直播话题-加密'''
        self.dashboard.topicList()
        self.topicList.createPptTopicEncrypted()
        sleep(1)
        insert_img(self.driver,"12幻灯片直播话题-加密.jpg")
        # 断言
        self.assertIn("幻灯片直播话题-加密",self.driver.title)
    def test_b2_createPptTopic_charge(self):
        '''新建幻灯片直播话题-收费'''
        self.dashboard.topicList()
        self.topicList.createPptTopicCharge()
        sleep(1)
        insert_img(self.driver,"13幻灯片直播话题-收费.jpg")
        # 断言
        self.assertIn("幻灯片直播话题-收费",self.driver.title)

    def test_c_createVideoGra(self):
        '''新建视频图文话题-channell'''
        self.dashboard.topicList()
        self.topicList.createVideoGraTopic()
        sleep(1)
        insert_img(self.driver,"14系列课内视频图文话题.jpg")
        # 断言
        self.assertIn("liveId=310000108181722&channelId=",self.driver.current_url)
    def test_c2_createAudioGra(self):
        '''新建音频图文话题-channell'''
        self.dashboard.topicList()
        self.topicList.createAudioGra()
        sleep(1)
        insert_img(self.driver,"15系列课内音频图文话题.jpg")
        # 断言
        self.assertIn("liveId=310000108181722&channelId=",self.driver.current_url)
    def test_c3_createVideoGraTopicCamp(self):
        '''新建视频图文话题-campe'''
        self.dashboard.topicList()
        self.topicList.createVideoGraTopicCamp()
        sleep(1)
        insert_img(self.driver,"16训练营内视频图文话题.jpg")
        # 断言
        self.assertIn("camp-topic-list?liveId=310000108181722",self.driver.current_url)
    def test_c4_createAudioGraTopicCamp(self):
        '''新建音频图文话题-campe'''
        self.dashboard.topicList()
        self.topicList.createAudioGraTopicCamp()
        sleep(1)
        insert_img(self.driver,"17训练营内音频图文话题.jpg")
        # 断言
        self.assertIn("camp-topic-list?liveId=310000108181722",self.driver.current_url)
if __name__ == "__main__":
    unittest.main()