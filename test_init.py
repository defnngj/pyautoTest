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
from tools.SliderVerificationTool import SliderTool

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

sleep(3)
slider = driver.find_element(By.CSS_SELECTOR,"#yodaBox")
background = driver.find_element(By.CSS_SELECTOR,"#yodaBoxWrapper > label")

SliderTool(driver,slider,background)

sleep(2000)