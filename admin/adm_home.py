from tkinter import *

from admin import adm_addroom
from admin.adm_addcategory import adm_addcategory
from admin.adm_additems import additems
from admin.adm_addsubcategory import adm_addsubcategory
from admin.adm_booking_room import bookroom
from admin.adm_showcustomers import adm_showcustomer
from admin.adm_usersignup import adm_signup
from admin.adm_showusers import *
from comman.cm_addcustomer import *
from comman.cm_res_billing import billing


class adm_home:
    def __init__(self):
        self.frame= Tk()
        self.frame.wm_title("Admin Panel")
        self.frame.geometry("800x800")

        Menubar=Menu(self.frame)

        self.frame.option_add("*tearOff","false")
        self.frame.config(menu=Menubar)

        Bookingmenu=Menu(Menubar)
        Paymentmenu=Menu(Menubar)
        Servicesmenu = Menu(Menubar)
        Employeemenu  =Menu(Menubar)
        Miscmenu = Menu(Menubar)
        Pricemenu =Menu(Menubar)

        Roommenu=Menu(Bookingmenu)
        Customermenu=Menu(Bookingmenu)
        Laundarymenu=Menu(Servicesmenu)
        Recordmenu=Menu(Employeemenu)

        Menubar.add_cascade(menu=Bookingmenu,label="Booking")
        Menubar.add_cascade(menu=Paymentmenu, label="Payment")
        Menubar.add_cascade(menu=Servicesmenu, label="Services")
        Menubar.add_cascade(menu=Employeemenu, label="Employee")
        Menubar.add_cascade(menu=Pricemenu, label="Price")
        Menubar.add_cascade(menu=Miscmenu, label="Misc")

        Bookingmenu.add_cascade(menu=Roommenu,label="Room")
        Roommenu.add_command(label="Add Room",command=self.addnewroom)
        Roommenu.add_command(label="Available")
        Roommenu.add_command(label="Booking",command=self.bookroom)
        Bookingmenu.add_cascade(menu=Customermenu,label="Customer")
        Customermenu.add_command(label="Add",command=self.addcustomer)
        Customermenu.add_command(label="View",command=self.viewcustomer)
        Customermenu.add_command(label="Update")
        Bookingmenu.add_command(label="Check-in")
        Bookingmenu.add_command(label="Check-out")

        Paymentmenu.add_command(label="Billing",command=self.view_billing)

        Servicesmenu.add_command(label="Resturant")
        Servicesmenu.add_cascade(menu=Laundarymenu,label="Laundary")
        Laundarymenu.add_command(label="Sock")
        Servicesmenu.add_command(label="Room Services")

        Employeemenu.add_command(label="Add Employee", command=self.addstudent)
        Employeemenu.add_cascade(menu=Recordmenu,label="Record")
        Recordmenu.add_command(label="View",command=self.showusers)
        Recordmenu.add_command(label="Edit")
        Recordmenu.add_command(label="Delete")

        Pricemenu.add_command(label="Room")
        Pricemenu.add_command(label="Services")
        Pricemenu.add_command(label="Resturant")

        Miscmenu.add_command(label="Feedback")
        Miscmenu.add_command(label="Add Category",command=self.addcategory)
        Miscmenu.add_command(label="Add Items",command=self.additems)
        Miscmenu.add_command(label="Change Password")
        Miscmenu.add_command(label="Dashboard")
        Miscmenu.add_command(label="Logout")
        self.frame.mainloop()

    def addstudent(self):
        adm_signup(self.frame)

    def showusers(self):
        adm_showusers(self.frame)

    def additems(self):
        additems(self.frame)

    def addcategory(self):
        adm_addcategory(self.frame)

    def addcustomer(self):
        addcustomer(self.frame)

    def viewcustomer(self):
        adm_showcustomer(self.frame)

    def view_billing(self):
        billing(self.frame)

    def addnewroom(self):
        adm_addroom.adm_addroom(self.frame)

    def bookroom(self):
        bookroom(self.frame)
adm_home()

