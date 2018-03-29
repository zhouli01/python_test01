#!usr/bin/python
#coding:UTF-8
for i in range(1,10):
    print
    for j in range (1,i+1):
        k=i*j
        print ("%d*%d=%d "  %(j, i, i*j),end='')
    print ('\n')