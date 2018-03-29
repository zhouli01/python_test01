#!/usr/bin/python
# -*- coding: UTF-8 -*-#
#递归做，非常慢。计算n=36就要大概七八秒吧
def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print ("这个方法出奇的恶心慢：",fib(36))







