import datetime
from tkinter import *
from tkinter import ttk, messagebox

import pymysql
from tkcalendar import DateEntry


class checkout:
    def __init__(self,frame):
        self.mywindow=Toplevel(frame)
        self.mywindow.wm_title("Check Out")
        self.mywindow.geometry("800x300")

        t1=Label(self.mywindow,text="Customer ID ")
        t2 = Label(self.mywindow, text="Customer Name ")
        t3 = Label(self.mywindow, text="Date of Check In ")
        t4 = Label(self.mywindow, text="Date of Check Out ")
        t5 = Label(self.mywindow, text="Resturant Balance ")
        t6 = Label(self.mywindow, text="Room Rent ")
        t7 = Label(self.mywindow, text="Mode of Payemt ")
        t8 = Label(self.mywindow, text="Advance Received ")
        t9 = Label(self.mywindow, text="Total Payable Amount ")

        self.e1 = Entry(self.mywindow) #Customer id
        self.e2 = Entry(self.mywindow) #Customer Name
        self.e3 = DateEntry(self.mywindow) #d Check in
        self.e4 = DateEntry(self.mywindow) #d check out
        self.e5 = Entry(self.mywindow) #resturant bill
        self.e6 = Entry(self.mywindow)  # room bill
        self.e7 = Entry(self.mywindow)  # Adv payment
        self.e8 = Entry(self.mywindow)  # payable amt
        self.mop=StringVar()
        self.c1=ttk.Combobox(self.mywindow,values=("Cash","Cheque","Debit Card","Paytm"),textvariable=self.mop,state="readonly")
        self.c1.set(" Mode Of Payment")
        t1.place(x=50,y=50)
        t2.place(x=350, y=50)
        t3.place(x=50, y=80)
        t4.place(x=350, y=80)
        t5.place(x=50, y=110)
        t6.place(x=350, y=110)
        t7.place(x=50, y=140)
        t8.place(x=350, y=140)

        self.e1.place(x=180, y=50)
        self.e2.place(x=500, y=50)
        self.e3.place(x=180, y=80)
        self.e4.place(x=500, y=80)
        self.e5.place(x=180, y=110)
        self.e6.place(x=500, y=110)
        self.c1.place(x=180, y=140)
        self.e7.place(x=500, y=140)

        self.frame()
        self.e1.bind("<FocusIn>",lambda e:self.foucsin())
        self.e1.bind("<FocusOut>",lambda e:self.getcustomerdetails())
        self.c1.bind("<<ComboboxSelected>>", lambda e: self.get_items())

    def get_items(self):
        # print(self.mop.get())
        self.totalpayableamt = (float(self.e5.get()) + float(self.e6.get())) - float(self.e7.get())
        if self.mop.get() in ("Debit Card","Paytm"):
            disscount=self.totalpayableamt*0.15
            self.totalpayableamt-=disscount
            # print(str(totalpayableamt))

        if self.mop.get() not in ("Debit Card", "Paytm"):
            print(str(self.totalpayableamt))
        self.ttlamtframe()

    def getcustomerdetails(self):
        try:

            mydb = pymysql.connect(host='localhost', user='root', password='', db='hotelmanagementdb')
            with mydb.cursor() as myconn:
                myroomhistory=[]
                myconn.execute("select room_type,customer_name,check_in,check_out,advance_payment,room_no,price_per_day from room_history where customer_id=%s",(self.e1.get()))
                mydb.commit()
                myroomhistory=myconn.fetchone()
                # print(type(myroomhistory))
                # print(myroomhistory)
                self.roomtype=myroomhistory[0]
                self.e2.insert(0,myroomhistory[1])
                self.e3.set_date(myroomhistory[2])
                self.e4.set_date(myroomhistory[3])
                self.e7.insert(0, myroomhistory[4])
                self.myroomno=myroomhistory[5]
                self.myroomprice = myroomhistory[6]
                # print("Room rent: "+str(int(self.myroomprice)))
                self.calcroomrent()
                del myroomhistory
                myconn.execute("select payable_amt from resturant_acc where customer_id=%s",(self.e1.get()))
                mydb.commit()
                myroomhistory=myconn.fetchone()
                print(type(myroomhistory))
                print(myroomhistory)
                if myroomhistory is None:
                    self.e5.insert(0,0)
                else:
                    self.e5.insert(0,myroomhistory[0])
                self.e2.config(state="readonly")
                self.e3.config(state="readonly")
                self.e5.config(state="readonly")
                self.e7.config(state="readonly")


        except Exception as e:
            messagebox.showerror("DataBase Error ","Error Occured Due to : "+str(e))

    def update_room_status(self):
        try:

            mydb = pymysql.connect(host='localhost', user='root', password='', db='hotelmanagementdb')
            with mydb.cursor() as myconn:
                myconn.execute("update room set status=%s where room_no=%s and  room_type=%s",("Available",self.myroomno,self.roomtype))
                mydb.commit()
        except Exception as e:
            messagebox.showerror("DataBase Error ", "Error Occured Due to : " + str(e))

    def update_customer_status(self):
        try:
            mydb = pymysql.connect(host='localhost', user='root', password='', db='hotelmanagementdb')
            with mydb.cursor() as mycon:
                mycon.execute("update customer set status=%s where customer_id=%s", ("out", self.e1.get()))
                mydb.commit()

        except Exception as e:
            messagebox.showerror("Database Error", "Error Occured Due to " + str(e))

    def calcroomrent(self):
        roomrent=0
        dayz=self.e4.get_date()-self.e3.get_date()
        stayday=str(dayz)
        index = stayday.find("day")
        # print(type(stayday))
        # print("Stay days : "+stayday)
        # print("Days : "+stayday[0:index])
        # print(self.roomtype)
        # print(self.myroomprice)
        # roomrent=int(stayday[0:index-1])*(int(self.myroomprice))
        print("Room rent : "+str(int(self.myroomprice)))
        self.e6.insert(0,str((int(self.myroomprice))))
        if self.roomtype == "Double":
            roomrent = int(stayday[0:index - 1] )* self.myroomprice
            self.e6.insert(0, str(roomrent))
        # if self.roomtype == "Triple":
        #     roomrent = int(stayday[0:index - 1]) * 750
        #     self.e6.insert(0, str(roomrent))
        # if self.roomtype == "Quad":
        #     roomrent = int(stayday[0:index - 1]) * 800
        #     self.e6.insert(0, str(roomrent))
        self.e6.config(state="readonly")

    def frame(self):
        note=Frame(self.mywindow,border=2,relief=RAISED)
        t1=Label(note,text="get 15% discount on Every Transaction with Debit Card / Paytm",font=(32))
        t1.pack()
        note.place(x=180, y=250)

    def ttlamtframe(self):
        self.note=Frame(self.mywindow,border=5,relief=RAISED)
        t1=Label(self.note,text="Total Payable Amount is : ₹ "+str(self.totalpayableamt),font=(28))
        t1.pack()
        self.note.place(x=250, y=180)

        self.note.bind("<Enter>", lambda e: self.enter(self.note))
        self.note.bind("<Leave>", lambda e: self.leave(self.note))
        t1.bind("<Button-1>",lambda e:self.billpaid())

    def billpaid(self):
        try:
            billingdate = ("{}/{}/{}".format(datetime.datetime.now().year, datetime.datetime.now().month,datetime.datetime.now().day))
            mydb = pymysql.connect(host='localhost', user='root', password='', db='hotelmanagementdb')
            with mydb.cursor() as myconn:
                myconn.execute("insert into billpaid (customer_id,customer_name,date_of_payment,amt_pay) values (%s,%s,%s,%s)",(self.e1.get(),self.e2.get(),billingdate,str(self.totalpayableamt)))
                mydb.commit()
                self.clear_rec()
                messagebox.showinfo("Bill Payment","Thank You \n Visit Again ",parent=self.mywindow)
                self.update_room_status()
                self.update_customer_status()

        except Exception as e:
            messagebox.showinfo("Database Error ","Occured due to "+str(e),parent=self.mywindow)
        self.clear()

    def enter(event,obj):
       obj.config(bg="Blue")

    def leave(event,obj):
        obj.config(bg="red")

    def foucsin(self):
        print("in")

        self.e2.config(state="normal")
        self.e3.config(state="normal")
        self.e4.config(state="normal")
        self.e5.config(state="normal")
        self.e6.config(state="normal")
        self.e7.config(state="normal")

        self.e2.delete(0, END)
        self.e3.delete(0, END)
        self.e4.delete(0, END)
        self.e5.delete(0, END)
        self.e6.delete(0, END)
        self.e7.delete(0, END)
        self.c1.set("Mode Of Payment")

    def clear_rec(self):
        try:
            mydb = pymysql.connect(host='localhost', user='root', password='', db='hotelmanagementdb')
            with mydb.cursor() as myconn:
                myconn.execute("delete from room_history where customer_id=%s",(self.e1.get()))
                myconn.execute("delete from resturant_acc where customer_id=%s",(self.e1.get()))
                mydb.commit()


        except Exception as e:
            messagebox.showerror("DataBase Error","Error occured due to : "+str(e))


    def clear(self):
        self.e2.config(state="normal")
        self.e3.config(state="normal")
        self.e4.config(state="normal")
        self.e5.config(state="normal")
        self.e6.config(state="normal")
        self.e7.config(state="normal")

        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)
        self.e4.delete(0, END)
        self.e5.delete(0, END)
        self.e6.delete(0, END)
        self.e7.delete(0, END)
        self.c1.set("Mode Of Payment")
