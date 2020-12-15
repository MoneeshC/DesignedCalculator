from tkinter import *

root =  Tk()

e=Entry(root,fg="Blue",width=30,borderwidth=10)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)


#gets values
def button_click(n):
    val=e.get()
    e.delete(0,END)
    e.insert(0,str(val)+str(n))
    m=int(e.get())

def clear():
    e.delete(0,END)

#gets symbol
def add():
    f_num = e.get()
    global f
    global mat
    
    mat="Add"
    f=int(f_num)
    
    e.delete(0,END)

def div():
    f_num = e.get()
    global f
    global mat
    
    mat="div"
    f=int(f_num)
    
    e.delete(0,END)


def sub():
    f_num = e.get()
    global f
    global mat
    
    mat="sub"
    f=int(f_num)
    
    e.delete(0,END)

def mul():
    f_num = e.get()
    global f
    global mat
    
    mat="mul"
    f=int(f_num)
    
    e.delete(0,END)
    
def eq():
    sn=e.get()
    e.delete(0,END)
    
    if mat=="Add":    
        e.insert(0, f + int(sn))
    if mat=="sub":    
        e.insert(0, f - int(sn))
    if mat=="div":    
        e.insert(0, f / int(sn))
    if mat=="mul":    
        e.insert(0, f * int(sn))

d=20
c="#fffff1"

Bu1=Button(root,text="1",bg=c,padx=d,command=lambda: button_click(1))
Bu2=Button(root,text="2",bg=c,padx=d,command=lambda: button_click(2))
Bu3=Button(root,text="3",bg=c,padx=d,command=lambda: button_click(3))
Bu4=Button(root,text="4",bg=c,padx=d,command=lambda: button_click(4))
Bu5=Button(root,text="5",bg=c,padx=d,command=lambda: button_click(5))
Bu6=Button(root,text="6",bg=c,padx=d,command=lambda: button_click(6))
Bu7=Button(root,text="7",bg=c,padx=d,command=lambda: button_click(7))
Bu8=Button(root,text="8",bg=c,padx=d,command=lambda: button_click(8))
Bu9=Button(root,text="9",bg=c,padx=d,command=lambda: button_click(9))

Bus1=Button(root,text="<",bg=c,padx=d,command=None)
Bus2=Button(root,text="del",bg=c,padx=d,command=clear)
Bus3=Button(root,text="/",bg=c,padx=d,command=div)
Bus4=Button(root,text="*",bg=c,padx=d,command=mul)
Bus5=Button(root,text="-",bg=c,padx=d,command=sub)
Bus6=Button(root,text="+",bg=c,padx=d-4,command=add)
Bus10=Button(root,text="Enter",bg=c,padx=d-4,command=eq)
Bus8=Button(root,text="0",bg=c,padx=d,command=lambda: button_click(0))

Bus7=Button(root,text=".",bg=c,padx=d,command=None)

Bu3.grid(row=4,column=2)
Bu2.grid(row=4,column=1)
Bu1.grid(row=4,column=0)
Bu4.grid(row=3,column=2)
Bu5.grid(row=3,column=1)
Bu6.grid(row=3,column=0)
Bu7.grid(row=2,column=2)
Bu8.grid(row=2,column=1)
Bu9.grid(row=2,column=0)

Bus1.grid(row=1,column=0)
Bus2.grid(row=1,column=1)
Bus3.grid(row=1,column=2)
Bus4.grid(row=1,column=3)
Bus5.grid(row=2,column=3)
Bus6.grid(row=3,column=3)
Bus7.grid(row=5,column=0)
Bus8.grid(row=5,column=1)
Bus10.grid(row=5,column=2)


root.mainloop()
 
 

