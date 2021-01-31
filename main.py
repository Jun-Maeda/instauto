#!/usr/bin/env python3
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
from ig_sc import login, tagsearch, clicknice

# .envファイルの内容を読み込みます
load_dotenv()


if __name__ == '__main__':
    taglist = os.environ['HASHTAG']
    time.sleep(1)
    login()
    tagsearch(taglist)
    clicknice()
    driver.quit()
    sys.exit()
