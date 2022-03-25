from tkinter import *
from datetime import datetime,date
app=Tk()
app.geometry('200x200')

def age_calc(birth_date):
    if '/' in birth_date:
        birth_d=datetime.strptime(birth_date,'%d/%m/%Y')
        curr_d=date.today()
        age=curr_d.year-birth_d.year-((curr_d.month,curr_d.day)<(birth_d.month,birth_d.day))
        screen.config(text=age) 
    elif  '-' in birth_date:
        birth_d=datetime.strptime(birth_date,'%d-%m-%Y')
        curr_d=date.today()
        age=curr_d.year-birth_d.year-((curr_d.month,curr_d.day)<(birth_d.month,birth_d.day))
        screen.config(text=age)  
    elif birth_date=="":
        screen.config(text='error')  
    
cal_label=Label(app,text="AGE CALCULATOR",bg="black",fg="white",font=("Calibri",20,'bold'))
cal_label.pack(side=TOP)

screen=Label(app,width=25,height=1,text="",font=("Arial",30),bg='light grey',fg='black')
screen.pack()

e=Entry(app,borderwidth=5,font=('arial,30,bold'))
e.pack()

Button(app,text="Calulate",width="6",height='2',font=('arial,30,bold'),command=lambda:age_calc(e.get())).place(x=50,y=120)

app.resizable(False,False)
app.mainloop()