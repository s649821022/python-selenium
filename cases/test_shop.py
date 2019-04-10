# Date：9/3/2019
# Name:kobe
# -*- coding:utf-8 -*-

import unittest
from selenium import webdriver
from common.excelUntil import ExcelMethod
from time import sleep
from common.readConfig import ReadConfig
import os
from common.logging_method import LoggingMethod
from pages.mainPage import *
from pages.loginPage import LoginPage
from common.browser_setup import *
from common.geturl import getUrl
from common.screen_shot import *
from pages.buyPage import BuyPage
from pages.commodityClassificationPage import CommodityClassificationPage
from pages.shoppingCartPage import ShoppingCartPage



class Shop(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.logger = LoggingMethod().getLogger()
        cls.ReadConfig = ReadConfig(cls.logger)
        cls.driver = BrowserSetup(cls.logger).browserSetup()
        cls.url = getUrl('/iwebshop/', cls.logger)
        cls.driver.get(cls.url)
        cls.shoppingCartPage = ShoppingCartPage(cls.driver, cls.logger)
        cls.shoppingCartPage.open_url(cls.url)
        cls.inputConsigneeName = int(cls.ReadConfig.readConfig('consignee', 'inputConsigneeName'))
        cls.inputConsignAddress = int(cls.ReadConfig.readConfig('consignee', 'inputConsignAddress'))
        cls.inputConsignTelephone = int(cls.ReadConfig.readConfig('consignee', 'inputConsignTelephone'))
        cls.inputConsignPhone = int(cls.ReadConfig.readConfig('consignee', 'inputConsignPhone'))
        cls.inputConsignPostalCode = int(cls.ReadConfig.readConfig('consignee', 'inputConsignPostalCode'))
        cls.expectedResult = int(cls.ReadConfig.readConfig('consignee', 'expectedResult'))
        cls.isExecute = int(cls.ReadConfig.readConfig('consignee', 'isExecute'))
        cls.testResult = int(cls.ReadConfig.readConfig('consignee', 'testResult'))
        cls.data_path = os.path.dirname(os.path.abspath('.')) + '\\data\\' + 'login.xlsx'
        cls.excelMethod = ExcelMethod(cls.logger, cls.data_path)
        cls.user_list = cls.excelMethod.readExcel('Sheet2', cls.isExecute)
        cls.index = int(cls.ReadConfig.readConfig('consignee', 'index'))

    def test_shop(self):
        # 滑动屏幕
        scroll = "document.getElementById('index_category').scrollIntoView(true)"
        self.driver.execute_script(scroll)
        sleep(2)
        # 随机进入商品分类页面
        choice_enter = MainPage(self.driver, self.logger)
        choice_enter.random_choice()
        sleep(1)

        enter_commodity = CommodityClassificationPage(self.driver, self.logger)
        enter_commodity.randomChoiceShop()  # 随机进入购买界面
        sleep(1)

        click_buy = BuyPage(self.driver, self.logger)
        click_buy.buyNow()  # 点击购买


        # 未登录的情况，点击登录

        login_Page = LoginPage(self.driver, self.logger)
        login_Page.input_username('zhang')
        sleep(1)
        login_Page.input_password('111111')
        sleep(1)
        login_Page.click_submit()
        sleep(1)
        # 选择省份
        self.shoppingCartPage.selectProvince(2)
        sleep(1)
        # 选择城市
        self.shoppingCartPage.selectCity(1)
        sleep(1)
        # 选择区
        self.shoppingCartPage.selectArea(8)
        sleep(1)

        for i in range(0, len(self.user_list)):
            shoppingCard_Page= ShoppingCartPage(self.driver, self.logger)
            shoppingCard_Page.inputConsigneeName(self.user_list[i][self.inputConsigneeName])
            sleep(1)
            shoppingCard_Page.inputConsigneeAddress(self.user_list[i][self.inputConsignAddress])
            sleep(1)
            shoppingCard_Page.inputConsignTeleMobile(self.user_list[i][self.inputConsignTelephone])
            sleep(1)
            shoppingCard_Page.inputConsignMobile(self.user_list[i][self.inputConsignPhone])
            sleep(1)
            shoppingCard_Page.inputConsignCode(self.user_list[i][self.inputConsignPostalCode])
            sleep(4)
            try:
                if self.user_list[i][self.expectedResult] in self.driver.page_source:
                    self.excelMethod.saveExcel(self.user_list[i][self.index]+1, 'pass')
            except:
                self.excelMethod.saveExcel(self.user_list[i][self.index]+1, 'fail')
                self.logger.error(u'第%s行用例执行失败' % (i + 4))
                ScreenShot().screenShot(self.driver)

        # 点击保存地址
        self.shoppingCartPage.saveAddress()
        sleep(2)

        # 选择配送快递
        # self.shoppingCartPage.selectExpressSf()
        # sleep(4)
        #
        # # 选择配送日期
        # self.shoppingCartPage.selectWeekends()
        # sleep(4)
        #
        # # 点击保存配送方式
        # self.shoppingCartPage.saveDistributionmode()
        # sleep(4)

        # 提交订单
        self.shoppingCartPage.submitOrder()
        sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        sleep(1)

if __name__ == '__main__':
    unittest.TestCase()