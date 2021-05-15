from tkinter import *


class emp_home:
    def __init__(self):
        self.frame=Tk()
        self.frame.wm_title("Employee Panel")
        self.frame.geometry("800x800")

        Menubar=Menu(self.frame)

        self.frame.option_add("*tearOff","false")
        self.frame.config(menu=Menubar)

        Bookingmenu=Menu(Menubar)
        Paymentmenu=Menu(Menubar)
        Servicesmenu = Menu(Menubar)
        Miscmenu = Menu(Menubar)

        Roommenu=Menu(Bookingmenu)
        Customermenu=Menu(Bookingmenu)
        Laundarymenu=Menu(Servicesmenu)

        Menubar.add_cascade(menu=Bookingmenu,label="Booking")
        Menubar.add_cascade(menu=Paymentmenu, label="Payment")
        Menubar.add_cascade(menu=Servicesmenu, label="Services")
        Menubar.add_cascade(menu=Miscmenu, label="Misc")

        Bookingmenu.add_cascade(menu=Roommenu,label="Room")
        Roommenu.add_command(label="Available")
        Roommenu.add_command(label="Booking")
        Bookingmenu.add_cascade(menu=Customermenu,label="Customer")
        Customermenu.add_command(label="View")
        Customermenu.add_command(label="Update")
        Bookingmenu.add_command(label="Check-in")
        Bookingmenu.add_command(label="Check-out")

        Paymentmenu.add_command(label="Billing")

        Servicesmenu.add_command(label="Resturant")
        Servicesmenu.add_cascade(menu=Laundarymenu,label="Laundary")
        Laundarymenu.add_command(label="Sock")
        Servicesmenu.add_command(label="Room Services")

        Miscmenu.add_command(label="Feedback")
        Miscmenu.add_command(label="Change Password")
        Miscmenu.add_command(label="Dashboard")
        Miscmenu.add_command(label="Logout")

        self.frame.mainloop()