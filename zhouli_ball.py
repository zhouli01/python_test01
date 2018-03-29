#!/usr/bin/python
# -*- coding: UTF-8 -*-

#这是如此坑人的代码
from tkinter import *
top = Tk()
# 进入消息循环
#标题
top.title("Test")




#设置窗口的大小宽x高+偏移量
top.geometry('500x300')

#canvas = Canvas(top,bg='white')
canvas = Canvas(top, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()

bg = PhotoImage(file="E:\\back.gif")
for x in range(0, 2):
	for y in range(0, 2):
		canvas.create_image(x * 500, y * 400, image=bg, anchor='nw')
top.mainloop()