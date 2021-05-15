from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

import pymysql


class additems:
    def __init__(self,frame):
        self.mywindow = Toplevel(frame)
        self.mywindow.wm_title("Add Items")
        self.mywindow.geometry("320x300")

        t1 = Label(self.mywindow,text="Category ")
        t2 = Label(self.mywindow, text="Item No. ")
        t3 = Label(self.mywindow, text="Item Name ")
        t4 = Label(self.mywindow, text="Price ")
        t5 = Label(self.mywindow, text="Quantity (opt) ")

        self.mycatchoice=StringVar()

        self.c1 = Combobox(self.mywindow,textvariable=self.mycatchoice)
        self.e1 = Entry(self.mywindow)
        self.e2 = Entry(self.mywindow)
        self.e3 = Entry(self.mywindow)
        self.e4 = Entry(self.mywindow)
        self.b1=Button(self.mywindow,text="Add Item")

        self.c1.set("Choose Category ")

        t1.place(x=50,y=50)
        t2.place(x=50, y=80)
        t3.place(x=50, y=110)
        t4.place(x=50, y=140)
        t5.place(x=50, y=170)

        self.c1.place(x=150, y=50)
        self.e1.place(x=150, y=80)
        self.e2.place(x=150, y=110)
        self.e3.place(x=150, y=140)
        self.e4.place(x=150, y=170)

        self.b1.place(x=150,y=220)

        self.fetchcategory()

        self.e1.bind("<FocusIn>", lambda e: self.myfocusin(self.e1))
        self.e2.bind("<FocusIn>", lambda e: self.myfocusin(self.e2))
        self.e3.bind("<FocusIn>", lambda e: self.myfocusin(self.e3))
        self.e4.bind("<FocusIn>", lambda e: self.myfocusin(self.e4))

        self.e1.bind("<FocusOut>", lambda e: self.myfocusout(self.e1))
        self.e2.bind("<FocusOut>", lambda e: self.myfocusout(self.e2))
        self.e3.bind("<FocusOut>", lambda e: self.myfocusout(self.e3))
        self.e4.bind("<FocusOut>", lambda e: self.myfocusout(self.e4))

        self.b1.bind("<Enter>", lambda e: self.myenter(self.b1))
        self.b1.bind("<Leave>", lambda e: self.myleave(self.b1))
        self.b1.bind("<Button-1>", lambda e: self.myenter(self.b1))

    def myfocusin(self, obj):
        obj.config(bg="green", fg="white")

    def myfocusout(self, obj):
        obj.config(bg="white", fg="black")

    def myenter(self,obj):
        obj.config(bg="green",fg="white")

    def myleave(self,obj):
        obj.config(bg="red",fg="black")


    def fetchcategory(self):
        mycat=[]
        try:
            mydb=pymysql.connect(host='localhost',user='root',password='',db='hotelmanagementdb')
            with mydb.cursor() as myconn:
                myconn.execute("select * from category")
                mydb.commit()
                myresult=myconn.fetchall()
                for i in range(len(myresult)):
                    mycat.append(str(myresult[i][0])+","+myresult[i][1])
                self.c1.config(values=mycat)
        except Exception as e:
            messagebox.showerror("Database Error ","Error Ocured Due to : "+str(e),parent=self.mywindow)

    def myenter(self,obj):
        obj.config(bg="orange", fg="white")
        self.insertrecord()

    def insertrecord(self):
        index = self.mycatchoice.get().find(",")
        getid = self.mycatchoice.get()[index+1:]

        try:
            mydb=pymysql.connect(host='localhost',user='root',password='',db='hotelmanagementdb')
            with mydb.cursor() as myconn:
                myconn.execute("insert into items(item_no,item_name,cat_name,Price,qty) values(%s,%s,%s,%s,%s)",(self.e1.get(),self.e2.get(),getid,self.e3.get(),self.e4.get()))
                mydb.commit()
                messagebox.showinfo("Database Information ", "Item Succesfully Inserted", parent=self.mywindow)

        except Exception as ex:
            messagebox.showerror("Database Error ","Error Ocured Due to : "+str(ex),parent=self.mywindow)