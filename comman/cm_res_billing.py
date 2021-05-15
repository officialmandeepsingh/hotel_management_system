from tkinter import *
from tkinter import ttk, messagebox
from tkinter.ttk import Combobox
from decimal import Decimal
import pymysql



class billing:
    def __init__(self,frame):
        self.myframe=Toplevel(frame)
        self.myframe.title("Billing")
        self.myframe.geometry("%dx%d+%d+%d" % (1300, 600, 50, 50))
        self.myframe.option_add("*tearOff", False)

        # self.srno=1
        t1 = Label(self.myframe,text="Customer ID").place(x=50,y=50)
        t2 = Label(self.myframe,text="Customer Name").place(x=300,y=50)
        t3 = Label(self.myframe,text="Room No").place(x=50,y=80)
        t4 = Label(self.myframe,text="Room Type").place(x=300,y=80)
        t5 = Label(self.myframe, text="Category").place(x=50, y=110)
        t6 = Label(self.myframe, text="Item").place(x=300, y=110)
        t7 = Label(self.myframe, text="Quantity").place(x=50, y=140)

        self.e1 = Entry(self.myframe) #For Customer ID
        self.e2 = Entry(self.myframe) #For Customer Name
        self.e3 = Entry(self.myframe) #For Room No
        self.e4 = Entry(self.myframe) #For Room Type
        self.e5 = Entry(self.myframe)  # For Quantity

        # self.b1=Button(self.myframe,text="Fetching...")
        self.b2 = Button(self.myframe, text="Add Item")

        self.mycatselect = StringVar()
        self.myitemselect = StringVar()

        self.c1 = Combobox(self.myframe,textvariable=self.mycatselect)
        self.c1.set("Choose Category")

        self.c2 = Combobox(self.myframe, textvariable=self.myitemselect)
        self.c2.set("Choose Item")

        mytablearea = Frame(self.myframe, width=100, height=500)
        scrollbarx = Scrollbar(mytablearea, orient=HORIZONTAL)
        scrollbary = Scrollbar(mytablearea, orient=VERTICAL)
        self.mytable = ttk.Treeview(self.myframe, columns=('srno','Item_no','Item_Name','Price','quantity','amount'),xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)

        scrollbarx.config(command=self.mytable.xview)
        scrollbary.config(command=self.mytable.yview)

        scrollbarx.pack(side=BOTTOM, fill=X)
        scrollbary.pack(side=RIGHT, fill=Y)
        #'srno','Item no','Item Name','Price','quantity','amount'
        self.mytable.heading("srno", text="Srno")
        self.mytable.heading("Item_no", text="Item No.")
        self.mytable.heading("Item_Name", text="Item Name")
        self.mytable.heading("Price", text="Price")
        self.mytable.heading("quantity", text="Quantity")
        self.mytable.heading("amount", text="Amount")

        self.mytable.column('#0', stretch=NO, minwidth=0, width=0)
        self.mytable.column('#1', stretch=NO,width=50)
        self.mytable.column('#2', stretch=NO,width=80)
        self.mytable.column('#3', stretch=NO,width=150)
        self.mytable.column('#4', stretch=NO,width=100)
        self.mytable.column('#5', stretch=NO,width=80)
        self.mytable.column('#6', stretch=NO,width=100)

        self.e1.place(x=130, y=50)  # For Customer ID
        self.e2.place(x=400, y=50)  # For Customer Name
        self.e3.place(x=130, y=80)  # For Room No
        self.e4.place(x=400, y=80)  # For Room Type
        self.e5.place(x=130, y=140)  # For Room Type

        self.c1.place(x=130, y=110)
        self.c2.place(x=400, y=110)

        # self.b1.place(x=550,y=50)
        self.b2.place(x=350, y=140)

        self.mytable.place(x=50,y=180)

        self.get_cat()
        self.e1.bind("<FocusOut>",lambda e:self.get_cus_info())
        self.c1.bind("<<ComboboxSelected>>", lambda e: self.get_items())
        self.c1.bind("<Enter>", lambda e: self.get_cat())
        self.b2.bind("<Enter>", lambda e: self.get_item_price())
        self.b2.bind("<Button-1>",lambda e:self.buyitems())

    def get_item_price(self):
        index = self.myitemselect.get().find(",")
        self.getid = self.myitemselect.get()[0:index]
        self.getname = self.myitemselect.get()[index + 1:]
        # self.srno=0
        try:
            mydb = pymysql.connect(host='localhost', user='root', password='', db='hotelmanagementdb')
            with mydb.cursor() as myconn:
                myconn.execute("select Price from items where item_no=%s", (self.getid))
                myresult = myconn.fetchone()
                self.myprice=myresult[0]
                # self.srno=self.srno+1
        except Exception as ex:
            messagebox.showerror("Database Error", "Error Occured during Fetching a Price of Item due To \n " + str(ex))

    def buyitems(self):

        mypurchase=[]
        # print("Item no: "+self.getid)
        # print("Item name: " + self.getname)
        # print("Price: " + str(self.myprice))
        # print("Quantity: " + self.e5.get())
        total_amt=str(self.myprice*Decimal(self.e5.get()))
        mypurchase.append("")
        mypurchase.append(self.getid)
        mypurchase.append(self.getname)
        mypurchase.append(str(self.myprice))
        mypurchase.append(self.e5.get())
        mypurchase.append(total_amt)
        # print(mypurchase)
        self.mytable.insert('',END,values=mypurchase)

    def get_cus_info(self):
        myresult=[]
        self.e2.config(state='normal')
        self.e3.config(state='normal')
        self.e4.config(state='normal')
        try:
            mydb=pymysql.connect(host='localhost', user='root', password='', db='hotelmanagementdb')
            with mydb.cursor() as myconn:
                myconn.execute("select customer_name,room_no,room_type from room_history where customer_id = %s",(self.e1.get()))
                mydb.commit()
                myresult=myconn.fetchone()
                # print(myresult)
                self.e2.delete(0,END)
                self.e3.delete(0, END)
                self.e4.delete(0, END)

                self.e2.insert(0,myresult[0])
                self.e3.insert(0, myresult[1])
                self.e4.insert(0, myresult[2])

                self.e2.config(state='readonly')
                self.e3.config(state='readonly')
                self.e4.config(state='readonly')
        except Exception as e:
            messagebox.showerror("Database Error","Error Occured Due To : "+str(e),parent=self.myframe)

    def get_cat(self):
        mycat = []
        try:
            mydb = pymysql.connect(host='localhost', user='root', password='', db='hotelmanagementdb')
            with mydb.cursor() as myconn:
                myconn.execute("select * from category")
                mydb.commit()
                myresult = myconn.fetchall()
                for i in range(len(myresult)):
                    mycat.append(str(myresult[i][0])+","+myresult[i][1])
                self.c1.config(values=mycat)
        except Exception as e:
            messagebox.showerror("Database Error", "Error Occured Due To : " + str(e), parent=self.myframe)

    def get_items(self):
        myitem = []
        index = self.mycatselect.get().find(",")
        getid = self.mycatselect.get()[index + 1:]
        try:
            # print(getid)
            mydb = pymysql.connect(host='localhost', user='root', password='', db='hotelmanagementdb')
            with mydb.cursor() as myconn:
                myconn.execute("select item_no,item_name from items where cat_name = %s",(getid))
                mydb.commit()
                myresult = myconn.fetchall()
                for i in range(len(myresult)):
                    myitem.append(str(myresult[i][0])+","+myresult[i][1])
                myconn.close()
            self.c2.config(values=myitem)
        #
        except Exception as e:
            messagebox.showerror("Database Error", "Error Occured Due To : " + str(e), parent=self.myframe)

