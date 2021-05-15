
import traceback
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.ttk import Combobox

import pymysql

class adm_showcustomer:
    def __init__(self,frame):
        self.myframe = Toplevel(frame)
        self.myframe.wm_title("Customer's List")
        self.myframe.option_add("*tearOff", False)
        self.myframe.geometry("900x500")

        t1=Label(self.myframe,text="Sort By : ")

        self.mysortby=StringVar()

        self.sortby=Combobox(self.myframe,textvariable=self.mysortby)
        self.sortby.config(values=('Customer ID','Customer Name','Date of birth'))
        self.sortby.set("Sorted By")

        self.mysearchby = StringVar()

        self.searchby = Combobox(self.myframe, textvariable=self.mysearchby)
        self.searchby.config(values=('Name','Customer id','Phone Number'))
        self.searchby.set("Search By")

        self.e1=Entry(self.myframe)

        b1=Button(self.myframe,text="Search")

        mytablearea=Frame(self.myframe,width=800,height=600)
        scrollbarx=Scrollbar(mytablearea,orient=HORIZONTAL)
        scrollbary = Scrollbar(mytablearea, orient=VERTICAL)
        self.mytable=ttk.Treeview(self.myframe,columns=('customer_id','customer_name','dob','address','phone_no','email_id','aadhar_no','reference'),xscrollcommand=scrollbarx.set,yscrollcommand=scrollbary.set)

        scrollbarx.config(command=self.mytable.xview)
        scrollbary.config(command=self.mytable.yview)

        scrollbarx.pack(side=BOTTOM,fill=X)
        scrollbary.pack(side=RIGHT, fill=Y)
        # `customer_id`, `customer_name`, `dob`, `address`, `phone_no`, `email_id`, `aadhar_no`, `reference`
        self.mytable.heading("customer_id", text="Customer ID")
        self.mytable.heading("customer_name",text="Customer Name")
        self.mytable.heading("dob",text= "Date of Birth")
        self.mytable.heading("address", text="Address")
        self.mytable.heading("phone_no", text="Phone No")
        self.mytable.heading("email_id",text="Email ID")
        self.mytable.heading("aadhar_no", text="Aadhar no")
        self.mytable.heading("reference", text="Reference By")
        # self.mytable.heading("doj", text="Date Of Joining")

        self.mytable.column('#0', stretch=NO,width=0)
        self.mytable.column('#1', stretch=NO)
        self.mytable.column('#2', stretch=NO)
        self.mytable.column('#3', stretch=NO)
        self.mytable.column('#4', stretch=NO)
        self.mytable.column('#5', stretch=NO)
        self.mytable.column('#6', stretch=NO)
        self.mytable.column('#7', stretch=NO)
        self.mytable.column('#8', stretch=NO)

        self.sortby.bind("<<ComboboxSelected>>",lambda e:self.mysortfunc(self.sortby))
        b1.bind("<Button-1>", lambda e: self.mysearchfunc(self.searchby))

        self.searchby.place(x=50,y=50)
        self.e1.place(x=200,y=50)
        b1.place(x=350,y=50)

        t1.place(x=400,y=50)
        self.sortby.place(x=480,y=50)
        self.mytable.place(x=50,y=100)
        self.fetch_record()

    def fetch_record(self):
        try:
            myresult=[]
            mydb=pymysql.connect(host='localhost', user='root', password='', db='hotelmanagementdb')
            with mydb.cursor() as myconn:
                myconn.execute("select * from customer")
                myresult=myconn.fetchall()
                self.mytable.delete(*self.mytable.get_children())
                try:
                    if len(myresult)>0:
                        for myrow in myresult:
                            print(type(myrow))
                            self.mytable.insert('', END, values=(myrow))
                    else:
                        messagebox.showinfo("No Result", "No Records found",parent=self.myframe)
                except Exception as e:
                    messagebox.showerror("Table Error ", "Record Cann't Inserted in Tabledue to  : " + str(e),parent=self.myframe)
        except Exception as e:
            traceback.print_exc()
            messagebox.showerror("Database Error ","Error Occured Due to : "+str(e),parent=self.myframe)

    def mysortfunc(self,obj):
        self.sorted_record()

    def mysearchfunc(self,obj):
        self.search_record()

    def search_record(self):
        try:
            mydb=pymysql.connect(host='localhost', user='root', password='', db='hotelmanagementdb')
            with mydb.cursor() as myconn:
                # 'Name','Customer id','Phone Number'
                if self.mysearchby.get()=='Name':
                    myconn.execute("select * from customer where customer_name like %s",(self.e1.get()+"%"))
                elif self.mysortby.get()=='Customer id':
                    myconn.execute("select * from customer where customer_id like %s",(self.e1.get()+"%"))
                elif self.mysortby.get()=='Phone Number':
                    myconn.execute("select * from customer where phone_no like %s", (self.e1.get() + "%"))

                myresult=myconn.fetchall()
                self.mytable.delete(*self.mytable.get_children())
                try:
                    if len(myresult)>0:
                        for myrow in myresult:
                            self.mytable.insert('', END, values=(myrow))
                    else:
                        messagebox.showinfo("No Result", "No Records found",parent=self.myframe)
                except Exception as e:
                    messagebox.showerror("Table Error ", "Record Cann't Inserted in Tabledue to  : " + str(e),parent=self.myframe)
        except Exception as e:
            traceback.print_exc()
            messagebox.showerror("Database Error ","Error Occured Due to : "+str(e),parent=self.myframe)

    def sorted_record(self):
        try:
            myresult=[]
            mydb=pymysql.connect(host='localhost', user='root', password='', db='hotelmanagementdb')
            with mydb.cursor() as myconn:

                if self.mysortby.get()=='Name (A to Z)':
                    myconn.execute("select * from users order by ename")
                elif self.mysortby.get()=='Name (Z to A)':
                    myconn.execute("select * from users order by ename desc")
                elif self.mysortby.get()=='Emp ID (1 to 9)':
                    myconn.execute("select * from users order by empid")
                elif self.mysortby.get() == 'Emp ID (9 to 1)':
                    myconn.execute("select * from users order by empid desc")

                myresult=myconn.fetchall()
                self.mytable.delete(*self.mytable.get_children())
                try:
                    if len(myresult)>0:
                        for myrow in myresult:
                            self.mytable.insert('', END, values=(myrow))
                    else:
                        messagebox.showinfo("No Result", "No Records found",parent=self.myframe)
                except Exception as e:
                    messagebox.showerror("Table Error ", "Record Cann't Inserted in Tabledue to  : " + str(e),parent=self.myframe)
        except Exception as e:
            traceback.print_exc()
            messagebox.showerror("Database Error ","Error Occured Due to : "+str(e),parent=self.myframe)
