from tkinter import *
from tkinter import ttk, messagebox

import pymysql
from tabulate import *

class avail_room:
    def __init__(self,frame):
        self.mywindow=Toplevel(frame)
        self.mywindow.geometry("300x450")
        self.mywindow.wm_title("View Available Rooms")


        t1=Label(self.mywindow,text="Room Type")
        self.t2=Label(self.mywindow)
        self.myroomtype=StringVar()
        c1 = ttk.Combobox(self.mywindow,values=('Single','Double','Triple','Quad'), textvariable=self.myroomtype,state="readonly")
        c1.set(" Room Type")

        t1.place(x=50,y=50)
        c1.place(x=120,y=50)
        self.t2.place(x=80,y=100)

        c1.bind("<<ComboboxSelected>>", lambda e: self.checkroom())

    def checkroom(self):
        try:
            mydb = pymysql.connect(host='localhost', user='root', password='', db='hotelmanagementdb')
            with mydb.cursor() as myconn:
                myconn.execute("select room_no,room_type,beds_rooms,people,status from room where status=%s",("Available"))
                mydb.commit()
                myresult=myconn.fetchall()
                myheader=["room no","room type","beds rooms","people","status"]
                self.t2.config(text=tabulate(myresult,headers=myheader,tablefmt="simple"))

        except Exception as e:
            messagebox.showinfo("Database Error ","Error Occured Due to "+str(e))

