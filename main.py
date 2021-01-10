from dotenv import load_dotenv
import re
import sqlite3
import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # オプションを使うために必要
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import chromedriver_binary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# .envファイルの内容を読み込みます
load_dotenv()


def login():
    driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    f = open('insta.txt', 'a')
    f.write("instagramにアクセスしました\n")
    f.close()
    time.sleep(1)
    username = os.environ['USERNAME']
    password = os.environ['PASSWORD']
    driver.find_element_by_name('username').send_keys(username)
    time.sleep(1)
    driver.find_element_by_name('password').send_keys(password)
    time.sleep(1)

    # ログインボタンを押す
    driver.find_element_by_class_name('L3NKy       ').click()
    time.sleep(random.randint(2, 5))
    f = open('insta.txt', 'a')
    f.write("instagramにログインしました\n")
    f.close()
    time.sleep(1)


def tagsearch(tag):
    instaurl = 'https://www.instagram.com/explore/tags/'
    driver.get(instaurl + tag)
    time.sleep(random.randint(2, 10))
    f = open('insta.txt', 'a')
    f.write("listtagより、tagで検索を行いました\n")
    f.close()
    time.sleep(1)


def clicknice():
    target = driver.find_elements_by_class_name('_9AhH0')[9]
    actions = ActionChains(driver)
    actions.move_to_element(target)
    actions.perform()
    f = open('insta.txt', 'a')
    f.write("最新の投稿まで画面を移動しました\n")
    f.close()
    time.sleep(1)

    dbname = os.environ["DBNAME"]
    wait = WebDriverWait(driver, 10)

    try:
        driver.find_elements_by_class_name('_9AhH0')[0].click()
        time.sleep(random.randint(2, 10))
        f = open('insta.txt', 'a')
        f.write("投稿をクリックしました\n")
        f.close()
        time.sleep(1)
        post_text = driver.find_element_by_class_name("C4VMK")
        post_contain = post_text.find_elements_by_tag_name("span")[1].text
        post_contain_plane_format = re.sub('\s', '', post_contain)
        print(post_contain_plane_format)

        for i in range(random.randint(200, 300)):
            # follow_button = driver.find_element_by_css_selector(
            # '.bY2yH .sqdOP')
            follow_button = wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '.bY2yH .sqdOP')))
            print(follow_button.text)

            # もしフォローしていなければフォローする
            if follow_button.text == "フォローする":
                # フォローする
                follow_button.click()
                # フォローした人にのみコメントを残す
                try:
                    driver.find_element_by_class_name(
                        'Ypffh').click()
                    driver.find_element_by_class_name(
                        'Ypffh').send_keys("フォローさせていただきました！")
                    time.sleep(3)
                    driver.find_element_by_css_selector(
                        '.X7cDz .sqdOP').click()
                except:
                    print("コメントできません。")
                f = open('insta.txt', 'a')
                f.write("フォローしました\n")
                f.close()

            # 新しくいいねするものだけを処理
            driver.find_element_by_class_name('fr66n').click()
            f = open('insta.txt', 'a')
            f.write("投稿をいいねしました\n")
            f.close()
            time.sleep(1)

            try:
                driver.find_element_by_class_name(
                    'coreSpriteRightPaginationArrow').click()
                f = open('insta.txt', 'a')
                f.write("次の投稿へ移動しました\n")
                f.close()
                time.sleep(random.randint(
                    random.randint(2, 5), random.randint(10, 15)))

            except WebDriverException:
                f = open('insta.txt', 'a')
                f.write("２つ目の位置でエラーが発生しました\n")
                f.close()
                time.sleep(5)

            try:
                post_text = driver.find_element_by_class_name("C4VMK")
                post_contain = post_text.find_elements_by_tag_name("span")[
                    1].text
                post_contain_plane_format = re.sub('\s', '', post_contain)
                print(post_contain_plane_format)
            except WebDriverException:
                f = open('insta.txt', 'a')
                f.write("lastエラーが発生しました\n")
                f.close()
                time.sleep(5)

    except WebDriverException:
        import traceback
        traceback.print_exc()
        f = open('insta.txt', 'a')
        f.write("エラーが発生しました\n")
        f.close()
        return


if __name__ == '__main__':
    taglist = ['広がり同盟']  # ここに自分の好きなハッシュタグを記載 #######
    option = Options()
    # option.add_argument('--headless')
    driver = webdriver.Chrome(
        options=option)
    time.sleep(1)
    login()
    tagsearch(random.choice(taglist))
    clicknice()
    driver.quit()
    sys.exit()
