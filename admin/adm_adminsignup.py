from  tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

import pymysql
from datetime import *

from tkcalendar import DateEntry


class admin_signup:

    def focusin(event,obj):
        obj.config(bg="green",fg="white")

    def focusout(event,obj):
       obj.config(bg="white",fg="black")

    def enter(event, obj):
       obj.config(bg="green", fg="white")

    def leave(event, obj):
        obj.config(bg="red", fg="black")

    def getdatabase(self):
        name = self.e2.get()
        dob=self.e3.get()
        address = self.e4.get("1.0", END)
        phone = self.e5.get()
        email = self.e6.get()
        mygender = self.gender.get()
        username = self.e7.get()
        password = self.e8.get()
        doj=self.e9.get()
        myusertype=self.usertypeent.get()
        # mydob = datetime.strptime(dob, '%d/%m/%Y').date()
        # mydoj = datetime.strptime(doj, '%d/%m/%Y').date()

        try:
            mydb=pymysql.connect(host='localhost',user='root',password='',db='hotelmanagementdb')

            with mydb.cursor() as myconn:
                # mydob = datetime.strptime(dob, '%d/%m/%Y').date()
                # mydoj = datetime.strptime(doj, '%d/%m/%Y').date()

                myconn.execute("insert into users(ename,dob,address,gender,phone,email,userid,password,doj,usertype)values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(name,self.e3.get_date(),address,mygender,phone,email,username,password,self.e9.get_date(),"admin"))
                mydb.commit()
                self.clear()
                messagebox.showinfo("Database Information","Record Sucessfully Inserted")

        except Exception as e:
            messagebox.showerror("Database Error "," Error occured Due to : "+str(e))

    def clear(self):
        self.e2.delete(0,END)
        self.e4.delete("1.0",END)
        self.e5.delete(0,END)
        self.e6.delete(0,END)
        self.e7.delete(0,END)
        self.e8.delete(0,END)

    def __init__(self):
        myframe =Tk()
        myframe.wm_title("Admin Registration")
        myframe.option_add("*tearOff", False)
        myframe.geometry("350x400")
        myframe.wm_minsize(height=500,width=500)
        myframe.wm_maxsize(height=500,width=500)
        try:
            my_menubar = Menu(myframe)
            myframe.config(menu=my_menubar)

            Admin=Menu(my_menubar)
            my_menubar.add_cascade(menu=Admin,label="Admin")
            Admin.add_command(label="Login")

            self.gender=StringVar()
            self.usertypeent=StringVar()
            self.t1=Label(myframe,text="Employee Signup")
            # self.t2=Label(myframe,text="Emp ID ")
            self.t3=Label(myframe,text="Name")
            self.t4 = Label(myframe, text="Date of Birth")
            self.t5 = Label(myframe, text="Address ")
            self.t=Label(myframe,text="Gender")
            self.t6 = Label(myframe, text="Phone")
            self.t7 = Label(myframe, text="Email")
            self.t8 = Label(myframe, text="User ID ")
            self.t9 = Label(myframe, text="Password")
            self.t10 = Label(myframe, text="Date of Joining")

            # self.e1=Entry(myframe,width=27) #Emp id
            self.e2=Entry(myframe,width=27) #Name
            self.e3 = DateEntry(myframe,width=27)#dob
            self.e4 = Text(myframe,height=4, width=20) #address
            self.e5 = Entry(myframe,width=27)#phone
            self.e6 = Entry(myframe,width=27)#email
            self.e7 = Entry(myframe,width=27)#username
            self.e8 = Entry(myframe,width=27,show="*") #password
            self.e9 = DateEntry(myframe,width=27)#doj

            self.r1=Radiobutton(myframe,text="Male",value="male",variable=self.gender,)#male
            self.r2 = Radiobutton(myframe, text="Female", value="female", variable=self.gender)#female


            self.b1=Button(myframe,text="Register",bg="red",command=self.getdatabase) #Button For Login

            # self.e1.bind("<FocusIn>",lambda e:self.focusin(self.e1))
            self.e2.bind("<FocusIn>", lambda e: self.focusin(self.e2))
            # self.e3.bind("<FocusIn>", lambda e: self.focusin(self.e3))
            self.e4.bind("<FocusIn>", lambda e: self.focusin(self.e4))
            self.e5.bind("<FocusIn>", lambda e: self.focusin(self.e5))
            self.e6.bind("<FocusIn>", lambda e: self.focusin(self.e6))
            self.e7.bind("<FocusIn>", lambda e: self.focusin(self.e7))
            self.e8.bind("<FocusIn>", lambda e: self.focusin(self.e8))
            # self.e9.bind("<FocusIn>", lambda e: self.focusin(self.e9))
            self.b1.bind("<Enter>", lambda e: self.enter(self.b1))
            self.b1.bind("<Leave>", lambda e: self.leave(self.b1))

            # self.e1.bind("<FocusOut>",lambda e:self.focusout(self.e1))
            self.e2.bind("<FocusOut>", lambda e: self.focusout(self.e2))
            # self.e3.bind("<FocusOut>", lambda e: self.focusout(self.e3))
            self.e4.bind("<FocusOut>", lambda e: self.focusout(self.e4))
            self.e5.bind("<FocusOut>", lambda e: self.focusout(self.e5))
            self.e6.bind("<FocusOut>", lambda e: self.focusout(self.e6))
            self.e7.bind("<FocusOut>", lambda e: self.focusout(self.e7))
            self.e8.bind("<FocusOut>", lambda e: self.focusout(self.e8))
            # self.e9.bind("<FocusOut>", lambda e: self.focusout(self.e9))


            self.t1.place(x=100,y=50)
            # self.t2.place(x=50,y=80)
            self.t3.place(x=50, y=110)
            self.t4.place(x=50, y=140)
            self.t5.place(x=50, y=170)
            self.t.place(x=50, y=250)
            self.t6.place(x=50, y=280)
            self.t7.place(x=50, y=310)
            self.t8.place(x=50, y=340)
            self.t9.place(x=50, y=370)
            self.t10.place(x=50, y=400)
            # self.t11.place(x=50, y=430)

            # self.e1.place(x=200, y=80)
            self.e2.place(x=200, y=110)
            self.e3.place(x=200, y=140)
            self.e4.place(x=200, y=170)
            self.r1.place(x=200,y=250)
            self.r2.place(x=280, y=250)
            self.e5.place(x=200, y=280)
            self.e6.place(x=200, y=310)
            self.e7.place(x=200, y=340)
            self.e8.place(x=200, y=370)
            self.e9.place(x=200, y=400)
            # self.usertype.place(x=200,y=430)
            self.b1.place(x=200,y=460)

        except Exception as e:
            messagebox.showerror("Error Occured ","Error Occured Due To : "+str(e))

        myframe.mainloop()

