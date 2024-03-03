from selenium import webdriver
from selenium.webdriver.common.by import By

import time

# 初始化浏览器驱动器
driver = webdriver.Chrome()  # 或者使用其他浏览器的驱动器

# 打开网页
driver.get("https://www.uworld.com/memberarea.aspx")

# # 等待网页加载完成
# driver.implicitly_wait(10)  # 等待最多10秒钟，可以根据需要调整等待时间

# # driver.find_element("[title='Close']").click()

# # 找到用户名输入框并输入用户名
# username_input = driver.find_element(By.CSS_SELECTOR,"#login-email")
# username_input.send_keys("lhf1019631213@126.com")

# # 找到密码输入框并输入密码
# password_input = driver.find_element(By.CSS_SELECTOR,"#login-password")
# password_input.send_keys("TOEFL100sat2200")

# time.sleep(5)


# # 找到登录按钮并点击登录
# login_button = driver.find_element(By.CSS_SELECTOR,"#login_btn")
# login_button.click()

# # 等待登录成功后的页面加载完成
# driver.implicitly_wait(10) 
for i in range(85):
    driver.save_screenshot(f"{i+1}_question.png")

    submit_btn = driver.find_element(By.XPATH, '//button[@aria-label="Submit"]')
    submit_btn.click()
    time.sleep(1)

    yes_button = driver.find_element(By.CSS_SELECTOR,".mat-focus-indicator.mat-primary.no-focus.mat-raised-button.mat-button-base")
    yes_button.click()
    time.sleep(1)
    # 获取网页内容的高度
    driver.save_screenshot(f"{i+1}_answer.png")

    next = driver.find_element(By.XPATH,'//a[@aria-label="Navigate to the next question"]')
    next.click()
    time.sleep(1)


print("finish~!")