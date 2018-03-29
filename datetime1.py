#使用datetime模块来获取当前的日期和时间

#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import datetime
#from datetime import datetime

i = datetime.datetime.now()
print ("当前的日期和时间是 %s" % i)
print ("ISO格式的日期和时间是 %s" % i.isoformat() )
print ("当前的年份是 %s" %i.year)
print ("当前的月份是 %s" %i.month)
print ("当前的日期是  %s" %i.day)
print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
print ("当前小时是 %s" %i.hour)
print ("当前分钟是 %s" %i.minute)
print ("当前秒是  %s" %i.second)

#把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式
print (time.ctime(time.time()))



#time localtime() 函数类似gmtime()，作用是格式化时间戳为本地的时间
print (time.asctime(time.localtime(time.time())))


#gmtime() 函数将一个时间戳转换为UTC时区（0时区）的struct_time
print (time.asctime(time.gmtime(time.time())))
