from tkinter import *
from tkinter import messagebox

from admin.adm_adminsignup import admin_signup
from comman.Login import login, pymysql, adm_signup


class MainFile:
    def __init__(self):
        # login()
        try:
            mydb = pymysql.connect(host='localhost', user='root', password='', db='hotelmanagementdb')

            with mydb.cursor() as myconn:
                myconn.execute("select count(*) from users")
                myresult=myconn.fetchone()
                if myresult[0] is 0:
                    admin_signup()
                else:
                    login()

        except Exception as e:
            messagebox.showerror("Error Occured ", "Error Occured in Login Frame  due to : " + str(e))


MainFile()