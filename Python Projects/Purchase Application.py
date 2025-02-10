import tkinter
from tkinter import *
from PIL import ImageTk,Image
import pymysql
d = pymysql.connect(host='localhost',user='root',password='Mudeth@1990',database='pythonclass')
mycursor = d.cursor()

def Payment():
    global var1,var2,var3,var4,var5,var6
    w3=Tk()
    w3.title('Payment page')
    w3.state('zoomed')

    l=Label(w3,text='Payment',font=('Aerial',16))
    l.place(x=590,y=30)
    l1=Label(w3,text='Your orders:',font=('Century',12))
    l1.place(x=400,y=150)
    d = {}
    
    if var1.get():
        d.update({'Mango':30})
    if var2.get():
        d.update({'Lychee':100})
    if var3.get():
        d.update({'Apple':220})
    if var4.get():
        d.update({'Banana':40})
    if var5.get():
        d.update({'Grape':70})
    if var6.get():
        d.update({'Orange':50})
    yaxis = 150
    for i in d.items():
        lab = Label(w3,text=i[0]+'   ->   '+str(i[1]),font=('Century',12))
        lab.place(x=600,y=yaxis)
        yaxis += 40
    
    add = 0
    for i in d.values():
        add += i
    l2=Label(w3,text='Total Amount:                 '+str(add)+'/-',font=('Century',12))
    l2.place(x=400,y=500)

    b1=Button(w3,text='Cancel',font=('Times New Roman',12,'bold'),bg='black',fg='white',command=w3.destroy)
    b1.place(x=710,y=600)
    b=Button(w3,text='Pay Now',font=('Times New Roman',12,'bold'),bg='black',fg='white')
    b.place(x=550,y=600)


def Order():
    global w2,f2,l2,i1,text,l13,t1,t2,t3,t4,t5,t6,var1,var2,var3,var4,var5,var6,b4
    #Kindly add database fetching and compare with login data
    mail=e1.get()
    pw=e2.get()
    mycursor.execute('select * from order_sheet')
    for i in mycursor:
        if i[1]==mail and i[4]==pw:
            w2=Tk()
            w2.title('Order page')
            w2.geometry('1800x768')
            w2.state('zoomed')

            f2 = Frame(w2, width=1500, height=800,bg="pink")
            f2.pack()

            l10=Label(w2,text='Order page',font=('Ariel',16))
            l10.place(x=650,y=20)

            i2=Image.open('mango.jpg')
            test=ImageTk.PhotoImage(i2,master=w2)
            l13=Label(f2,image=test,width=200,height=200)
            l13.image=test
            l13.place(x=120,y=100)
            i3=Image.open('lychee.jpg')
            test=ImageTk.PhotoImage(i3,master=w2)
            l13=Label(f2,image=test,width=200,height=200)
            l13.image=test
            l13.place(x=600,y=100)
            i4=Image.open('Apple.jpg')
            test=ImageTk.PhotoImage(i4,master=w2)
            l13=Label(f2,image=test,width=200,height=200)
            l13.image=test
            l13.place(x=1100,y=100)
            i5=Image.open('Banana.jpg')
            test=ImageTk.PhotoImage(i5,master=w2)
            l13=Label(f2,image=test,width=200,height=200)
            l13.image=test
            l13.place(x=120,y=370)
            i6=Image.open('Grape.jpg')
            test=ImageTk.PhotoImage(i6,master=w2)
            l13=Label(f2,image=test,width=200,height=200)
            l13.image=test
            l13.place(x=600,y=370)
            i7=Image.open('Orange.jpg')
            test=ImageTk.PhotoImage(i7,master=w2)
            l13=Label(f2,image=test,width=200,height=200)
            l13.image=test
            l13.place(x=1100,y=370)
           
            var1 = IntVar(w2)
            var2 = IntVar(w2)
            var3 = IntVar(w2)
            var4 = IntVar(w2)
            var5 = IntVar(w2)
            var6 = IntVar(w2)

            t1 = Checkbutton(w2, text="Mango", variable=var1, onvalue=1, offvalue=0)
            t1.place(x=140,y=320)
            t2 = Checkbutton(w2, text="Lychee", variable=var2, onvalue=1, offvalue=0)
            t2.place(x=613,y=320)
            t3 = Checkbutton(w2, text="Apple", variable=var3, onvalue=1, offvalue=0)
            t3.place(x=1110,y=320)
            t4 = Checkbutton(w2, text="Banana", variable=var4, onvalue=1, offvalue=0)
            t4.place(x=1110,y=600)
            t5 = Checkbutton(w2, text="Grape", variable=var5, onvalue=1, offvalue=0)
            t5.place(x=613,y=600)
            t6 = Checkbutton(w2, text="Orange", variable=var6, onvalue=1, offvalue=0)
            t6.place(x=140,y=600)
    
            b4=Button(w2,text='Order',width=5,font=('Times New Roman',12,'bold'),bg='light blue',fg='black',activebackground='black',activeforeground='white',command=Payment)
            b4.place(x=710,y=600)
            b5=Button(w2,text='Cancel',font=('Times New Roman',12,'bold'),bg='light blue',fg='black',activebackground='black',activeforeground='white',command=w2.destroy)
            b5.place(x=750,y=665)


def Login():
    global w1,f1,l1,i1,e1,e2
    Name_n = e.get()
    Email = e10.get()
    Mobile = e20.get()
    Location = e30.get()
    Password_p = e40.get()
    val = [Name_n,Email,Mobile,Location,Password_p]
    mycursor.execute('insert into order_sheet values(%s,%s,%s,%s,%s);',val)
    d.commit()
    print(Name_n,Email,Mobile,Location,Password_p)

    w1=Tk()
    w1.title('Login page')
    w1.geometry('1920x768')
    w1.state('zoomed')
        
    f1=Frame(w1,width=568,height=911)
    i1=ImageTk.PhotoImage(Image.open('lemon.jpg'),master=f1)
    l1=Label(f1,image=i1)
    f1.pack()
    l1.pack()

    l6=Label(w1,text='Login Page',font=('Aeriel',14,'bold'),bg='white')
    l6.place(x=600,y=20)
    l7=Label(w1,text='Email',font=('Century',12),bg='light blue')
    l7.place(x=330,y=200)
    l8=Label(w1,text='Password',font=('Century',12),bg='light blue')
    l8.place(x=330,y=280)

    e1=Entry(w1)
    e1.place(x=420,y=202)
    e2=Entry(w1)
    e2.place(x=420,y=282)
    b2=Button(w1,text='Login',width=5,font=('Times New Roman',12,'bold'),bg='light blue',fg='black',activebackground='black',activeforeground='white',command=Order)
    b2.place(x=550,y=470)
    b3=Button(w1,text='Cancel',font=('Times New Roman',12,'bold'),bg='light blue',fg='black',activebackground='black',activeforeground='white',command=w1.destroy)
    b3.place(x=720,y=470)



#Signup
w=Tk()
w.title('Signup page')
w.geometry('1920x768')
w.state('zoomed')


f=Frame(w,width=1366,height=911)
i=ImageTk.PhotoImage(Image.open('sign_pic.jpg'))
l=Label(f,image=i)
f.place(x=0,y=-150)
l.place(x=0,y=0)

c=Canvas(w,bg='light green',width=320,height=250)
c.place(x=495,y=15)

l=Label(w,text='Signup Page',font=('Matura MT Script capitals',14,'bold'),bg='light blue')
l.place(x=590,y=20)
l1=Label(w,text='Name',font=('Thoma',12),bg='pink')
l1.place(x=510,y=60)
l2=Label(w,text='Email',font=('Thoma',12),bg='pink')
l2.place(x=510,y=95)
l3=Label(w,text='Mobile',font=('Thoma',12),bg='pink')
l3.place(x=510,y=130)
l4=Label(w,text='Location',font=('Thoma',12),bg='pink')
l4.place(x=510,y=165)
l5=Label(w,text='Password',font=('Thoma',12),bg='pink')
l5.place(x=510,y=200)

e=Entry(w)
e.place(x=600,y=62)
e10=Entry(w)
e10.place(x=600,y=97)
e20=Entry(w)
e20.place(x=600,y=132)
e30=Entry(w)
e30.place(x=600,y=167)
e40=Entry(w)
e40.place(x=600,y=202)

b=Button(w,text='Sign up',font=('Times New Roman',12,'bold'),bg='blue',fg='white',command=Login)
b.place(x=560,y=228)
b1=Button(w,text='Cancel',font=('Times New Roman',12,'bold'),bg='blue',fg='white',command=w.destroy)
b1.place(x=700,y=228)
