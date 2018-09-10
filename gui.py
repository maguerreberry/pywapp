from Tkinter import Tk, Label, Entry, Button, END, FIRST
from ScrolledText import ScrolledText
from FileDialog import FileDialog
import tkFileDialog

window = Tk()
 
window.title("Wapp Spammer")
 
window.geometry('1280x720')
 
lbl = Label(window, text="Hello")
 
lbl.grid(column=0, row=0)
  
txt = ScrolledText(window,width=40,height=10)
 
txt.grid(column=0,row=1)

def clicked():
 
    print "Text =", txt.get(index1="1.0", index2='end-1c')
  
btn = Button(window, text="Click Me", command=clicked)
 
btn.grid(column=0, row=2)

def get_file():
    # filed = FileDialog(window)
    filed = tkFileDialog.askopenfilename(initialdir = "C:/%\userprofile%", title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    
    print filed

btn = Button(window, text="Image", command=get_file)
 
btn.grid(column=1, row=2)

window.mainloop()