#!usr/bin/python
#coding:UTF-8
n=int(input('please input a num:'))
n1=n
l=[]

while n>1:
	for i in range (2,n+1):
		if n%i==0:
			n=n//i
			l.append(str(i))
			break
			
print ("因数分解：" '%d='  %n1+'*'.join(l))


sum=0
for num  in l:
	num=int(num)
	sum += num
print ("因数的最小和：",sum)


