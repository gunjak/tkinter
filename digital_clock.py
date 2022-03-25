from tkinter import *
import time
app=Tk()

def get_time():
    timevar=time.strftime("%I:%M:%S %p")
    clock.config(text=timevar)
    clock.after(200,get_time)
    
clock=Label(app,font=("Calibri",20))
clock.pack()
get_time()

app.resizable(False,False)
app.mainloop()