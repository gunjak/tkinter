from tkinter import *
import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfile
import os

if __name__=="__main__":
    app=Tk()
    app.title("My Notepad")
    app.geometry("900x400")
    text=Text(app,font='Calibri 13')
    text.pack(fill=BOTH,expand=True)
    file=None
    
    def newfile():
        global file
        app.title("untitled - Notepad")
        file=None
        text.delete(1.0,END)
        
    def openfile():
        global file
        file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file=="":
            file=None
        else:
              app.title(os.path.basename(file)+'Notepad')  
              text.delete(1.0,END)
              f=open(file,'r')
              text.insert(1.0,f.read())
              f.close()
    def savefile():
        global file
        if file==None:
            file=asksaveasfile(initialfile="Untitled file",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
            if file=="":
                file=None
            else:
                f=open(file,'w')
                f.write(text.get(1.0,END))  
                f.close() 
                app.title(os.path.basename(file)+"-Notepad")
                print("file saved")
        else: 
            f=open(file,'w')
            f.write(text.get(1.0,END))  
            f.close()     
        
    def exitfile():
        app.destroy()
    def cut():
        text.event_generate(("<<Cut>>"))
    def copy():
        text.event_generate(("<<Copy"))
    def paste():
        text.event_generate(("<<Paste>>")) 
    def about():
        showinfo("Notepad","Just Notepad")
                   
    
    Menubar=Menu(app)
    
    filemenu=Menu(Menubar,tearoff=False)
    filemenu.add_command(label='New',compound=LEFT,command=newfile)
    filemenu.add_command(label='Open',compound=LEFT,command=openfile)
    filemenu.add_command(label='Exit',compound=LEFT,command=exit)
    filemenu.add_command(label='Save',compound=LEFT,command=savefile)
    filemenu.add_command(label='Save as',compound=LEFT)
    Menubar.add_cascade(label="File",menu=filemenu)
    
    editmenu=Menu(Menubar,tearoff=False)
    editmenu.add_command(label='Cut',compound=LEFT,command=cut)
    editmenu.add_command(label='Copy',compound=LEFT,command=copy)
    editmenu.add_command(label='Paste',compound=LEFT,command=paste)
    Menubar.add_cascade(label="Edit",menu=editmenu)
    
    helpmenu=Menu(Menubar,tearoff=0)
    helpmenu.add_command(label='About NotePad',command=about)
    Menubar.add_cascade(label="Help",menu=helpmenu)
    
    scroll=Scrollbar(text)
    scroll.pack(side=RIGHT,fill=Y)
    scroll.config(command=text.yview)
    text.config(yscrollcommand=scroll.set)
    
    app.config(menu=Menubar)
    app.mainloop()
