# Date：9/3/2019
# Name:kobe
# -*- coding:utf-8 -*-

import time


class TimeUntil(object):

    def currentDate(self):
        today = time.strftime('%Y-%m-%d')  # 2019-3-9
        return today

    def currentTime(self):
        now = time.strftime('%H_%M_%S')  # 9_52_35
        return now

    def currentDataTime(self):
        todayNow = time.strftime('%Y-%m-%d %H_%M_%S')  # 2019-3-9 9_52_35
        return todayNow

