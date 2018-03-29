#coding:utf-8


import datetime
begin = datetime.datetime.now()
for i in range(2,101):
    fg = 0
    for j in range(2,i-1):
        if i%j == 0:
            fg = 1
            break
    if fg == 0:
        print (i)
end = datetime.datetime.now()
k = end - begin
print("时间：",k.total_seconds())