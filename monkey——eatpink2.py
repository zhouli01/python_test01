
if __name__ == '__main__':
	
	x=0
	i=0
	j=1
	while (i<5):
		x = 4 * j
		for i in range(0,5):
			if x %4 ==0:
				i=i+1
				x=x/4*5+1
			else:
				break
		j=j+1
	print (x)