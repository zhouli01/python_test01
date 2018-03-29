


# x=1
# for i in   range(0,9):
# 	x =(x+1)*2
# print ("总数:",x)


# coding:utf-8
# 猴子分桃，最少问题分析：问最少有多少只桃子，则岸上最后剩的桃子数目越小，则原岸上的桃子越少
# 假设最后岸上还剩4x只桃子,可以利用递归方法求解

num = int(input("输入猴子的数目:"))
def fn(n):
	if n == num:
		return (4 * x)  # 最后剩的桃子的数目
	
	else:
		return (fn(n + 1) * 5 / 4 + 1)
	
	
x = 1
while 1:
	count = 0
	for i in range(1, num):
		if fn(i) % 4 == 0:
			count = count + 1
	if count == num - 1:
		print("海滩上原来最少有%d个桃子" % int(fn(0)))
		break
	else:
		x = x + 1
		



