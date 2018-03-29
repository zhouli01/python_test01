#!usr/bin/python
#coding:UTF-8
#Python3.x 取整为 //
num =[]
for i in range (100, 1000):
	x= i//100
	y= i%100//10
	z= i%100%10
	if i == x**3+y**3+z**3:
		#if i == pow(x,3)+pow(y,3)+pow(z,3):
			num.append(i)
print (num)
print (len(num))




