#!usr/bin/python
#coding:UTF-8
n = int(input("输入人数："))
data = [i+1 for i in range(20)]
print(data)



l=[ input("please input a number:\n") for i in range(5)]
print(l)

List=[]
for i in range(1,n+1):
	List.append(i)
sum=0
while 1:
	t=0
	for i in range(1,len(List)+1):
		sum+=1
		if (sum)%3==0:
			List.pop(i-t-1)
			t+=1
	if len(List)==1:
		print ("最后留下的：%d"% List[0])
		break