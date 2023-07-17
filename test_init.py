#目的：构建一个能自主更新浏览器驱动的框架（只使用谷歌浏览器）

#导入对应的包
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep

#参数实例化浏览器驱动
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
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
slider = driver.find_element(By.CSS_SELECTOR,"#yodaBox")
background = driver.find_element(By.CSS_SELECTOR,"#yodaBoxWrapper > label")

#计算滑块和背景的相对距离
distance = background.location["x"] - slider.location["x"]
#模拟鼠标操作（按住元素，滑动到指定位置，释放鼠标）
i = 120
act = ActionChains(driver)
while True:
    i += 20
    for j in range(10,20,5):
        act.click_and_hold(slider).move_by_offset(j,0).perform()
        sleep(0.5)
    act.release().perform()
    if slider.is_displayed() == False:
        print("识别成功")
        break
sleep(2000)