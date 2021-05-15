from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

import pymysql


class adm_addsubcategory:
    def __init__(self,frame):
        self.myframe=Toplevel(frame)
        self.myframe.wm_title("Add Sub Category")
        self.myframe.geometry("450x250")
        try:

            self.mycategory=StringVar()
            t1=Label(self.myframe,text="Category Name ")
            t2=Label(self.myframe,text="Sub Category Name")

            self.e1=Combobox(self.myframe,textvariable=self.mycategory)
            self.fetchcategory()
            self.e1.set("Choose Category")
            self.e2=Entry(self.myframe,width=23)
            self.b1=Button(self.myframe,text="Add Sub Category")


            t1.place(x=50,y=50)
            t2.place(x=50, y=80)

            self.e1.place(x=200, y=50)
            self.e2.place(x=200, y=80)
            self.b1.place(x=200,y=130)

            self.e2.bind("<FocusIn>", lambda e:self.myfocusin(self.e2))
            self.e2.bind("<FocusOut>", lambda e: self.myfocusout(self.e1))
            self.b1.bind("<Enter>", lambda e: self.myenter(self.b1))
            self.b1.bind("<Leave>", lambda e: self.myleave(self.b1))
            self.b1.bind("<Button-1>",lambda e:self.mybtnclick())
        except Exception as e:
            messagebox.showerror("Error Occured ","Error Occured Due To : "+str(e),parent=self.myframe)

    def mybtnclick(self):
        print("button clicked")
        self.getconnect()

    def getcatid(self):
        index=self.mycategory.get().find(",")
        self.getid=self.mycategory.get()[0:index]

    def getconnect(self):
        try:
            mydb = pymysql.connect(host='localhost', user='root', password='', db='hotelmanagementdb')

            with mydb.cursor() as myconn:
                myconn.execute("insert into subcategory (catid,subcatname) values(%s,%s)",(self.getid,self.e2.get()))
                mydb.commit()
                messagebox.showinfo("Information ", "Sub Category Successfully Inserted",parent=self.myframe)
        except Exception as e:
            messagebox.showerror("Error Occured ", "Error Occured in Login Frame  due to : " + str(e))

    def fetchcategory(self):
        try:
            mycat=[]
            mydb = pymysql.connect(host='localhost', user='root', password='', db='hotelmanagementdb')

            with mydb.cursor() as myconn:
                myconn.execute("select * from category ")
                myresult = myconn.fetchall()
                mydb.commit()
                if len(myresult) > 0:
                    for i in range(len(myresult)):
                        mycat.append(str(myresult[i][0])+","+myresult[i][1])
                self.c1.config(values=mycat)
        except Exception as e:
            messagebox.showerror("Error Occured ", "Error Occured in Login Frame  due to : " + str(e))

    def myenter(self,obj):
        obj.config(bg="green",fg="white")

    def myleave(self,obj ):
        obj.config(bg="red",fg="black")

    def myfocusin(self, obj):
        self.getcatid()
        obj.config(bg="green", fg="white")

    def myfocusout(self,obj):
        obj.config(bg="white",fg="black")
