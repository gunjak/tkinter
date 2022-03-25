from tkinter import *
from tkinter import filedialog,messagebox
import os
root=Tk()
root.geometry("200x250")
root.title("FILE EXPLORER")

label=Label(root,font=('Calibri','20','bold'))
label.config(text="FILE EXPLORER")
label.pack()

def openfile():
    file = filedialog.askopenfilename(title='Choose a file of any type', filetypes=[("All files", "*.*")])
    os.startfile(os.path.abspath(file))
def openfolder():
    folder = filedialog.askdirectory(title="Select Folder to open")
    os.startfile(folder)
def openfiles():
    file = filedialog.askopenfilenames(title='Choose a file of any type', filetypes=[("All files", "*.*")])
    for f in file:
        os.startfile(os.path.abspath(f))
def saveas():
    file=filedialog.asksaveasfile(filetypes=[("All Files","*.*"),("Text Documents","*.*")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file))

Button(root,text="openfile",width="10",height='2',font=('arial,30,bold'),command=lambda:openfile()).place(x=50,y=50)
Button(root,text="openfolder",width="10",height='2',font=('arial,30,bold'),command=lambda:openfolder()).place(x=50,y=100)       
Button(root,text="openfiles",width="10",height='2',font=('arial,30,bold'),command=lambda:openfiles()).place(x=50,y=150)    
Button(root,text="saveas",width="10",height='2',font=('arial,30,bold'),command=lambda:saveas()).place(x=50,y=200)     
           
root.resizable(False,False)   
root.mainloop()
      