#!/usr/bin/python
# -*- coding: UTF-8 -*-

def Fib(n):
    a, b = 0, 1
    while n:
        a, b, n = b, a + b, n - 1
        print (a)
Fib(36)