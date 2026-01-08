import os
import time
import random
from tinydb import TinyDB
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from config import topics

db_cnt = 0
MAX_PAGES = 20
def save(db, results):
    global db_cnt
    for result in results:
        db.insert({"index": db_cnt, "data": result})
        db_cnt += 1
def get_page(driver, db, topic, page):
    def click(driver, button):
        driver.execute_script("arguments[0].click();", button)
        time.sleep(1 + random.random())
        if driver.current_url != url:
            driver.switch_to.window(main_window)
    url = 'https://s.weibo.com/weibo?q=' + topic + "&page=" + str(page)
    driver.get(url)
    title = driver.title
    while (title != "微博搜索"):
        time.sleep(1)
        title = driver.title
    main_window = driver.current_window_handle

    items = driver.find_elements(By.XPATH, '//div[@action-type="feed_list_item" and @class="card-wrap"]')
    results = list()
    for item in items:
        result = dict()
        try:
            expand_button = item.find_elements(By.XPATH, './/a[@action-type="fl_unfold"]')
            if len(expand_button) > 0:
                click(driver, expand_button[0])
            content = item.find_elements(By.XPATH, './/p[@node-type="feed_list_content"]')
            content_full = item.find_elements(By.XPATH, './/p[@node-type="feed_list_content_full"]')
            if len(content_full) > 0:
                result["content"] = content_full[0].text.rstrip("收起d")
            else:
                result["content"] = content[0].text
            result["comments"] = list()

            comment_button = item.find_elements(By.XPATH, './/a[@action-type="feed_list_comment" and @class="woo-box-flex woo-box-alignCenter woo-box-justifyCenter"]')
            click(driver, comment_button[-1])
            comments = item.find_elements(By.XPATH, './/div[@class="card-review s-ptb10"]')
            for comment in comments:
                comment.find_elements(By.XPATH, './/div[@class="txt"]')
                result["comments"].append(comment.text)
            results.append(result)
        except Exception as e:
            print(e)
            continue
        time.sleep(1 + 3 * random.random())
    save(db, results)
    return len(results)

if __name__ == "__main__":
    os.makedirs(".\\Topics", exist_ok=True)
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
    for topic in topics:
        db_cnt = 0
        db = TinyDB(".\\Topics\\" + f"{topic}.json", ensure_ascii=False, encoding='utf-8')
        cnt = 0
        for page in range(1, MAX_PAGES):
            cnt += get_page(driver, db, topic, page)
            time.sleep(3 * random.random())
            if cnt >= 100:
                break
        time.sleep(5 + 3 * random.random())
    driver.quit()