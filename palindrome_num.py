#!/usr/bin/env python3

#a = input("输入一串数字: ")
#b = a[::-1]




a=input("请输入字符：")
#print (len(s))
for i in range(len(a)-1,-1,-1):
    b=print(a[i],end='')
if a == b:
    print("\n%s 是回文"% a)
else:
    print("\n%s 不是回文"% a)