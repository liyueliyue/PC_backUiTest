from selenium import webdriver
from time import sleep

def browser():
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox()
    return driver
if __name__ == "__main__":
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
    sleep(2)
    driver.find_element_by_xpath(".//*[@id='app']/div/div[1]/div/div[2]/div/div[2]/div[2]/header/ul/li[3]/span").click()
    text = driver.find_element_by_xpath("html/body/div[3]/div/span/div/div/div/span").text
    print(text)


    driver.quit()