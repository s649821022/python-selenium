# Date：9/3/2019
# Name:kobe
# -*- coding:utf-8 -*-

import os
import time
import logging
from common.timeUntil import TimeUntil


# 同一天的日志输出到同一个log文件

class LoggingMethod(object):

    def getLogger(self):

        now = TimeUntil().currentDate()
        filename = os.path.dirname(os.path.abspath('.')) + '\\log\\' + now + '.log'
        # 第一步，创建logger对象
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        # 第二步，创建一个handler, 用于写入日志
        fh1 = logging.FileHandler(filename, encoding='utf-8')
        fh1.setLevel(logging.DEBUG)

        # 创建控制台输出
        consoleh = logging.StreamHandler()
        consoleh.setLevel(logging.WARNING)

        # 第三步，定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(pathname)s - %(lineno)s' + '行' + '- %(message)s')
        fh1.setFormatter(formatter)
        consoleh.setFormatter(formatter)

        # 第四步，将handlers添加到logger
        logger.addHandler(fh1)
        logger.addHandler(consoleh)

        return logger
if __name__ == '__main__':
    logger = LoggingMethod().getLogger()
    logger.info('测试info日志')

