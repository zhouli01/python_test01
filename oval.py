if __name__ =='__main__':
	from tkinter import *
	x=360
	y=160
	top=y-30
	bottom=y-30
	
	top=50
	canvas=Canvas(width=400,height=600,bg='white')
	for i in range(20):
	#	canvas.create_oval(250-top,250-bottom,250+top,250+bottom)
		canvas.create_rectangle(20-2*i,20-2*i,20+10*i,20+10*i)
		canvas.create_oval(250 - 20, 250 - top, 250 + 20, 250 + top)
		top-=5
		bottom+=5
	canvas.pack()
	mainloop()
	