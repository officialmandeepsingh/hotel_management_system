from tkinter import *
from tkinter import messagebox

import pymysql


class dashboard:
    def __init__(self,frame):
        self.myframe=Toplevel(frame)
        # self.myframe.config(bg="black")
        self.myframe.title("Dash Board")
        self.myframe.geometry("400x200")

        self.show_customer=Frame(self.myframe,width=10,height=50,bd=2,relief=RAISED )
        l1=Label(self.show_customer,text="No of Customer's").pack()
        self.count_customers()
        self.show_customer.place(x=50,y=50)

        self.show_bookrooms = Frame(self.myframe, width=10, height=50,bd=2,relief=RAISED )
        l2 = Label(self.show_bookrooms, text="Total Room Book").pack()
        self.count_book_room()
        self.show_bookrooms.place(x=200, y=50)

        self.show_availrooms = Frame(self.myframe, width=10, height=50, bd=2, relief=RAISED)
        l3 = Label(self.show_availrooms, text="Available Room").pack()
        self.count_avail_room()

        self.show_availrooms.place(x=50, y=100)

    def count_avail_room(self):
        try:
            mydb = pymysql.connect(host='localhost', user='root', password='', db='hotelmanagementdb')
            with mydb.cursor() as myconn:
                myconn.execute("select count(*) from room where status=%s",
                               ("Available"))
                mydb.commit()
                myresult = myconn.fetchone()
                show_ac = Label(self.show_availrooms,text=myresult).pack()
        except Exception as e:
            messagebox.showinfo("Database Error ", "Error Occured Due to " + str(e))

    def count_book_room(self):
        try:
            mydb = pymysql.connect(host='localhost', user='root', password='', db='hotelmanagementdb')
            with mydb.cursor() as myconn:
                myconn.execute("select count(*) from room where status=%s",
                               ("Book"))
                mydb.commit()
                myresult = myconn.fetchone()
                show_book = Label(self.show_bookrooms,text=myresult).pack()
        except Exception as e:
            messagebox.showinfo("Database Error ", "Error Occured Due to " + str(e))

    def count_customers(self):
            try:
                mydb = pymysql.connect(host='localhost', user='root', password='', db='hotelmanagementdb')
                with mydb.cursor() as myconn:
                    myconn.execute("select count(*) from customer where status=%s",("in"))
                    mydb.commit()
                    myresult = myconn.fetchone()
                    show = Label(self.show_customer,text=myresult).pack()
            except Exception as e:
                messagebox.showinfo("Database Error ", "Error Occured Due to " + str(e))


