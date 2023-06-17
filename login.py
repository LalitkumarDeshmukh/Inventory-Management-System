from tkinter import*
from PIL import ImageTk #pip install pillow
from tkinter import messagebox
import sqlite3
import os
from dashboard import IMS
class Login_system:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System ")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")
        #====images====
        self.phone_image=ImageTk.PhotoImage(file="images/phone1.png")
        self.lbl_Phone_image=Label(self.root,image=self.phone_image,bd=0).place(x=350,y=60)

        #===Login_Frame===
        login_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=650,y=90,width=350,height=460)

        title=Label(login_frame,text="Login System",font=("Elephant",30,"bold"),bg="white").place(x=0,y=30,relwidth=1)
        
        lbl_user=Label(login_frame,text="ADMIN",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=100)
        self.username=StringVar()
        self.password=StringVar()
        txt_username=Entry(login_frame,textvariable=self.username,font=("times new roman",15),bg="#ECECEC").place(x=50,y=140,width=250)

        lbl_pass=Label(login_frame,text="PASSWORD",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=200)
        txt_pass=Entry(login_frame,textvariable=self.password,show="*",font=("times new roman",15),bg="#ECECEC").place(x=50,y=240,width=250)

        btn_logic=Button(login_frame,command=self.login,text="Log In",font=("Arial Rounded MT Bold",15),bg="#00B0F0",activebackground="#00B0F0",fg="white",activeforeground="white",cursor="hand2").place(x=50,y=300,width=250,height=35)

        hr=Label(login_frame,bg="lightgray").place(x=50,y=370,width=250,height=2)
        or_=Label(login_frame,text="OR",bg="white",fg="lightgray",font=("times new roman",15,"bold")).place(x=150,y=360)

        

    def login(self):
        if self.username.get()=="" or self.password.get()=="":  
             messagebox.showerror("Error","All fields are required") 

        
        elif self.username.get()!="admin" or self.password.get()!="admin":  
             messagebox.showerror("Error","Invalid Username or Password\nTry again with correct credentials") 

        
        else:
            messagebox.showinfo("Information",f"Welcome") 
            self.username.set('')
            self.password.set('')
            self.new_win=Toplevel(self.root)
            self.new_obj=IMS(self.new_win)

   
            
root=Tk()
obj=Login_system(root)
root.mainloop()    