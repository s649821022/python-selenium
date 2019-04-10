# Date：9/3/2019
# Name:kobe
# -*- coding:utf-8 -*-


from common.readConfig import ReadConfig
"""
    url思路：1.从config.ini文件中获取标签和host
             2.创建url对象并添加刚才获取的
             3.返回url    
"""

def getUrl(url, logger):
    config = ReadConfig(logger)
    configUrl = config.readConfig('browser', 'host')
    url = configUrl + url
    return url
