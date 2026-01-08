import os
import time
import random
from tinydb import TinyDB
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from config import user_url

DEBUG = False

MAX_CONTENT = 10
def save(db, results):
    for k, v in results.items():
        db.insert({"index": k, "data": v})
def get_content(driver, db, url):
    def exit_comment(driver):
        try:
            driver.find_elements(By.XPATH, "//span[@class='CopyRight_cricon_3Apzk']")[0].click()
        except:
            print("error")
            pass
    driver.get(url)
    time.sleep(3)
    client_height = driver.execute_script('return document.documentElement.clientHeight')
    driver.execute_script(f'window.scrollBy(0, {client_height // 4});')
    results = dict()

    for i in range(MAX_CONTENT):
        items = driver.find_elements(By.XPATH, "//div[@class='vue-recycle-scroller__item-view']")
        contents = list()
        for item in items:
            # index = item.find_elements(By.XPATH, ".//div[contains(@class, 'wbpro-scroller-item')]")
            # index = int(index[0].get_attribute("data-index"))
            item_index = item.find_elements(By.XPATH, ".//a[@class='head-info_time_6sFQg']")
            item_time = item_index[0].get_attribute('title')
            item_index = item_index[0].get_attribute('href')
            if item_index in results.keys():
                continue
            contents.append((item_index, item_time, item))

        if len(contents) == 0:
            driver.execute_script(f"window.scrollBy(0, {client_height // 2});")
            continue
        contents = sorted(contents, key=lambda x: x[1], reverse=True)

        current_height = driver.execute_script("return window.pageYOffset;")
        content_height = contents[0][2].location['y']
        if current_height > content_height:
            driver.execute_script(f"window.scrollBy(0, {- client_height // 2});")

        for item_index, item_time, item in contents:
            result = dict()
            try:
                result["time"] = item_time
                expand_button = item.find_elements(By.XPATH, ".//span[@class='expand']")
                if len(expand_button) > 0:
                    driver.execute_script("arguments[0].click();", expand_button[0])
                    if not DEBUG:
                        time.sleep(1 + random.random())
                    exit_comment(driver)

                content = item.find_elements(By.XPATH, ".//div[@class='detail_wbtext_4CRf9']")
                result["content"] = content[0].text

                height = item.size["height"]
                driver.execute_script(f"window.scrollBy(0, {height});")

                comment_button = item.find_elements(By.XPATH, ".//i[@title='评论' and @class='woo-font woo-font--comment toolbar_commentIcon_3o7HB']")
                driver.execute_script("arguments[0].click();", comment_button[-1])
                if not DEBUG:
                    time.sleep(1 + random.random())
                exit_comment(driver)

                comments = item.find_elements(By.XPATH, ".//div[@class='wbpro-list']")
                result["comment"] = list()
                for comment in comments:
                    comment.find_elements(By.XPATH, ".//div[@class='text']")
                    comment = comment.text.split("来自")
                    result["comment"].append({"comment": comment[0], "responses_to_comment": comment[1:-1]})

                height = item.size["height"] - height
                driver.execute_script(f"window.scrollBy(0, {height});")

                results[item_index] = result
            except Exception as e:
                print(e)
                continue
        time.sleep(1 + 3 * random.random())
    save(db, results)

if __name__ == "__main__":
    os.makedirs(".\\User", exist_ok=True)
    db = TinyDB(".\\User\\" + 'user.json', ensure_ascii=False, encoding='utf-8')
    service = ChromeService(executable_path=".\\chromedriver-win64\\chromedriver.exe")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options, service=service)
    driver.get('https://s.weibo.com/weibo?q=test')
    title = driver.title
    while (title != "微博搜索"):
        time.sleep(1)
        title = driver.title
    # with open('cookies.json', 'r', encoding='utf-8') as f:
    #     cookies = json.load(f)
    # for cookie in cookies:
    #     driver.add_cookie(cookie)
    get_content(driver, db, user_url)
    driver.quit()