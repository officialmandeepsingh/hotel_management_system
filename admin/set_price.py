from tkinter import *
from tkinter import ttk, messagebox

import pymysql


class SetPrice:
    def __init__(self,frame):
        self.mywindow = Toplevel(frame)
        self.mywindow.wm_title("Update Room Rent")
        self.mywindow.geometry("400x200")

        self.old=Frame(self.mywindow,width=10,height=50,bd=2,relief=RAISED)
        self.new = Frame(self.mywindow,width=10,height=50,bd=2,relief=RAISED)
        t1=Label(self.mywindow,text="Room Type")

        self.myroomtype = StringVar()
        self.c1 = ttk.Combobox(self.mywindow, textvariable=self.myroomtype)
        self.c1.config(values=('Single', 'Double', 'Triple', 'Quad'))
        self.c1.set("Choose  Room Type")

        old_t1=Label(self.old,text="Present Room Rent (₹) ")
        self.old_e1=Entry(self.old)

        old_t1.pack()
        self.old_e1.pack()

        new_t1 = Label(self.new, text="New Room Rent (₹) ")
        self.new_e1 = Entry(self.new)

        b1=Button(self.mywindow,text="Update Rent")

        new_t1.pack()
        self.new_e1.pack()

        t1.place(x=50,y=50)
        self.c1.place(x=150,y=50)
        self.old.place(x=50,y=80)
        self.new.place(x=200, y=80)
        b1.place(x=125,y=130)
        self.c1.bind("<<ComboboxSelected>>", lambda e: self.get_roomno())
        b1.bind("<Button-1>", lambda e: self.updatetable())


    def get_roomno(self):
        myno=[]
        self.old_e1.config(state="normal")
        self.old_e1.delete(0,END)
        try:
            mydb = pymysql.connect(host='localhost', user='root', password='', db='hotelmanagementdb')
            with mydb.cursor() as mycon:
                mycon.execute("select distinct(price_per_day) from room where room_type=%s",(self.myroomtype.get()))
                myresult=mycon.fetchone()
                mydb.commit()
                self.myroomprice = myresult[0]
                print("Room rent: " + str(int(self.myroomprice)))
                self.old_e1.insert(0,"₹ "+str(int(self.myroomprice)))
                self.old_e1.config(state="readonly")
        except Exception as e:
            messagebox.showerror("Database Error","Error Occured Due to "+str(e))

    def updatetable(self):
        try:
            mydb = pymysql.connect(host='localhost', user='root', password='', db='hotelmanagementdb')
            with mydb.cursor() as mycon:
                mycon.execute("update room set price_per_day=%s where room_type=%s",(self.new_e1.get(),self.myroomtype.get()))
                mydb.commit()
                messagebox.showinfo("DataBase Information","Room Rent is Updated")
                self.new_e1.delete(0,END)
                self.old_e1.config(state="normal")
                self.old_e1.delete(0,END)
                self.c1.set("Choose  Room Type")
        except Exception as e:
            messagebox.showerror("Database Error","Error Occured Due to "+str(e))

