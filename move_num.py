


#!/usr/bin/python
#coding:UTF-8
a=[1,2,3,4,5]
m=int(input("请输入移动的数："))


# L=len(a)
# if m > L:
# 	b=(a<<m)
# else:
# 	b=(a>>m)
# print (b)


for i in range(m):
	a.insert(0,a.pop())
print (a)

