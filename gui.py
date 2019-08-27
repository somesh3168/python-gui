from tkinter import *
from tkinter import filedialog
root = Tk() 
#root.opens = filedialog.askopenfilename(initialdir = "c:/somesh/", title = "Select file", filetypes = (("text files","*.txt"),("all files","*.*")))
T = Text(root, height=20, width=30) 
T.pack() 
T.insert(END, 'abc\ndef\n') 
mainloop() 
