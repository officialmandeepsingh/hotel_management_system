import traceback
from datetime import *
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

import pymysql


class addcustomer:
    def __init__(self,frame):
        self.mywindow = Toplevel(frame)
        self.mywindow.wm_title("Add Customer")
        self.mywindow.geometry("400x450")

        self.maxid=[]

        t1 = Label(self.mywindow,text="Customer id ")
        t2 = Label(self.mywindow, text="Customer Name ")
        t3 = Label(self.mywindow, text="DoB ")
        t4 = Label(self.mywindow, text="Address ")
        t5 = Label(self.mywindow, text="Phone no.")
        t6 = Label(self.mywindow, text="Email ID ")
        t7 = Label(self.mywindow, text="Aadhar No. ")
        t8 = Label(self.mywindow, text="Reference's ")

        self.getmaxcid()

        self.mycatchoice=StringVar()
        maxcid=str(self.maxid[0]+1)
        self.e1 = Entry(self.mywindow,width=27)# Entry Box for Customer id
        self.e1.insert(0,maxcid)
        self.e2 = Entry(self.mywindow,width=27)# Entry Box for Customer Name
        self.e3 = Entry(self.mywindow,width=27)# Entry Box for DOB
        self.e4 = Text(self.mywindow, height=4, width=20)# Text Box for Address
        self.e5 = Entry(self.mywindow,width=27)# Entry Box for Phone no
        self.e6 = Entry(self.mywindow,width=27)# Entry Box for Email id
        self.e7 = Entry(self.mywindow,width=27)# Entry Box for Aadhar No.
        self.e8 = Entry(self.mywindow,width=27)# Entry Box for Referneces

        self.b1=Button(self.mywindow,text="Add Item")

        t1.place(x=50,y=50)
        t2.place(x=50, y=80)
        t3.place(x=50, y=110)
        t4.place(x=50, y=140)
        t5.place(x=50, y=220)
        t6.place(x=50, y=250)
        t7.place(x=50, y=280)
        t8.place(x=50, y=310)

        self.e1.place(x=150, y=50)
        self.e2.place(x=150, y=80)
        self.e3.place(x=150, y=110)
        self.e4.place(x=150, y=140)
        self.e5.place(x=150, y=220)
        self.e6.place(x=150, y=250)
        self.e7.place(x=150, y=280)
        self.e8.place(x=150, y=310)

        self.b1.place(x=150,y=340)

        self.e1.bind("<FocusIn>", lambda e: self.myfocusin(self.e1))
        self.e2.bind("<FocusIn>", lambda e: self.myfocusin(self.e2))
        self.e3.bind("<FocusIn>", lambda e: self.myfocusin(self.e3))
        self.e4.bind("<FocusIn>", lambda e: self.myfocusin(self.e4))
        self.e5.bind("<FocusIn>", lambda e: self.myfocusin(self.e5))
        self.e6.bind("<FocusIn>", lambda e: self.myfocusin(self.e6))
        self.e7.bind("<FocusIn>", lambda e: self.myfocusin(self.e7))
        self.e8.bind("<FocusIn>", lambda e: self.myfocusin(self.e8))

        self.e1.bind("<FocusOut>", lambda e: self.myfocusout(self.e1))
        self.e2.bind("<FocusOut>", lambda e: self.myfocusout(self.e2))
        self.e3.bind("<FocusOut>", lambda e: self.myfocusout(self.e3))
        self.e4.bind("<FocusOut>", lambda e: self.myfocusout(self.e4))
        self.e5.bind("<FocusOut>", lambda e: self.myfocusout(self.e5))
        self.e6.bind("<FocusOut>", lambda e: self.myfocusout(self.e6))
        self.e7.bind("<FocusOut>", lambda e: self.myfocusout(self.e7))
        self.e8.bind("<FocusOut>", lambda e: self.myfocusout(self.e8))

        self.b1.bind("<Enter>", lambda e: self.myenter(self.b1))
        self.b1.bind("<Leave>", lambda e: self.myleave(self.b1))
        self.b1.bind("<Button-1>", lambda e: self.myclick(self.b1))

    def myfocusin(self, obj):
        obj.config(bg="green", fg="white")

    def myfocusout(self, obj):
        obj.config(bg="white", fg="black")

    def myenter(self,obj):
        obj.config(bg="green",fg="white")

    def myleave(self,obj):
        obj.config(bg="red",fg="black")

    def myclick(self,obj):
        obj.config(bg="orange", fg="white")
        self.insertrecord()

    def insertrecord(self):
        try:
            id=self.e1.get()
            name=self.e2.get()
            dob = self.e3.get()
            address=self.e4.get("1.0",END)
            phone=self.e5.get()
            email=self.e6.get()
            aadhar=self.e7.get()
            ref=self.e8.get()
            mydob = datetime.strptime(dob, '%d/%m/%Y').date()
            messagebox.showinfo("demo","Id : "+id+"\n name : "+name+"\n dob : "+dob+"\n Address : "+address+"\n Phone : "+phone+"\n Email : "+email+" \n Addhar : "+aadhar+"\n References : "+ref,parent=self.mywindow)
            mydb = pymysql.connect(host='localhost', user='root', password='', db='hotelmanagementdb')
            with mydb.cursor() as myconn:
                myconn.execute("insert into customer values (%s,%s,%s,%s,%s,%s,%s,%s)",(id,name,mydob,address,phone,email,aadhar,ref))
                mydb.commit()
                messagebox.showinfo("Database Information","Customer Record Successfully Inserted",parent=self.mywindow)
        except Exception as e:
            traceback.print_exc()
            messagebox.showerror("Database Error","Error Occured Due to : "+str(e),parent=self.mywindow)

    def getmaxcid(self):
        try:
            mydb=pymysql.connect(host='localhost', user='root', password='', db='hotelmanagementdb')
            with mydb.cursor() as myconn:
                myconn.execute("select max(customer_id) from customer")
                self.maxid=myconn.fetchone()
                mydb.close()


        except Exception as e:
            messagebox.showerror("Database Error ","Error Occured Due To : "+str(e),parent=self.mywindow)
