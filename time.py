
import time;
ticks = time.time();
print ("unix当前时间戳:",ticks)

localtime=time.localtime(time.time())
print ("本地时间：",localtime)


localtime1=time.asctime(time.localtime(time.time()))
print ("本地标准模式时间：",localtime1)



print("格式化时间：",  time.strftime("%Y-%m-%d  %H:%M:%S %Y",time.localtime()))

#将格式字符串转换为时间戳
a=localtime1;
print("格式化时间转换为时间戳：",  time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y") ))

