import win32gui
import win32api
from colorlist import *
import tkinter, win32api, win32con, pywintypes
import os
import time
from threading import Thread 
hwnd = win32gui.GetDC(win32gui.GetActiveWindow())
def fillall(color):
	colorx = win32api.RGB(color[0], color[1], color[2])
	for x in range(0, 1919):                                          # fill all display
		for y in range(0, 1079):
			win32gui.SetPixel(hwnd, x, y, colorx)
def draw(x,y,x2,y2,color):
	colorx = win32api.RGB(color[0], color[1], color[2])                # fill area from point to point 
	for i in range(x, x2):
		for j in range(y, y2):
			win32gui.SetPixel(hwnd, i, j, colorx)
def d(x,y,lenx,color, step, d):
	colorx = win32api.RGB(color[0], color[1], color[2]) 
	if d == "rl":
		for b in range(lenx):
			win32gui.SetPixel(hwnd, x, y, colorx)             # make diagonal from point to point with valueable step
			x += 1
			y += step
	elif d == "rh":
		for b in range(lenx):
			win32gui.SetPixel(hwnd, x, y, colorx)             # make diagonal from point to point with valueable step
			x += 1
			y -= step
	elif d == "ll":
		for b in range(lenx):
			win32gui.SetPixel(hwnd, x, y, colorx)             # make diagonal from point to point with valueable step
			x -= 1
			y += step
	elif d == "lh":
		for b in range(lenx):
			win32gui.SetPixel(hwnd, x, y, colorx)             # make diagonal from point to point with valueable step
			x -= 1
			y -= step


def ttsx(param,fontx,fgx,bgx):
	global status
	status = False
	label = tkinter.Label(text=param, font=('Times New Roman',str(fontx)), fg=fgx, bg=bgx)
	label.master.overrideredirect(True)
	label.master.geometry("+250+250")
	label.master.lift()
	label.master.wm_attributes("-topmost", True)
	label.master.wm_attributes("-disabled", True)
	label.master.wm_attributes("-transparentcolor", "white")	
	hWindow = pywintypes.HANDLE(int(label.master.frame(), 16))
	# http://msdn.microsoft.com/en-us/library/windows/desktop/ff700543(v=vs.85).aspx
	# The WS_EX_TRANSPARENT flag makes events (like mouse clicks) fall through the window.
	exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT
	win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)
	label.pack()
	label.mainloop()
	time.sleep(2)
	label.quit()
def tts(text, font, fg, bg):
	t1 = Thread(target=ttsx, args=(text,font,fg,bg))
	t1.start()
	time.sleep(1)
	global label
	label.quit()
def enttsx():
	global label
	label.quit()
	print("quited")
def endtts():
	t2 = Thread(target=enttsx)
	t2.start()
	print("started")