# from selenium import webdriver
# import pytest
#
# driver = None
#
#
# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#     当测试失败的时候，自动截图，展示到html报告中
#     """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::", "_") + ".png"
#             screen_img = _capture_screenshot()
#             if file_name:
#                 html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % screen_img
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#
#
# def _capture_screenshot():
#     '''
#     截图保存为base64，展示到html中
#
#     '''
#     return driver.get_screenshot_as_base64()
#
#
# @pytest.fixture(scope='session', autouse=True)
# def browser():
#     global driver
#     if driver is None:
#         driver = webdriver.Firefox()
#     return driver

import pytest
import allure
from selenium import webdriver

driver = None


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        if hasattr(driver, "get_screenshot_as_png"):
            allure.attach(driver.get_screenshot_as_png(), "异常截图", allure.attachment_type.PNG)


@pytest.fixture(scope="session")
def browser():
    global driver
    if driver is None:
        driver = webdriver.Chrome()
        driver.maximize_window()
    yield driver
    # 所有用例执行完毕退出浏览器
    driver.quit()
