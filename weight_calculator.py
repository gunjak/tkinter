from tkinter import *
from tkinter import ttk
app=Tk()
app.geometry("300x400")
kilogram={"tonne":0.001,
            'kilogram':1,
            'gram':1000,
            'milligram':10e+6,
            'microgram':10e+9,
            'imperial tone':0.000984207,
            'US tone':0.00110231,
            'stone':0.157473,
            'pound':2.20462,
            'ounce':35.274}

def cal(textbox1,textbox2,choose,choose1,kilogram):
    textbox2.delete(0,END)
    num=(kilogram[choose1.get()]/kilogram[choose.get()])*float(textbox1.get())
    textbox2.insert(0,str(num))

            
  
weight_var=["tonne",
            'kilogram',
            'gram',
            'milligram',
            'microgram',
            'imperial tone',
            'US tone',
            'stone',
            'pound',
            'ounce']

text =StringVar()
textbox1= ttk.Entry(app, textvariable=text,width=20)
textbox1.insert(0,1)
textbox1.grid(column=0,row=0)
choose=StringVar()
choose.set(weight_var[1])


combo1=ttk.Combobox(width=20,textvariable=choose,state='readonly')
combo1['values']=weight_var
combo1.current(4)
combo1.grid(column=0,row=1)

text1 =StringVar()
textbox2 = ttk.Entry(app, textvariable=text1)
textbox2.grid(row=0,column=1)

choose1=StringVar()
choose1.set(weight_var[1])

combo2=ttk.Combobox(width=20,textvariable=choose1,state='readonly')
combo2['values']=weight_var
combo2.current(4)
combo2.grid(column=1,row=1,padx=2)

b=Button(app,text='Enter',width='20',height='2',command=lambda:cal(textbox1,textbox2,choose,choose1,kilogram)).place(x=50,y=50)

app.resizable(False,False)
app.mainloop()