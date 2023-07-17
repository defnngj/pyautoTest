import sys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

"""
获取背景图片和滑块的位置信息：通过背景图片和滑块的位置信息，以便计算滑块需要拖动的距离。

计算滑块需要拖动的距离：根据滑块和背景图片的位置信息，可以计算出滑块需要拖动的距离。

模拟鼠标操作：使用ActionChains类来模拟鼠标的拖动操作，将滑块拖动到指定位置。
"""

    #传入driver、滑块元素、背景元素
def SliderTool(driver,slider_ele,background_ele):
    """
    《滑块验证码处理工具》\n
    传入driver、滑块元素、背景元素\n
    ps:请确保滑块和背景元素已经展示了再获取element，否则本方法可能失效
    """ 
    #计算滑块和背景的相对距离
    distance = slider_ele.size["width"] + background_ele.size["width"]
    print(f"滑块+滑道的像素距离：{distance}")
    #模拟鼠标操作（按住元素，滑动到指定位置，释放鼠标）
    act = ActionChains(driver)
    act.click_and_hold(slider_ele).perform()
    #先滑动[distance - 5] 个像素
    act.move_by_offset(distance,0).perform()
    #使用循环，每100毫秒滑动1个像素，最多移动10个像素
    for j in range(1,11):
        act.move_by_offset(1,0).perform()
        #打印划过的像素数量，sys.stdout.write() 输出一个字符串，包含一个回车符 \r，表示将输出内容定位到本行开头。sys.stdout.flush() 将输出内容刷新到控制台
        sys.stdout.write(f"\r已移动: [ {j} ]个像素点")
        sys.stdout.flush()
        sleep(0.1)
    # 释放鼠标，完成滑动操作
    act.release().perform()
    if slider_ele.is_displayed() == False:
        print("\n滑块识别成功")
    elif slider_ele.is_displayed() == True:
        print("\n滑块识别失败")
