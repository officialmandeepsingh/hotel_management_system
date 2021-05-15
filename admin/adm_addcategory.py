from tkinter import *
from tkinter import messagebox

import pymysql
from PIL import ImageTk

class adm_addcategory:
    def __init__(self,frame):
        self.mywindow=Toplevel(frame)
        self.mywindow.wm_title("Add Category")
        self.mywindow.geometry("320x300")

        t1=Label(self.mywindow,text="Category Name")
        self.e1=Entry(self.mywindow)
        self.b1=Button(self.mywindow,text="Add Category",bg="red",fg="black")

        self.e1.bind("<FocusIn>",lambda e:self.myfocusin(self.e1))
        self.e1.bind("<Key>", self.checkchar)
        self.e1.bind("<FocusOut>", lambda e: self.myfocusout(self.e1))
        self.b1.bind("<Enter>",lambda e:self.myenter(self.b1))
        self.b1.bind("<Leave>", lambda e: self.myleave(self.b1))
        self.b1.bind("<Button-1>",lambda e:self.mybtnclick())

        t1.place(x=50,y=60)
        self.e1.place(x=150, y=60)
        self.b1.place(x=150,y=100)

    def checkchar(self,event):
        char_allow = []

        print("String Length: "+str(length))
        for i in range(65, 91):
            char_allow.append(chr(i))
        for i in range(97, 123):
            char_allow.append(chr(i))
        if event.keysym in char_allow:
            print("char")
            length = len(self.e1.get())
            # print("Element Position :"+str(len(self.e1.get())))
            self.e1.delete(length+1,END)
            # self.e1.insert(length,event.keysym)
    def mybtnclick(self):
        try:

            self.validation()
            mydb=pymysql.connect(host='localhost',user='root',password='',db='hotelmanagementdb')
            with mydb.cursor() as myconn:
                # myconn.execute("insert into category (catname) values(%s)",(self.e1.get()))
                mydb.commit()
                # self.getcatid()
        except nameistooshort as ex:
            messagebox.showwarning("Warning",""+str(ex))
        except Exception as e:
            messagebox.showerror("DataBase Error","Error Occured Due to : "+str(e))

    def getcatid(self):
        try:
            mydb=pymysql.connect(host='localhost',user='root',password='',db='hotelmanagementdb')
            with mydb.cursor() as myconn:
                myconn.execute("select catid from category where catname=%s",(self.e1.get()))
                mydb.commit()
                myresult=myconn.fetchall()
                messagebox.showinfo("Category Information ", "Your Category "+self.e1.get()+" is Successfully Inserted \n Your Category Id : "+str(myresult[0][0]))
        except Exception as e:
            messagebox.showerror("DataBase Error","Error Occured Due to : "+str(e))

    def myenter(self,obj):
        obj.config(bg="green",fg="white")

    def myleave(self,obj):
        obj.config(bg="red",fg="black")

    def myfocusin(self, obj):
        obj.config(bg="green", fg="white")

    def myfocusout(self,obj):
        obj.config(bg="white",fg="black")

    def validation(self):
        if len(self.e1.get())<4:
            raise nameistooshort("You Entered Catagory Name too short ")

class nameistooshort(Exception):
    def __init__(self,message):
        super(nameistooshort, self).__init__(message)

