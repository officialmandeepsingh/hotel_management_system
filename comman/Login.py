from  tkinter import *
from tkinter import messagebox
from admin.adm_home import *
from comman import *
import pymysql

from employee.emp_home import emp_home


class login:
    def focusin(event,obj):
       obj.config(bg="green",fg="white")

    def focusout(event,obj):
       obj.config(bg="white",fg="black")

    def enter(event, obj):
       obj.config(bg="green", fg="white")

    def leave(event, obj):
        obj.config(bg="red", fg="black")

    # def buttonpreesed_l(event,window):
    #     adm_home(window)


    def getconnection(self):
        try:
            mydb = pymysql.connect(host='localhost', user='root', password='', db='hotelmanagementdb')

            with mydb.cursor() as myconn:
                myconn.execute("select usertype from users where userid=%s and password =%s",
                    (self.e1.get(),self.e2.get()))
                myresult=myconn.fetchall()
                mydb.commit()
                if len(myresult)>0:
                    if myresult[0][0]=="Admin":
                        adm_home()
                    else:
                        emp_home()

                # messagebox.showinfo("Database Information", "Record Sucessfully Inserted")


        except Exception as e:
            messagebox.showerror("Error Occured ","Error Occured in Login Frame  due to : "+str(e))

    def __init__(self,frame):
        self.myframe=frame
        self.myframe.wm_title("Login Form")
        self.myframe.geometry("350x400")
        self.myframe.wm_maxsize(height=250,width=300)
        try:
            t1=Label(self.myframe,text="AUTHENTICATION")
            t2=Label(self.myframe,text="User ID ")
            t3=Label(self.myframe,text="Password")

            self.e1=Entry(self.myframe) #Entry Box For get Userid
            self.e2=Entry(self.myframe,show="*") #Entry Box For get Password

            self.b1=Button(self.myframe,text="Login",bg="red",command=self.getconnection) #Button For Login

            self.e1.bind("<FocusIn>",lambda e:self.focusin(self.e1))
            self.e2.bind("<FocusIn>",lambda e:self.focusin(self.e2))

            self.e1.bind("<FocusOut>", lambda e: self.focusout(self.e1))
            self.e2.bind("<FocusOut>", lambda e: self.focusout(self.e2))
            # self.b1.bind("<Button-1>",lambda e:self.buttonpreesed_l(self.myframe))
            self.b1.bind("<Enter>", lambda e: self.enter(self.b1))
            self.b1.bind("<Leave>", lambda e: self.leave(self.b1))

            t1.place(x=100,y=50)
            t2.place(x=50,y=80)
            t3.place(x=50, y=110)
            self.e1.place(x=120, y=80)
            self.e2.place(x=120, y=110)
            self.b1.place(x=120,y=150)

        except Exception as e:
            messagebox.showerror("Error Occured ","Error Occured Due To : "+str(e))

def mymain():
    frame = Tk()
    login(frame)
    frame.mainloop()

if __name__ == '__main__':
    mymain()