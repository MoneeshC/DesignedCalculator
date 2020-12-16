from tkinter import *
from PIL import ImageTk,Image


root =  Tk()

e=Entry(root,fg="Blue",width=30,borderwidth=2)
e.grid(row=0,column=0,columnspan=10,ipadx=45,ipady=10,pady=10)

#buttons section
m=72
n=64

img_dot=Image.open("imgs2\\dot.png")
img_dot = img_dot.resize((m//4, n//4), Image.ANTIALIAS)
img_dot = ImageTk.PhotoImage(img_dot)

img_zero=Image.open("imgs2\\zero.png")
img_zero = img_zero.resize((m, n), Image.ANTIALIAS)
img_zero = ImageTk.PhotoImage(img_zero)

img_eq=Image.open("imgs2\\equal.png")
img_eq = img_eq.resize((m*2, n), Image.ANTIALIAS)
img_eq = ImageTk.PhotoImage(img_eq)

img_one=Image.open("imgs2\\one.png")
img_one = img_one.resize(( n,m), Image.ANTIALIAS)
img_one = ImageTk.PhotoImage(img_one)

img_two=Image.open("imgs2\\two.png")
img_two = img_two.resize((m, n), Image.ANTIALIAS)
img_two = ImageTk.PhotoImage(img_two)

img_three=Image.open("imgs2\\three.png")
img_three = img_three.resize(( n,m), Image.ANTIALIAS)
img_three = ImageTk.PhotoImage(img_three)

img_four=Image.open("imgs2\\four.png")
img_four = img_four.resize((m, n), Image.ANTIALIAS)
img_four = ImageTk.PhotoImage(img_four)

img_five=Image.open("imgs2\\five.png")
img_five = img_five.resize((m, n), Image.ANTIALIAS)
img_five = ImageTk.PhotoImage(img_five)

img_six=Image.open("imgs2\\six.png")
img_six = img_six.resize((m, n), Image.ANTIALIAS)
img_six = ImageTk.PhotoImage(img_six)

img_seven=Image.open("imgs2\\seven.png")
img_seven = img_seven.resize((m, n), Image.ANTIALIAS)
img_seven = ImageTk.PhotoImage(img_seven)

img_eight=Image.open("imgs2\\eight.png")
img_eight = img_eight.resize((m, n), Image.ANTIALIAS)
img_eight = ImageTk.PhotoImage(img_eight)

img_nine=Image.open("imgs2\\nine.png")
img_nine = img_nine.resize((m, n), Image.ANTIALIAS)
img_nine = ImageTk.PhotoImage(img_nine)

img_back=Image.open("imgs2\\back.png")
img_back = img_back.resize((m, n), Image.ANTIALIAS)
img_back = ImageTk.PhotoImage(img_back)

img_del=Image.open("imgs2\\del.png")
img_del = img_del.resize((m, n+m//6), Image.ANTIALIAS)
img_del = ImageTk.PhotoImage(img_del)

img_slash=Image.open("imgs2\\slash.png")
img_slash = img_slash.resize((m, n), Image.ANTIALIAS)
img_slash = ImageTk.PhotoImage(img_slash)

img_mul=Image.open("imgs2\\star.png")
img_mul = img_mul.resize((m, n), Image.ANTIALIAS)
img_mul = ImageTk.PhotoImage(img_mul)

img_min=Image.open("imgs2\\min.png")
img_min = img_min.resize((m, n), Image.ANTIALIAS)
img_min = ImageTk.PhotoImage(img_min)

img_add=Image.open("imgs2\\add.png")
img_add = img_add.resize((m, n*2), Image.ANTIALIAS)
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
b=5

Bu1=Button(root,image=img_one,borderwidth=b,command=lambda: button_click(1))
Bu2=Button(root,image=img_two,borderwidth=b,command=lambda: button_click(2))
Bu3=Button(root,image=img_three,borderwidth=b,command=lambda: button_click(3))
Bu4=Button(root,image=img_four,borderwidth=b,command=lambda: button_click(4))
Bu5=Button(root,image=img_five,borderwidth=b,command=lambda: button_click(5))
Bu6=Button(root,image=img_six,borderwidth=b,command=lambda: button_click(6))
Bu7=Button(root,image=img_seven,borderwidth=b,command=lambda: button_click(7))
Bu8=Button(root,image=img_eight,borderwidth=b,command=lambda: button_click(8))
Bu9=Button(root,image=img_nine,borderwidth=b,command=lambda: button_click(9))

Bus1=Button(root,image=img_back,borderwidth=b,command=None)
Bus2=Button(root,image=img_del,borderwidth=b,command=clear)
Bus3=Button(root,image=img_slash,borderwidth=b,command=div)
Bus4=Button(root,image=img_mul,borderwidth=b,command=mul)
Bus5=Button(root,image=img_min,borderwidth=b,command=sub)
Bus6=Button(root,image=img_add,borderwidth=b,command=add)
Bus10=Button(root,image=img_eq,borderwidth=b,command=eq)
Bus8=Button(root,image=img_zero,borderwidth=b,command=lambda: button_click(0))

Bus7=Button(root,image=img_dot,borderwidth=b,command=None)

Bu3.grid(row=4,column=2)
Bu2.grid(row=4,column=1)
Bu1.grid(row=4,column=0)
Bu4.grid(row=3,column=0)
Bu5.grid(row=3,column=1)
Bu6.grid(row=3,column=2)
Bu7.grid(row=2,column=0)
Bu8.grid(row=2,column=1)
Bu9.grid(row=2,column=2)

Bus1.grid(row=1,column=0)
Bus2.grid(row=1,column=1)
Bus3.grid(row=1,column=2)
Bus4.grid(row=1,column=3)
Bus5.grid(row=2,column=3)
Bus6.grid(row=3,column=3,rowspan=2)
Bus7.grid(row=5,column=0,sticky='se')
Bus8.grid(row=5,column=1)
Bus10.grid(row=5,column=2,columnspan=2)


root.mainloop()
 
 

