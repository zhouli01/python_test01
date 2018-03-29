#! /usr/bin/env python
# coding:utf-8

import time

D=input("请输入年份，格式如XXXX-XX-XX：")
d=time.strptime( D,'%Y-%m-%d').tm_yday
print ("the {} day of this year!" .format(d))