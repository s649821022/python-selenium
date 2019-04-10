# Date：9/3/2019
# Name:kobe
# -*- coding:utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class BasePage(object):
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.timeout = 10

    def ele_is_presence(self, eleTuple):
        try:
            ele = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(eleTuple))
            return ele
        except:
            self.logger.error('ele_is_presence:未找到元素 %s' % eleTuple)

    def input_text(self, eleTuple, text):
        try:
            ele = self.ele_is_presence(eleTuple)
            ele.clear()
            ele.send_keys(text)
        except:
            self.logger.error('send_keys:未找到元素 %s 或不能发送文本' % eleTuple)

    def click(self, eleTuple):
        try:
            self.ele_is_presence(eleTuple).click()
        except:
            self.logger.error('click:未找到元素 %s 或不可点击' % eleTuple)

    def open_url(self, url):
        try:
            self.driver.get(url)
            self.driver.maximize_window()
        except:
            self.logger.error('url地址错误')

    def select_index(self, eleTuple, number):
        try:
            options = self.ele_is_presence(eleTuple)
            self.select = Select(options)
            self.select.select_by_index(number)
        except:
            self.logger.error('没有找到这个选项')









