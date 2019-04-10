# Date：10/3/2019
# Name:kobe
# -*- coding:utf-8 -*-

from selenium.webdriver.common.by import By
from pages.basePage import BasePage
import random

class CommodityClassificationPage(BasePage):

    def randomChoiceShop(self):
        ul = self.driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[2]/ul')
        li = ul.find_elements_by_tag_name('li')
        li[random.randint(0, len(li)-1)].find_element_by_tag_name('a').click()