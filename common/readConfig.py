# Date：9/3/2019
# Name:kobe
# -*- coding:utf-8 -*-

import configparser
import os
class ReadConfig(object):
    def __init__(self, logger):
        self.logger = logger
    def readConfig(self, tagName, name):
        try:
            cf = configparser.ConfigParser()
            cfpath = os.path.dirname(os.path.abspath('.')) + '\\config\\config.ini'
            cf.read(cfpath)
            res_name = cf.get(tagName, name)
            return res_name
        except:
            self.logger.error('读取配置信息错误，tagName为%s, name为%s' % (tagName, name))


