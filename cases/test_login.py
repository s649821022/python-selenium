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
from common.geturl import *
from common.browser_setup import *
from common.geturl import getUrl
from common.screen_shot import *

class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.logger = LoggingMethod().getLogger()
        cls.ReadConfig = ReadConfig(cls.logger)
        cls.driver = BrowserSetup(cls.logger).browserSetup()
        cls.url = getUrl('/iwebshop/', cls.logger)
        cls.driver.get(cls.url)
        cls.inputName = int(cls.ReadConfig.readConfig('loginInfo', 'inputName'))
        cls.inputPassword = int(cls.ReadConfig.readConfig('loginInfo', 'inputPassword'))
        cls.expectedResult = int(cls.ReadConfig.readConfig('loginInfo', 'expectedResult'))
        cls.isExecute = int(cls.ReadConfig.readConfig('loginInfo', 'isExecute'))
        cls.testResult = int(cls.ReadConfig.readConfig('loginInfo', 'testResult'))
        cls.data_path = os.path.dirname(os.path.abspath('.')) + '\\data\\' + 'login.xlsx'
        cls.excelmethod = ExcelMethod(cls.logger, cls.data_path)
        cls.user_list = cls.excelmethod.readExcel('Sheet1', cls.isExecute)


    def test_login(self):
        # 点击进入登录页面
        enter_LoginPage = MainPage(self.driver, self.logger)
        enter_LoginPage.enter_loginPage()
        for i in range(0, len(self.user_list)):
            login_Page = LoginPage(self.driver, self.logger)
            login_Page.input_username(self.user_list[i][self.inputName])
            sleep(1)
            login_Page.input_password(self.user_list[i][self.inputPassword])
            sleep(1)
            login_Page.click_submit()
            sleep(1)
            try:
                if self.user_list[i][self.expectedResult] in self.driver.page_source:
                    self.excelmethod.saveExcel(i + 2, 'pass')
            except:
                self.excelmethod.saveExcel(i + 2, 'fail')
                self.logger.error(u'第%s行用例执行失败' % (i + 2))
                ScreenShot().screenShot(self.driver)





    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
















if __name__ == '__main__':
    unittest.main()
