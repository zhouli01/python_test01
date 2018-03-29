#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# def batoshi(num):
#     count=0
#     j=len(num)-1
#    # print ('j=',j)
#     for i in num:
#         count+=pow(8,j)*int(i)
#         j-=1
#     return count
#
# print(batoshi('12'))

num= (input("please input number:"))
j=len(num)-1
sum=0
for  i in  num:
     sum += (8**j)*int(i)
     j-=1
print (sum)