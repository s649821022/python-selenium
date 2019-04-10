# Date：9/3/2019
# Name:kobe
# -*- coding:utf-8 -*-

from selenium.webdriver.common.by import By
from pages.basePage import BasePage


class LoginPage(BasePage):
    username = (By.NAME, 'login_info')
    password = (By.NAME, 'password')
    submit = (By.CLASS_NAME, 'submit_login')

    # 输入用户名
    def input_username(self, name):
        self.input_text(self.username, name)

    # 输入密码
    def input_password(self, pwd):
        self.input_text(self.password, pwd)

    # 点击登录按钮
    def click_submit(self):
        self.click(self.submit)

    # 清除用户名
    def clear_username(self):
        self.clear(self.username)

    # 清除密码
    def clear_password(self):
        self.clear(self.password)


