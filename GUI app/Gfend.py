from tkinter import *
import Gbend

window=Tk()

l1=Label(window, text='Port Name')
l1.grid(row=0,column=0)

l2=Label(window, text='Country')
l2.grid(row=0,column=2)

l3=Label(window, text='Last POC')
l3.grid(row=1,column=0)

l4=Label(window, text='Visit (if any)')
l4.grid(row=1,column=2)

l5=Label(window, text='Date of visit')
l5.grid(row=2,column=2)

port_name_text = StringVar()
e1=Entry(window, textvariable=port_name_text)
e1.grid(row=0,column=1)

country_text = StringVar()
e2=Entry(window, textvariable=country_text)
e2.grid(row=1,column=1)

last_poc_text = StringVar()
e3=Entry(window, textvariable=last_poc_text)
e3.grid(row=0,column=3)

visit_text = StringVar()
e4=Entry(window, textvariable=visit_text)
e4.grid(row=1,column=3)

date_of_visit_text = StringVar()
e5=Entry(window, textvariable=date_of_visit_text)
e5.grid(row=2,column=3)

list1=Listbox(window, height=6,width=35)
list1.grid(row=3,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=3,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview())

b1=Button(window,text='View All', width=15)
b1.grid(row=3,column=3)

b2=Button(window,text='Search', width=15)
b2.grid(row=4,column=3)

b3=Button(window,text='Add entry', width=15)
b3.grid(row=5,column=3)

b4=Button(window,text='Update selected', width=15)
b4.grid(row=6,column=3)

b5=Button(window,text='Delete selected', width=15)
b5.grid(row=7,column=3)

b6=Button(window,text='Close', width=10)
b6.grid(row=9,column=3)

window.mainloop()
