from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

class Page():
    '''基础类，用于所有页面的继承'''
    home_url = r"https://m.qlchat.com/wechat/page/topic-intro?topicId=2000001368645697"
    pcUrl = "https://m.qlchat.com/video/admin/live/select"
    def __init__(self,driver,base_url=home_url):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 30
    # def on_page(self):
    #     return self.driver.current_url == (self.base_url + self.url)
    def _open(self):
        url = self.base_url
        self.driver.get(url)
        # assert self.on_page(),"Did not land on %s" %url
    # 打开页面操作
    def open(self):
        self._open()
    def _openPc(self):
        self.open()
        cookies1 = {"name": "QLZB_SESSIONID",
                    "value": "4B6250526A505A5A2F3532506F6446537552357167336276646C79537151536631673449674E51637832413D"}
        cookies2 = {"name": "JSESSIONID", "value": "D395751EE783F47A40E57E501670614E"}
        cookies3 = {"name": "rsessionid",
                    "value": "qlwrsid%3A7A72F7FD-5FC9-4871-9E5D-96FCE61CEA00.QROHJBR0uqoEc6xLMzVAPCVjRlUs6OeIpSFzRpCJ2NI"}
        self.driver.add_cookie(cookie_dict=cookies1)
        self.driver.add_cookie(cookie_dict=cookies2)
        self.driver.add_cookie(cookie_dict=cookies3)
        self.driver.refresh()
        self.driver.get(self.pcUrl)
        self.driver.maximize_window()
    # 增加cookies打开PC管理后台页面操作
    def openPc(self):
        self._openPc()
    def find_element(self,*loc):
        return self.driver.find_element(*loc)
    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)
    # 使用显式等待定位元素
    def wait_element(self,*loc):
        return WebDriverWait(self.driver,10,0.5).until(lambda driver:self.find_element(*loc))
    def wiat_elements(self,*loc):
        return WebDriverWait(self.driver,10,0.5).until(lambda driver:self.find_elements(*loc))
    # 执行js脚本
    def execute_js(self,src):
        return self.driver.execute_script(src)
    # 处理下拉框
    def select(self,el,number):
        return Select(el).select_by_index(number)
    #警告框的处理，获取文本
    def switch_alert(self):
        return self.driver.switch_to_alert().text