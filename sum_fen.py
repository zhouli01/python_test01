

a=2
b=1
s=0
for i in range(0,20):
	s+=a/b
	t=a
	a=a+b
	b=t
print (s)



#!/usr/bin/python
# -*- coding: UTF-8 -*-

s=0
def fact(n):
	if n==1:
		return 1
	return n*fact(n-1)

for n in  range(1,3):
   a=fact(n)
   s+=a
print("结果是：",s)




def Factorial(n):
    if n == 1:
        fn=1
    else:
        fn = n*Factorial(n-1)
    return fn
print("Factorial(5)=",Factorial(5))








