from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("285x352")
root.title("CALCULATOR")

cal_label=Label(root,text="CALCULATOR",bg="black",fg="white",font=("Calibri",20,'bold'))
cal_label.pack(side=TOP)

result=""
def clear():
    global result
    result=""
    screen.config(text=result)
def equation(val):
    global result
    result+=val 
    if len(result)<=13:   
        screen.config(text=result)
    else:
        screen.config(text='not more than 13')
def calc():
    global result
    res=''
    if result!="":
        try:
            res= eval(result) 
        except:
            res="error"  
            result=''  
    screen.config(text=res)           

screen=Label(root,width=25,height=1,text="",font=("Arial",30),bg='light grey',fg='black')
screen.pack()


Button(root,text="c",width="6",height='2',font=('arial,30,bold'),command=lambda:clear()).place(x=10,y=100)
Button(root,text="/",width="6",height='2',font=('arial,10,bold'),command=lambda:equation('/')).place(x=80,y=100)
Button(root,text="%",width="6",height='2',font=('arial,30,bold'),command=lambda:equation('%')).place(x=150,y=100)
Button(root,text="*",width="6",height='2',font=('arial,30,bold'),command=lambda:equation('*')).place(x=220,y=100)

Button(root,text="7",width="6",height='2',font=('arial,30,bold'),command=lambda:equation('7')).place(x=10,y=150)
Button(root,text="8",width="6",height='2',font=('arial,30,bold'),command=lambda:equation('8')).place(x=80,y=150)
Button(root,text="9",width="6",height='2',font=('arial,30,bold'),command=lambda:equation('9')).place(x=150,y=150)
Button(root,text="-",width="6",height='2',font=('arial,30,bold'),command=lambda:equation('-')).place(x=220,y=150)

Button(root,text="4",width="6",height='2',font=('arial,30,bold'),command=lambda:equation('4')).place(x=10,y=200)
Button(root,text="5",width="6",height='2',font=('arial,30,bold'),command=lambda:equation('5')).place(x=80,y=200)
Button(root,text="6",width="6",height='2',font=('arial,30,bold'),command=lambda:equation('6')).place(x=150,y=200)
Button(root,text="+",width="6",height='2',font=('arial,30,bold'),command=lambda:equation('+')).place(x=220,y=200)

Button(root,text="1",width="6",height='2',font=('arial,30,bold'),command=lambda:equation('1')).place(x=10,y=250)
Button(root,text="2",width="6",height='2',font=('arial,30,bold'),command=lambda:equation('2')).place(x=80,y=250)
Button(root,text="3",width="6",height='2',font=('arial,30,bold'),command=lambda:equation('3')).place(x=150,y=250)
Button(root,text="=",width="6",height='6',font=('arial,30,bold'),command=lambda:calc()).place(x=220,y=250)

Button(root,text="0",width="10",height='2',font=('arial,30,bold'),command=lambda:equation('0')).place(x=10,y=300)
Button(root,text=".",width="6",height='2',font=('arial,100,bold'),command=lambda:equation('.')).place(x=130,y=300)


root.resizable(False,False)
root.mainloop()
