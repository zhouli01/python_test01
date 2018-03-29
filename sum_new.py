#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input('n = '))
a = int(input('a = '))
sum = 0
total = 0
for i in range(n):
	sum+=(10**i)
	total += sum * a
print(total)