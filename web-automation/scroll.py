from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.chrome.options import Options

import time

# 初始化浏览器驱动器
driver = webdriver.Chrome()  # 或者使用其他浏览器的驱动器

# 打开网页
driver.get("https://www.uworld.com/memberarea.aspx")
# driver.get("https://www.cnblogs.com/superhin/p/11482188.html")



while True:

    # window_height = driver.get_window_size()['height']  # 窗口高度

    # page_height = driver.execute_script('return document.documentElement.scrollHeight')  # 页面高度

    scroll_element = driver.find_element(By.CSS_SELECTOR, ".question-content.right-content")
    answer_element = driver.find_element(By.ID,"explanation")
    # element.screenshot("element_screenshot.png")
    div_scrollHeight = driver.execute_script("return arguments[0].scrollHeight;", answer_element)
    div_offsetHeight = driver.execute_script("return arguments[0].offsetHeight;", answer_element)



    viewport_height = driver.execute_script("return window.innerHeight;")
    half_height = viewport_height / 2

    # 获取视口宽度
    viewport_width = driver.execute_script("return window.innerWidth;")
    # 计算右半区的水平位置（视口宽度的一半）
    half_width = viewport_width / 2

    # #移动鼠标到右半区
    # action = ActionBuilder(driver)
    # action.pointer_action.move_to_location(half_width+10, half_height)
    # action.perform()

    # 获取页面高度
    page_height = driver.execute_script("return document.body.scrollHeight")

    scrolls = div_scrollHeight/844
    params = (scroll_element, 844)

    for i in range(int(scrolls)+1):
        driver.save_screenshot(f"answer{i+1}.png")
        # 模拟滚动到页面底部
        driver.execute_script("arguments[0].scrollBy(0, arguments[1]);", *params)
