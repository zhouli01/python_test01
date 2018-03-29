# coding:utf-8
List1=[2,5,4,8,3,1,9]
List1=sorted(List1)
print("打印原来的数组:",List1)

num=int(input("请输入一个数:"))
List1.append(num)
print("打印新的数组:",sorted(List1))