import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
if __name__ == '__main__':
    service = ChromeService(executable_path=".\\chromedriver-win64\\chromedriver.exe")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options, service=service)
    driver.get('https://s.weibo.com/weibo?q=test')
    title = driver.title
    while (title != "微博搜索"):
        time.sleep(1)
        title = driver.title
    dictCookies = driver.get_cookies()
    with open('cookies.json', 'w', encoding='utf-8') as f:
        json.dump(dictCookies, f)
    print("Successfully saved cookies!")