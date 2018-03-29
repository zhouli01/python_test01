#!/usr/bin/python3

import random

for i in range(0,7):
    a = random.randint(0,50)
    print(a,'\n')
    for j in range(0,a):
        print('*',end='')
    print('\n')