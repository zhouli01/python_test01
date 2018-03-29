#!/usr/bin/python
# -*- coding: UTF-8 -*-

class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print ('self.__seceretCount is :',self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
#print('i1  is:', i1)

print ('publicCount is :' ,counter.publicCount)