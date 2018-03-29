from tkinter import *
import time
import random

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
bg = PhotoImage(file="E:\\back.gif")
for x in range(0, 2):
	for y in range(0, 1):
		canvas.create_image(x * 100, y * 100, image=bg, anchor='nw')


class Ball:
	def __init__(self, canvas, paddle, color):
		self.canvas = canvas
		self.paddle = paddle
		self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
		self.canvas.move(self.id, 245, 100)
		self.x = 0
		self.y = 0
		self.canvas_width = self.canvas.winfo_width()
		self.canvas_height = self.canvas.winfo_height()
		self.hit_bottom = False
		self.num = 0
		self.canvas.bind_all('<Button-1>', self.turn_sb)
	
	def turn_sb(self, evt):
		start = [-3, -2, -1, 1, 2, 3]
		random.shuffle(start)
		self.x = start[0]
		self.y = 3
	
	def hit(self, pos):
		pos_paddle = self.canvas.coords(self.paddle.id)
		if pos[3] <= pos_paddle[3] and pos[3] >= pos_paddle[1]:
			if pos[2] >= pos_paddle[0] and pos[0] <= pos_paddle[2]:
				return True
		return False
	
	def draw(self):
		self.canvas.move(self.id, self.x, self.y)
		pos = self.canvas.coords(self.id)
		if pos[0] <= 0:
			self.x = 3
		if pos[2] >= self.canvas_width:
			self.x = -3
		if pos[1] <= 0:
			self.y = 3
		if pos[3] >= self.canvas_height:
			self.hit_bottom = True
		if self.hit(pos) == True:
			self.y = -3
			self.num += 1


class Paddle:
	def __init__(self, canvas, color):
		self.canvas = canvas
		self.id = canvas.create_rectangle(0, 0, 200, 10, fill=color)
		self.canvas.move(self.id, 250, 330)
		self.x = 0
		self.canvas_width = self.canvas.winfo_width()
		self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
		self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
	
	def draw(self):
		self.canvas.move(self.id, self.x, 0)
		pos = self.canvas.coords(self.id)
		if pos[0] <= 0:
			self.x = 0
		if pos[2] >= self.canvas_width:
			self.x = 0
	
	def turn_left(self, evt):
		self.x = -4
	
	def turn_right(self, evt):
		self.x = 4


paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')

while 1:
	if ball.hit_bottom == False:
		ball.draw()
		paddle.draw()
		
	'''
	
	else:
		time.sleep(1)
		canvas.create_text(250, 150, text="游戏失败，继续努力", \
						   font=("Courier", 30), fill='yellow')
		string = "成功次数 %s "
		canvas.create_text(250, 180, text=string % ball.num, font=("Courier", 20), fill="yellow")
		break
	'''
	tk.update_idletasks()
	tk.update()
	time.sleep(0.01)
