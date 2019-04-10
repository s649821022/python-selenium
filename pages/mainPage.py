# Date：9/3/2019
# Name:kobe
# -*- coding:utf-8 -*-

from selenium.webdriver.common.by import By
from pages.basePage import BasePage
import random
class MainPage(BasePage):

    login_btn = (By.LINK_TEXT, '登录')

    def enter_loginPage(self):
        self.click(self.login_btn)

    computer = (By.LINK_TEXT, '电脑')

    def enter_computer(self):
        self.click(self.computer)

    def random_choice(self):
        id = self.driver.find_element_by_id('index_category')
        th = id.find_elements_by_tag_name('th')
        th[random.randint(0, len(th)-1)].find_element_by_tag_name('a').click()
