char_allow=[]
for i in range(65,91):
    char_allow.append(chr(i))
for i in range(97,123):
    char_allow.append(chr(i))

print(char_allow)

# length=(len(self.e1.get()))
# self.e1.delete(length-1,END)

# from PIL import ImageTk
# from tkinter import *
# mywindow=Tk()
# myback=PhotoImage(file="images//background.png")
# mywindow.config(image=myback)
# background_label = Label(mywindow, image=myback)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)
# t1=Label(mywindow,text="Category Name",image=myback)
# e1=Entry(mywindow)
# b1=Button(mywindow,text="Add Category",bg="red",fg="black")
#
# t1.place(x=50, y=60)
# e1.place(x=150, y=60)
# b1.place(x=150, y=100)
#
#
# mywindow.mainloop()
# from tkinter import *
# import pymysql
# from tkinter import messagebox, ttk
# from tkinter.ttk import Combobox
# from tkinter.messagebox import askquestion
#
#
# class billing:
#
#     def myfocusin(self, obj):
#         obj.config(bg="green", fg="white")
#
#     def myfocusout(self, obj):
#         obj.config(bg="white", fg="black")
#
#     def myenter(self, obj):
#         obj.config(bg="green", fg="white")
#
#     def myleave(self, obj):
#         obj.config(bg="red", fg="black")
#
#     def __init__(self, myframe):
#         self.myframe = Toplevel(myframe)
#         self.myframe.geometry("%dx%d+%d+%d" % (1000, 600, 0, 0))
#
#         self.cat = Label(self.myframe, text="Category ").place(x=100, y=50)
#         self.item = Label(self.myframe, text="Item ").place(x=100, y=80)
#         self.roomno = Label(self.myframe, text="Room no. ").place(x=100, y=110)
#         self.roomtype = Label(self.myframe, text="Room Type ").place(x=100, y=140)
#         self.button = Button(self.myframe, text="Place Order").place(x=200,y=170)
#
#         self.roombox = Entry(self.myframe).place(x=200,y=110)
#         self.roomtbox = Entry(self.myframe).place(x=200,y=140)
#
#         # self.roombox.bind("<FocusIn>", lambda e: self.myfocusin(self.roombox))
#         # self.roomtbox.bind("<FocusIn>", lambda e: self.myfocusin(self.roomtbox))
#
#         # self.roombox.bind("<FocusOut>", lambda e: self.myfocusout(self.roombox))
#         # self.roomtbox.bind("<FocusOut>", lambda e: self.myfocusout(self.roomtbox))
#
#         # self.button.bind("<Enter>", lambda e: self.myenter(self.button))
#         # self.button.bind("<Leave>", lambda e: self.myleave(self.button))
#         # self.button.bind("<Button-1>", lambda e: self.myenter(self.button))
#
#         self.mycatchoice = StringVar()
#         self.myitemchoice = StringVar()
#
#         self.c1 = Combobox(self.myframe, textvariable=self.mycatchoice)
#         self.c1.set("Choose Category ")
#
#         self.c2 = Combobox(self.myframe, textvariable=self.myitemchoice)
#         self.c2.set("Choose items ")
#
#         self.c1.place(x=200, y=50)
#         self.c2.place(x=200, y=80)
#
#         self.fetchcategory()
#
#         # mytablearea = Frame(self.myframe)
#         # scrollbarx = Scrollbar(mytablearea, orient=HORIZONTAL)
#         # scrollbary = Scrollbar(mytablearea, orient=VERTICAL)
#         # # columns=('itemno', 'itemname', 'price', 'quantity', 'tamount')
#         # self.mytable = ttk.Treeview(mytablearea, columns=('itemno', 'itemname', 'price', 'quantity', 'tamount'),xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)
#         #
#         # scrollbarx.config(command=self.mytable.xview)
#         # scrollbarx.pack(side=BOTTOM, fill=X)
#         # scrollbary.config(command=self.mytable.yview)
#         # scrollbary.pack(side=RIGHT, fill=Y)
#         #
#         # self.mytable.heading('itemno', text="Item No")
#         # self.mytable.heading('itemname', text="Item Name")
#         # self.mytable.heading('price', text="Price")
#         # self.mytable.heading('quantity', text="Quantity")
#         # self.mytable.heading('tamount', text="Total Ammount")
#         #
#         # self.mytable['show']='headings'
#         #
#         # self.mytable.column('#0', stretch=NO,width=0)
#         # self.mytable.column('#1', stretch=NO,width=100)
#         # self.mytable.column('#2', stretch=NO,width=150)
#         # self.mytable.column('#3', stretch=NO,width=120)
#         # self.mytable.column('#4', stretch=NO,width=120)
#
#         # self.mytable.place(x=300,y=50)
#
#         # mytablearea.pack()
#
#         mytablearea = Frame(self.myframe, width=800, height=600)
#         scrollbarx = Scrollbar(mytablearea, orient=HORIZONTAL)
#         scrollbary = Scrollbar(mytablearea, orient=VERTICAL)
#         self.mytable = ttk.Treeview(self.myframe, columns=(
#         'customer_id', 'customer_name', 'dob', 'address', 'phone_no', 'email_id', 'aadhar_no', 'reference'),
#                                     xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)
#
#         scrollbarx.config(command=self.mytable.xview)
#         scrollbary.config(command=self.mytable.yview)
#
#         scrollbarx.pack(side=BOTTOM, fill=X)
#         scrollbary.pack(side=RIGHT, fill=Y)
#         # `customer_id`, `customer_name`, `dob`, `address`, `phone_no`, `email_id`, `aadhar_no`, `reference`
#         self.mytable.heading("customer_id", text="Customer ID")
#         self.mytable.heading("customer_name", text="Customer Name")
#         self.mytable.heading("dob", text="Date of Birth")
#         self.mytable.heading("address", text="Address")
#         self.mytable.heading("phone_no", text="Phone No")
#         self.mytable.heading("email_id", text="Email ID")
#         self.mytable.heading("aadhar_no", text="Aadhar no")
#         self.mytable.heading("reference", text="Reference By")
#
#         self.mytable.place(x=350,y=50)
#         try:
#             myobj = pymysql.connect(host="localhost", user="root",password="", db="hotelmanagementdb")
#             # with myobj.cursor() as myconn:
#             #     sql_query = "select itemno,itemname,price,quantity,tamount from emptable"
#             #     try:
#             #         myconn.execute(sql_query)
#             #         result = myconn.fetchall()
#             #         for myrow in result:
#             #             self.mytable.insert('', END, values=(myrow))
#             #
#             #         myobj.commit()
#             #         myobj.close()
#             #
#             #     except Exception as ex:
#             #         messagebox.showerror("Error Occured in query", "Error occured due to " + str(ex))
#
#         except Exception as ex:
#             messagebox.showerror("Error Occured", "Error occured due to " + str(ex))
#
#     def fetchcategory(self):
#         mycat = []
#         try:
#             mydb = pymysql.connect(host='localhost', user='root', password='', db='hotelmanagementdb')
#             with mydb.cursor() as myconn:
#                 myconn.execute("select * from category")
#                 mydb.commit()
#                 myresult = myconn.fetchall()
#                 for i in range(len(myresult)):
#                     mycat.append(str(myresult[i][0]) + "," + myresult[i][1])
#                 self.c1.config(values=mycat)
#         except Exception as e:
#             messagebox.showerror("Database Error ", "Error Ocured Due to : " + str(e), parent=self.myframe)
#
#         def myenter(self, obj):
#             obj.config(bg="orange", fg="white")
#             self.insertrecord()
#
#         def insertrecord(self):
#             try:
#                 mydb = pymysql.connect(host='localhost', user='root', password='', db='hotelmanagementdb')
#                 with mydb.cursor() as myconn:
#                     myconn.execute("insert into items(item_no,item_name,cat_name,Price,qty) values(%s,%s,%s,%s,%s)",
#                                    (self.e1.get(), self.e2.get(), self.mycatchoice.get(), self.e3.get(), self.e4.get()))
#                     mydb.commit()
#                     messagebox.showinfo("Database Information ", "Item Succesfully Inserted", parent=self.mywindow)
#
#             except Exception as ex:
#                 messagebox.showerror("Database Error ", "Error Ocured Due to : " + str(ex), parent=self.mywindow)
#


# from tkinter import*
#
# myframe = Tk()
# myframe.wm_minsize(500,500)
# usernamelabel = Label(myframe,text="Username")
# usernameentry = Entry(myframe)
# passlabel = Label(myframe,text="Password")
# passentry = Entry(myframe)
# usernamelabel.place(x=50,y=50)
# usernameentry.place(x=150,y=50)
# passlabel.place(x=50,y=100)
# passentry.place(x=150,y=100)
# loginbutton= Button(myframe,text = "Login",bg="red")
#
# loginbutton.bind("<Enter>", lambda e :myenter(e,loginbutton))
# usernameentry.bind("<FocusIn>", lambda e :myfocusin(e,usernameentry))
# loginbutton.place(x=175,y=150)
#
# def myenter(event,obj):
#     obj.config(bg="green",fg="white")
#
# def myfocusin(event,loginbutton):
#     loginbutton.config(bg="green",fg="white")
#
# myframe.mainloop()
#
#


# from datetime import *
#
# date_str = '09-19-2018'
#
# date_str = '09-19-2018'
#
# date_object = datetime.strptime(date_str, '%m-%d-%Y').date()
# print(type(date_object))
# print(date_object)
# print(type(date_object))
# print(date_object)