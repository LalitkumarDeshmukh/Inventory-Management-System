from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
import time
#import datetime

class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        #===title====
        self.icon_title=PhotoImage(file="Images/trolley3.png")
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
    
        #===btn_logout===
        #btn_logout=Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1100,y=10,height=50,width=150)
        #===clock===
        def clock():
         global date,currenttime
         date=time.strftime('%d/%m/%Y')
         currenttime=time.strftime('%H:%M:%S')
         datetimeLabel.config(text=f'   Date: {date}\nTime: {currenttime}')
         datetimeLabel.after(1000,clock)
        self.lbl_datetime=Label(self.root,text="Welcome to Inventory Management System",font=("times new roman",15,"bold"),bg="#4d636d",fg="white")
        self.lbl_datetime.place(x=0,y=70,relwidth=1,height=30)

        datetimeLabel=Label(root,font=('times new roman',18,'bold'))
        datetimeLabel.place(x=1120,y=620)
        clock()

        

        #====Left Menu==
        self.MenuLogo=Image.open("Images/menu1.png")
        self.MenuLogo=self.MenuLogo.resize((200,200),Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=565)

        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)

        self.icon_side=PhotoImage(file="Images/arrow3.png")


        lbl_menu=Label(LeftMenu,text="Menu",font=("times new roman",20),bg="#009688").pack(side=TOP,fill=X)

        btn_employee=Button(LeftMenu,text="Employee",command=self.employee,image=self.icon_side,compound=LEFT,padx=20,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier=Button(LeftMenu,text="Supplier",command=self.supplier,image=self.icon_side,compound=LEFT,padx=20,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_category=Button(LeftMenu,text="Category",command=self.category,image=self.icon_side,compound=LEFT,padx=20,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_product=Button(LeftMenu,text="Product",command=self.product,image=self.icon_side,compound=LEFT,padx=20,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales=Button(LeftMenu,text="Sales",command=self.sales,image=self.icon_side,compound=LEFT,padx=20,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(LeftMenu,text="Exit",image=self.icon_side,compound=LEFT,padx=20,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)

        #====content=====

        self.lbl_employee=Label(self.root,text=" Employee\n",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)

        self.lbl_supplier=Label(self.root,text=" Supplier\n",bd=5,relief=RIDGE,bg="#ff5722",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)

        self.lbl_category=Label(self.root,text=" Category\n",bd=5,relief=RIDGE,bg="#009688",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_category.place(x=1000,y=120,height=150,width=300)

        self.lbl_product=Label(self.root,text=" Product\n",bd=5,relief=RIDGE,bg="#607d8b",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_product.place(x=300,y=300,height=150,width=300)

        self.lbl_sales=Label(self.root,text=" Sales\n",bd=5,relief=RIDGE,bg="#ffc107",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=650,y=300,height=150,width=300)

#=====================================================================================================================================

    def employee(self):
          self.new_win=Toplevel(self.root)
          self.new_obj=employeeClass(self.new_win)

    def supplier(self):
          self.new_win=Toplevel(self.root)
          self.new_obj=supplierClass(self.new_win)  

    def category(self):
          self.new_win=Toplevel(self.root)
          self.new_obj=categoryClass(self.new_win)   

    def product(self):
          self.new_win=Toplevel(self.root)
          self.new_obj=productClass(self.new_win)

    def sales(self):
          self.new_win=Toplevel(self.root)
          self.new_obj=salesClass(self.new_win)   
       

if __name__=="__main__":      
    root=Tk()
    obj=IMS(root)
    root.mainloop()   
