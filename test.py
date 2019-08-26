from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os

def __init__(root, master = None):
	root.text = Text(top, height = 200, width = 200)
	root.text.pack()

def OpenFile():
	root.opens = filedialog.askopenfilename(initialdir = "c:/somesh/", title = "Select file", filetypes = (("text files","*.txt"),("all files","*.*")))
	with open(root.opens) as file:
		for i in file:
			root.text.insert(END,i)
	my_label = Label(root, text= root.opens).pack()
	
def SaveFile():
	root.saves = filedialog.asksaveasfilename(initialdir = "c:/somesh/", title = "Select file", filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
def About():
	root.msg = messagebox.showinfo("About","This is a simple Image Viewer. \nYou can open images and, \nsave them to another location")


root = Tk() 
root.title ("Python GUI - Demo")
root.iconbitmap('folder.ico')
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

# from tkinter import *
# from tkinter import filedialog

# root = Tk()
# root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
# print (root.filename)

# from tkinter import filedialog
# from tkinter import *

# root = Tk()
# root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
#print (root.filename)