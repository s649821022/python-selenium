# Date：10/3/2019
# Name:kobe
# -*- coding:utf-8 -*-


from selenium.webdriver.common.by import By
from pages.basePage import BasePage


class ShoppingCartPage(BasePage):

    consignee_name = (By.NAME, 'accept_name')
    def inputConsigneeName(self, name):
        self.input_text(self.consignee_name, name)

    province = (By.ID, 'province')
    def selectProvince(self, num):
        self.select_index(self.province, num)

    city = (By.ID, 'city')
    def selectCity(self, num):
        self.select_index(self.city, num)

    area = (By.ID, 'area')
    def selectArea(self, num):
        self.select_index(self.area, num)

    address = (By.NAME, 'address')
    def inputConsigneeAddress(self, address1):
        self.input_text(self.address, address1)

    teleMobile = (By.NAME, 'mobile')
    def inputConsignTeleMobile(self, telephone):
        self.input_text(self.teleMobile, telephone)

    mobile = (By.NAME, 'telphone')
    def inputConsignMobile(self, mobile1):
        self.input_text(self.mobile, mobile1)

    code = (By.NAME, 'zip')
    def inputConsignCode(self, code1):
        self.input_text(self.code, code1)

    save_address = (By.CSS_SELECTOR, '#address_save_button > input[type="button"]')
    def saveAddress(self):
        self.click(self.save_address)

    # 配送方式
    china = (By.ID, 'delivery1')
    shentong = (By.ID, 'delivery2')
    shunfeng = (By.ID, 'delivery3')
    oneone = (By.ID, 'delivery4')
    # chinaList = list(china)
    # shengtongList = list(shentong)
    # shunfengList = list(shunfeng)
    # oneoneList = list(oneone)
    # list = []
    # list.append(chinaList)
    # list.append(shengtongList)
    # list.append(shunfengList)
    # list.append(oneoneList)

    def selectExpressCh(self):
        self.click(self.china)

    def selectExpressSto(self):
        self.click(self.shentong)

    def selectExpressSf(self):
        self.click(self.shunfeng)

    def selectExpress11(self):
        self.click(self.oneone)

    # 配送时间
    everyTime = (By.XPATH, '//*[@id="delivery_form"]/tfoot/tr/td/label[1]/input')
    weekdays = (By.XPATH, '//*[@id="delivery_form"]/tfoot/tr/td/label[2]/input')
    weekends = (By.XPATH, '//*[@id="delivery_form"]/tfoot/tr/td/label[3]/input')
    def selectEveryTime(self):
        self.click(self.everyTime)
    def selectWeendays(self):
        self.click(self.weekdays)
    def selectWeekends(self):
        self.click(self.weekends)

    # 保存配送方式
    saveDistribution = (By.ID, 'delivery_save_button')
    def saveDistributionmode(self):
        self.click(self.saveDistribution)

    # 提交订单
    submit_order = (By.CLASS_NAME, 'submit_order')
    def submitOrder(self):
        self.click(self.submit_order)
