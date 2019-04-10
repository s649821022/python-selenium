# Date：9/3/2019
# Name:kobe
# -*- coding:utf-8 -*-

from common.timeUntil import TimeUntil
import os

class ScreenShot(object):
    def screenShot(self, driver):
        scrTime = TimeUntil().currentDataTime()
        scrName = os.path.dirname(os.path.abspath('.')) + '\\screenshot\\' + scrTime + '.png'
        driver.get_screenshot_as_file(scrName)

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    ScreenShot().screenShot(driver)
