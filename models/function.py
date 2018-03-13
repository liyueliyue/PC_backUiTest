import sys,os
sys.path.append('./models')

def insert_img(driver,filename):
    base_dir = os.path.dirname(__file__)
    base_dir = str(base_dir)
    base_dir = base_dir.replace("\\","/")
    base = base_dir.split('/models')[0]
    file_path = base + "/test_report/image/" + filename
    driver.get_screenshot_as_file(file_path)
if __name__ == "__main__":
    from models.driver import browser
    from time import sleep
    driver = browser()
    driver.get(r'https://m.qlchat.com/topic/details?topicId=2000000871263149&preview=Y')
    cookies = {"name": "userId", "value": "270000127243445"}
    cookies1 = {"name": "QLZB_SESSIONID",
                "value": "4B6250526A505A5A2F3532506F6446537552357167336276646C79537151536631673449674E51637832413D"}
    cookies2 = {"name": "JSESSIONID", "value": "D395751EE783F47A40E57E501670614E"}
    cookies3 = {"name": "rsessionid",
                "value": "qlwrsid%3A7A72F7FD-5FC9-4871-9E5D-96FCE61CEA00.QROHJBR0uqoEc6xLMzVAPCVjRlUs6OeIpSFzRpCJ2NI"}
    driver.add_cookie(cookie_dict=cookies1)
    driver.add_cookie(cookie_dict=cookies2)
    driver.add_cookie(cookie_dict=cookies3)
    driver.refresh()
    sleep(1)
    driver.get(r'https://m.qlchat.com/video/admin/live/select')
    driver.maximize_window()
    sleep(1)
    driver.find_element_by_xpath(".//*[@id='app']/div/div[1]/div[2]/div/div/div[1]/div/div/div").click()
    sleep(1)
    insert_img(driver,"仪表盘首页.jpg")

    driver.quit()
