import re

pattern = re.compile(r'\d+')                    # 用于匹配至少一个数字
m1 = pattern.match('one12twothree34four')        # 查找头部，没有匹配
print ('m1 is:',m1)

m2 = pattern.match('one12twothree34four', 2, 10) # 从'e'的位置开始匹配，没有匹配
print ('m2 is:',m2)

m3 = pattern.match('one12twothree34four', 3, 10) # 从'1'的位置开始匹配，正好匹配
print ('m3 is:',m3)                                        # 返回一个 Match 对象

m3.group(0)   # 可省略 0
m3.start(0)   # 可省略 0
m3.end(0)     # 可省略 0
m3.span(0)    # 可省略 0