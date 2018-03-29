#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
	from tkinter import *
	
	canvas = Canvas(width=800, height=600, bg='red')
	canvas.pack(expand=YES, fill=BOTH)
	k = 1
	
	for i in range(0, 3):
		#canvas.create_oval(400-k, 400-k,100+k, 100+k , width=8)
		canvas.create_line(400-k, 400-k,100+k, 100+k ,fill='black')
		k+=60
	
	
	'''
	
	for i in range(0, 10):
		canvas.create_oval(310 - k, 250 - k, 310 + k, 250 + k, width=5)
		k += j
		j += 3

	'''
	mainloop()