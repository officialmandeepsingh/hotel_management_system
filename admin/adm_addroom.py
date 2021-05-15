from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

import pymysql


class adm_addroom:
    def __init__(self,frame):
        self.mywindow=Toplevel(frame)
        self.mywindow.wm_title("Add Room")
        self.mywindow.geometry("400x300")

        t1=Label(self.mywindow,text="Room No. ")
        t2 = Label(self.mywindow, text="Room Type . ")
        t3 = Label(self.mywindow, text="No.of Bed Rooms ")
        t4 = Label(self.mywindow, text="No.of People ")


        self.e1 = Entry(self.mywindow)
        self.e2 = Entry(self.mywindow)
        self.e3 = Entry(self.mywindow)

        self.b1 = Button(self.mywindow,text="Add Room",bg="red",fg="white")

        self.myroomtype=StringVar()
        # Single: A room assigned to one person.May have one or more beds.\
        # Double: A room assigned to two people.May have one or more beds.
        # Triple: A room assigned to three people.May have two or more beds.
        # Quad: A room assigned to four people.May have two or more beds.
        # Queen: A  room with a queen-sized bed.May be occupied by one or more people.
        # King: A room with a king-sized bed.May be occupied by one or more people.
        # Twin: A room with two beds.May be occupied by one or more people.
        # Double - double: A room with two double ( or perhaps queen) beds.May be occupied by one or more people.
        # Studio: A room with a studio bed – a couch that can be converted into a bed.May also have an additional bed.
        self.c1=Combobox(self.mywindow,textvariable=self.myroomtype)
        self.c1.config(values=('Single','Double','Triple','Quad','Queen','King','Twin','Double-Double','Studio'))

        t1.place(x=50,y=50)
        t2.place(x=50, y=80)
        t3.place(x=50, y=110)
        t4.place(x=50, y=140)

        self.e1.place(x=150,y=50)
        self.c1.place(x=150,y=80)
        self.e2.place(x=150, y=110)
        self.e3.place(x=150, y=140)

        self.b1.place(x=150,y=170)
        self.c1.bind("<<ComboboxSelected>>", lambda e:self.myroom(e))
        self.b1.bind("<Button-1>",lambda e:self.getinsert())

    def myroom(self,event):
        self.e2.config(state='normal')
        self.e3.config(state='normal')
        self.e2.delete(0,END)
        self.e3.delete(0,END)

        if self.myroomtype.get() =='Single':
            self.e2.insert(0,"1")
            self.e3.insert(0, "1")
            self.e2.config(state='readonly')
            self.e3.config(state='readonly')

        elif self.myroomtype.get()=='Double':
            self.e2.insert(0,"1")
            self.e3.insert(0, "2")
            self.e2.config(state='readonly')
            self.e3.config(state='readonly')

        elif self.myroomtype.get()=='Triple':
            self.e2.insert(0,"2")#Bed rooms
            self.e3.insert(0, "3")#people
            self.e2.config(state='readonly')
            self.e3.config(state='readonly')

        elif self.myroomtype.get()=='Quad':
            self.e2.insert(0,"2")#Bed rooms
            self.e3.insert(0, "4")#people
            self.e2.config(state='readonly')
            self.e3.config(state='readonly')

    def getinsert(self):
        try:
            mydb=pymysql.connect(host='localhost', user='root', password='', db='hotelmanagementdb')
            with mydb.cursor() as myconn:
                myconn.execute("insert into room(room_no,room_type,beds_rooms,people,status)values(%s,%s,%s,%s,%s)",(self.e1.get(),self.myroomtype.get(),self.e2.get(),self.e3.get(),"Available"))
                mydb.commit()
                messagebox.showinfo("Record Inserted","Your Room Records Successfully Inserted ")
        except Exception as e:
            messagebox.showerror("Database Error","Error Occured Due to "+str(e))

    def myenter(self,obj):
        obj.config(bg="green",fg="white")

    def myleave(self,obj):
        obj.config(bg="red",fg="black")

    def myfocusin(self, obj):
        obj.config(bg="green", fg="white")

    def myfocusout(self,obj):
        obj.config(bg="white",fg="black")


