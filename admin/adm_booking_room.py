from tkinter import *
from tkcalendar import DateEntry
from tkinter import messagebox
from tkinter.ttk import Combobox

import pymysql


class bookroom:
    def __init__(self, frame):
        self.myframe = Toplevel(frame)
        self.myframe.wm_title(" Booking Room ")
        self.myframe.geometry("700x250")

        t1 = Label(self.myframe,text="Customer Id ")
        t2 = Label(self.myframe, text="Customer Name ")
        t3 = Label(self.myframe, text="Room Type ")
        t4 = Label(self.myframe, text="Room No. ")
        t5 = Label(self.myframe, text="Check In ")
        t6 = Label(self.myframe, text="Check Out ")
        t7 = Label(self.myframe, text="Advance Payment ")

        self.e1 = Entry(self.myframe)
        self.e2 = Entry(self.myframe)
        self.e3 = Entry(self.myframe)

        self.myroomtype = StringVar()
        self.c1 = Combobox(self.myframe, textvariable=self.myroomtype)
        self.c1.config(values=('Single', 'Double', 'Triple', 'Quad', 'Queen', 'King', 'Twin', 'Double-Double', 'Studio'))

        self.myroomno = StringVar()
        self.c2 = Combobox(self.myframe, textvariable=self.myroomno)

        self.check_in = DateEntry(self.myframe, width=12, background='darkblue',foreground='white', borderwidth=2)
        self.check_out = DateEntry(self.myframe, width=12, background='darkblue',foreground='white', borderwidth=2)

        self.b1 = Button(self.myframe,text="Book Room",bg="red",fg="white")



        t1.place(x=50,y=50)
        t2.place(x=380, y=50)
        t3.place(x=50, y=80)
        t4.place(x=380, y=80)
        t5.place(x=50, y=110)
        t6.place(x=380, y=110)
        t7.place(x=50, y=140)

        self.e1.place(x=200,y=50)
        self.e2.place(x=480, y=50)
        self.c1.place(x=200,y=80)
        self.c2.place(x=480, y=80)
        self.check_in.place(x=200, y=110)
        self.check_out.place(x=480, y=110)
        self.e3.place(x=200,y=140)

        self.b1.place(x=200,y=190)

        self.e1.bind("<FocusIn>",lambda e:self.getnormal())
        self.e1.bind("<FocusOut>", lambda e:self.get_cus_info() )
        self.c1.bind("<<ComboboxSelected>>", lambda e: self.get_roomno())
        self.b1.bind("<Button-1>",lambda e:self.booking_room())

    def  getnormal(self):
        self.e2.config(state="normal")
    def get_roomno(self):
        myno=[]
        try:
            mydb = pymysql.connect(host='localhost', user='root', password='', db='hotelmanagementdb')
            with mydb.cursor() as mycon:
                mycon.execute("select room_no from room where status=%s and room_type=%s",("Available",self.myroomtype.get()))
                myresult=mycon.fetchall()
                mydb.commit()
                if len(myresult) > 0:
                    for i in range(len(myresult)):
                        myno.append(str(myresult[i][0]))
                self.c2.config(values=myno)
        except Exception as e:
            messagebox.showerror("Database Error","Error Occured Due to "+str(e))

    def get_cus_info(self):
        try:
            self.e2.delete(0,END)
            mydb = pymysql.connect(host='localhost', user='root', password='', db='hotelmanagementdb')
            with mydb.cursor() as mycon:
                mycon.execute("select customer_name from customer where customer_id=%s",(self.e1.get()))
                myresult=mycon.fetchone()
                mydb.commit()
                if len(myresult) > 0:
                    self.e2.insert(0,str(myresult[0]))
                    self.e2.config(state="readonly")
        except Exception as e:
            messagebox.showerror("Database Error","Error Occured Due to "+str(e))

    def booking_room(self):
        try:
            mydb = pymysql.connect(host='localhost', user='root', password='', db='hotelmanagementdb')
            with mydb.cursor() as myconn:
                # customer_id,checkin,checkout,adv_amt,status
                # room_no,customer_id,customer_name,check_in,check_out,advance_payment
                myconn.execute("update room set status=%s where room_no =%s and room_type=%s",("Book",self.myroomno.get(),self.myroomtype.get()))
                try:
                    myconn.execute("insert into room_history values(%s,%s,%s,%s,%s,%s,%s)",(self.myroomno.get(),self.myroomtype.get(),self.e1.get(),self.e2.get(),self.check_in.get_date(),self.check_out.get_date(),self.e3.get()))
                except Exception as ex:
                    messagebox.showerror("Database Error","Error Occured in Room History Table due to \n"+str(ex))
                mydb.commit()
                messagebox.showinfo("Room Booked", " Room No. "+self.myroomno.get()+ "  Booked To "+self.e2.get()+"\n from : "+str(self.check_in.get_date())+"  to : "+str(self.check_out.get_date()))
        except Exception as e:
            messagebox.showerror("Database Error", "Error Occured Due to " + str(e))
