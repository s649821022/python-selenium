# Date：10/3/2019
# Name:kobe
# -*- coding:utf-8 -*-

from selenium.webdriver.common.by import By
from pages.basePage import BasePage

class BuyPage(BasePage):

    buy_now = (By.ID, 'buy_now')

    def buyNow(self):
        self.click(self.buy_now)

# china = (By.ID, 'delivery1')
# shentong = (By.ID, 'delivery2')
# shunfeng = (By.ID, 'delivery3')
# oneone = (By.ID, 'delivery4')
# chinaList = list(china)
# shengtongList = list(shentong)
# shunfengList = list(shunfeng)
# oneoneList = list(oneone)
# list = []
# list.append(chinaList)
# list.append(shengtongList)
# list.append(shunfengList)
# list.append(oneoneList)
# print(list)