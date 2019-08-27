from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os

def OpenFile():
	x = filedialog.askopenfilename(initialdir = "c:/", filetypes = (("text files","*.txt"),("all files","*.*")))
	global T
	T = Text(root)
	T.pack()
	T.insert(END,open(x).read())
	
def SaveFile():
	saves = filedialog.asksaveasfile(mode ='w', initialdir = "c:/",  title = "Select file", filetypes = (("text files","*.txt"),("all files","*.*")))
	if saves is None:
		return
	text2save = str(T.get(1.0, END))
	saves.write(text2save)
	saves.close()	
def About():
	root.msg = messagebox.showinfo("About","This is a simple Text Editor. \nYou can open text files and, \nsave them to different locations")


root = Tk() 
root.title ("TextPad - Demo")
root.iconbitmap('Python.ico')
root.geometry('350x250')
msg = Label(root, text="\nOpen,Edit, and Save Your text files\n \n\n Simple is better than Complex.",background='teal')
msg.pack()
root.configure(background='teal')
menu = Menu(root) 
root.config(menu=menu) 
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
