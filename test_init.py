#目的：构建一个能自主更新浏览器驱动的框架（只使用谷歌浏览器）

#导入对应的包
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as CH_options
from time import sleep

#参数实例化浏览器驱动
#options参数设置
chrome_options = CH_options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])#去除 “Chrome正受到自动化测试软件的控制”
#chrome_options.add_argument("--headless")
#chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(options=chrome_options,service=ChromeService(ChromeDriverManager().install()))
#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(30)

#打开网页
driver.get("http://pos.meituan.com/web/rms-account#/login")
#切换iframe
frame_element = driver.find_element(By.CSS_SELECTOR,"#__root_wrapper_ > div > div.introduce-bg-3TjSR > div > div.ant-col.login-section-36Fr9 > iframe")
driver.switch_to.frame(frame_element)
#点击账号登录
driver.find_element(By.CSS_SELECTOR,"#app > div > div.header > a:nth-child(2)").click()
#输入账号
driver.find_element(By.CSS_SELECTOR,"#account").send_keys(17808231403)
#输入密码并回车登录
driver.find_element(By.CSS_SELECTOR,"#password").send_keys("meituan123",Keys.ENTER)


"""
定位滑块和背景图片：首先需要通过元素定位来找到滑块和背景图片的元素。

获取背景图片和滑块的位置信息：需要获取背景图片和滑块的位置信息，以便后续计算滑块需要拖动的距离。

计算滑块需要拖动的距离：根据滑块和背景图片的位置信息，可以计算出滑块需要拖动的距离。

模拟鼠标操作：使用ActionChains类来模拟鼠标的拖动操作，将滑块拖动到指定位置。
"""
#定位滑块和背景图片的元素
sleep(4)
slider = driver.find_element(By.CSS_SELECTOR,"#yodaBox")
background = driver.find_element(By.CSS_SELECTOR,"#yodaBoxWrapper > label")
print(background.size)
#计算滑块和背景的相对距离
distance = slider.size["width"] + background.size["width"]
print(distance)
#模拟鼠标操作（按住元素，滑动到指定位置，释放鼠标）
act = ActionChains(driver)
act.click_and_hold(slider).perform()
#先滑动[distance - 5] 个像素
act.move_by_offset(distance,0).perform()
#使用循环，每100毫秒滑动5像素
for j in range(0,10):
    act.move_by_offset(1,0).perform()
    print(j)
    sleep(0.1)
# 释放鼠标，完成滑动操作
act.release().perform()
if slider.is_displayed() == False:
    print("识别成功")
elif slider.is_displayed() == True:
    print("识别失败")
sleep(2000)