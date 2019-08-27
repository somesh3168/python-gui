from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os

# def __init__(root, master = None):
# 	root.text = Text(top, height = 200, width = 200)
# 	root.text.pack()

def OpenFile():
	x = filedialog.askopenfilename(initialdir = "c:/somesh/", filetypes = (("text files","*.txt"),("all files","*.*")))
	global T
	T = Text(root)
	T.pack()
	T.insert(END,open(x).read())
	
	# root.opens = filedialog.askopenfile(mode ='r',initialdir = "c:/somesh/", title = "Select file", filetypes = (("text files","*.txt"),("all files","*.*")))
	# with open(root.opens) as file:
	# 	for i in file:
	# 		root.text.insert(END,i)
	#my_label = Label(root, text= root.opens).pack()
	
def SaveFile():
	#root.saves = filedialog.asksaveasfilename(initialdir = "c:/somesh/", title = "Select file", filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
	saves = filedialog.asksaveasfile(mode ='w', initialdir = "c:/somesh/",  title = "Select file", filetypes = (("text files","*.txt"),("all files","*.*")))
	#text = Text(root)
	#text.pack()
	if saves is None:
		return
	text2save = str(T.get(1.0, END))
	saves.write(text2save)
	saves.close()	
def About():
	root.msg = messagebox.showinfo("About","This is a simple Text Editor. \nYou can open txt files and, \nsave them to another location")


root = Tk() 
root.title ("Python GUI - Demo")
root.iconbitmap('folder.ico')
menu = Menu(root) 
root.config(menu=menu) 
#text = Text(root)
#text.pack()
file_menu = Menu(menu) 
menu.add_cascade(label='File', menu=file_menu) 

file_menu.add_command(label='Open', command = OpenFile)
file_menu.add_command(label='Save As', command= SaveFile)
file_menu.add_separator() 

file_menu.add_command(label='Exit', command=root.quit) 

helpmenu = Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About' , command = About) 

mainloop() 

