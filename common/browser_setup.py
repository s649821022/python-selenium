# Date：9/3/2019
# Name:kobe
# -*- coding:utf-8 -*-


from selenium import webdriver
from common.readConfig import ReadConfig

class BrowserSetup(object):
    def __init__(self, logger):
        self.logger = logger
        self.config = ReadConfig(logger)
        self.browserName = self.config.readConfig('browser', 'browserName')
        self.browserName = self.browserName.lower()

    def browserSetup(self):
        if self.browserName == 'chrome':
            return webdriver.Chrome()
        elif self.browserName == 'firefox':
            return webdriver.Firefox()
        elif self.browserName == 'ie':
            return webdriver.Ie()
        else:
            self.logger.error("浏览器名称有误 %s" % self.browserName)

if __name__ == '__main__':
    from common.logging_method import LoggingMethod
    logger = LoggingMethod().getLogger()
    browser = BrowserSetup(logger).browserSetup()


