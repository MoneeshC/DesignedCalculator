from tkinter import *
from PIL import ImageTk,Image


root =  Tk()

e=Entry(root,fg="Blue",width=30,borderwidth=10)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

#buttons section
img_dot=Image.open("imgs\dot.png")
img_dot = ImageTk.PhotoImage(img_dot)

img_zero=Image.open("imgs\zero.png")
img_zero = ImageTk.PhotoImage(img_zero)

img_eq=Image.open("imgs\equal.png")
img_eq = ImageTk.PhotoImage(img_eq)

img_one=Image.open("imgs\\one.png")
img_one = ImageTk.PhotoImage(img_one)

img_two=Image.open("imgs\\two.png")
img_two = ImageTk.PhotoImage(img_two)

img_three=Image.open("imgs\\three.png")
img_three = ImageTk.PhotoImage(img_three)

img_four=Image.open("imgs\\four.png")
img_four = ImageTk.PhotoImage(img_four)

img_five=Image.open("imgs\\five.png")
img_five = ImageTk.PhotoImage(img_five)

img_six=Image.open("imgs\\six.png")
img_six = ImageTk.PhotoImage(img_six)

img_seven=Image.open("imgs\\seven.png")
img_seven = ImageTk.PhotoImage(img_seven)

img_eight=Image.open("imgs\\eight.png")
img_eight = ImageTk.PhotoImage(img_eight)

img_nine=Image.open("imgs\\nine.png")
img_nine = ImageTk.PhotoImage(img_nine)

img_back=Image.open("imgs\\back.png")
img_back = ImageTk.PhotoImage(img_back)

img_del=Image.open("imgs\\del.png")
img_del = ImageTk.PhotoImage(img_del)

img_slash=Image.open("imgs\\slash.png")
img_slash = ImageTk.PhotoImage(img_slash)

img_mul=Image.open("imgs\\star.png")
img_mul = ImageTk.PhotoImage(img_mul)

img_min=Image.open("imgs\\min.png")
img_min = ImageTk.PhotoImage(img_min)

img_add=Image.open("imgs\\add.png")
img_add = ImageTk.PhotoImage(img_add)

#im_1=Image.open("imgs\1.png")


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

Bu1=Button(root,image=img_one,borderwidth=0,command=lambda: button_click(1))
Bu2=Button(root,image=img_two,borderwidth=0,command=lambda: button_click(2))
Bu3=Button(root,image=img_three,borderwidth=0,command=lambda: button_click(3))
Bu4=Button(root,image=img_four,borderwidth=0,command=lambda: button_click(4))
Bu5=Button(root,image=img_five,borderwidth=0,command=lambda: button_click(5))
Bu6=Button(root,image=img_six,borderwidth=0,command=lambda: button_click(6))
Bu7=Button(root,image=img_seven,borderwidth=0,command=lambda: button_click(7))
Bu8=Button(root,image=img_eight,borderwidth=0,command=lambda: button_click(8))
Bu9=Button(root,image=img_nine,borderwidth=0,command=lambda: button_click(9))

Bus1=Button(root,image=img_back,borderwidth=0,command=None)
Bus2=Button(root,image=img_del,borderwidth=0,command=clear)
Bus3=Button(root,image=img_slash,borderwidth=0,command=div)
Bus4=Button(root,image=img_mul,borderwidth=0,command=mul)
Bus5=Button(root,image=img_min,borderwidth=0,command=sub)
Bus6=Button(root,image=img_add,borderwidth=0,command=add)
Bus10=Button(root,image=img_eq,borderwidth=0,command=eq)
Bus8=Button(root,image=img_zero,borderwidth=0,command=lambda: button_click(0))

Bus7=Button(root,image=img_dot,borderwidth=0,command=None)

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
Bus6.grid(row=3,column=3,rowspan=2)
Bus7.grid(row=5,column=0)
Bus8.grid(row=5,column=1)
Bus10.grid(row=5,column=2,columnspan=2)


root.mainloop()
 
 

