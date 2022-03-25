from tkinter import *
from tkinter import ttk
import csv

root = Tk()
root.title('PythonGuides')

root.geometry("1200x680+50+20")
m_tree = ttk.Treeview(root,selectmode='browse')
  

sb = Scrollbar( orient=VERTICAL)
sb.pack(side=RIGHT, fill=Y)
m_tree.config(yscrollcommand=sb.set)
sb.config(command=m_tree.yview)

m_tree["columns"]=('SNo','ObservationDate','Province/State','Country/Region','Last Update','Confirmed','Deaths','Recovered')
m_tree.column('#0', width=0, stretch=NO)
m_tree.column("SNo",width=50,anchor=W)
m_tree.column('ObservationDate',width=80,anchor=CENTER)
m_tree.column('Province/State',width=80,anchor=CENTER)
m_tree.column('Country/Region' ,width=100,anchor=CENTER)
m_tree.column('Last Update',width=100,anchor=CENTER)
m_tree.column('Confirmed',width=80,anchor=CENTER)
m_tree.column('Deaths',width=80,anchor=CENTER)
m_tree.column('Recovered',width=80,anchor=CENTER)

m_tree.heading('#0', text='', anchor=CENTER)
m_tree.heading('SNo', text='SNo', anchor=W)
m_tree.heading('ObservationDate', text='ObservationDate', anchor=CENTER)
m_tree.heading('Province/State', text='Province/State', anchor=CENTER)
m_tree.heading('Country/Region', text='Country/Region', anchor=CENTER)
m_tree.heading('Last Update', text='Last Update', anchor=CENTER)
m_tree.heading('Confirmed', text='Confirmed', anchor=CENTER)
m_tree.heading('Deaths', text='Deaths', anchor=CENTER)
m_tree.heading('Recovered', text='Recovered', anchor=CENTER)




count=0
with open("C:\\Users\\Gunja\\Desktop\\MyNotepad\\venv\\covid_19_data.csv",'r') as file:
    reader=csv.reader(file)
    for record in reader:
        m_tree.insert(parent='', index=count, iid=count, text='', values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7]))
        count+=1
     


m_tree.pack(fill='both',expand=True) 
root.mainloop()