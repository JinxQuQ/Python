from selenium import webdriver
import time


def test_yoyo_01(browser:webdriver.Firefox):

    browser.get("https://www.cnblogs.com/yoyoketang/")
    time.sleep(2)
    t = browser.title
    assert "上海-金克丝" in t