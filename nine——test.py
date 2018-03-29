



b=int(input('input a number：\n'))

a=9
n=1
while 1:
	if a % b==0:
		break
	else:
		a=a*10+9
		n+=1

print ('%d 个9 除以 %d为整数' % (n,b))