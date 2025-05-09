from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk   #pip install pillow
from tkinter import messagebox
import mysql.connector
#  defining class  Register
class Register:
    # initialising  constructor
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        #====================variables=======================
        self.var_fname=StringVar()
        self.var_1name=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        # background img
        self.bg=ImageTk.PhotoImage(file=r"D:\prayas2k25\prayas2k25\images\SDT_Zoom-Backgrounds_April-8_Windansea-1.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        
        # left background img
        self.bg1=ImageTk.PhotoImage(file=r"D:\prayas2k25\prayas2k25\images\SDT_Zoom-Backgrounds_April-8_Windansea-1.jpg")
        left_lbl1=Label(self.root,image=self.bg1)
        left_lbl1.place(x=50,y=100,width=470,height=550)
        
        # white frame
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)
        
        #register label
        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)
        
        # label and entry field
        #=====row1======
        
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        fname.place(x=50,y=100) 
        
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)  
        
        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        lname.place(x=370,y=100) 
        
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_1name,font=("times new roman",15)) 
        self.txt_lname.place(x=370,y=130,width=250)
        
        #=========row2
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)
        
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15)) 
        self.txt_contact.place(x=50,y=200,width=250)
        
        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170) 
        
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15)) 
        self.txt_email.place(x=370,y=200,width=250)
        
        #========row3
        security_Q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)
        
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Pet Name"," Your Favorite Book Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)
        
        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)
        
        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)
        
        #===========row4
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)
        
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)
        
        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)
        
        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)
        
        # ========checkbutton==========
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=380)
        
        # =========buttons=========
        img=Image.open(r"D:\prayas2k25\prayas2k25\images\register-now-button.png")
        img=img.resize((200,50), Image.Resampling.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=40,y=420,width=200)
        
        img1=Image.open(r"D:\prayas2k25\prayas2k25\images\login.png")
        img1=img1.resize((200,40), Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2")
        b1.place(x=370,y=420,width=200)        
   
   # ====================function declartion===================

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & Confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and condition")
        # else:
        #     messagebox.showinfo("Success","Welcome friends")
        else:
            conn=mysql.connector.connect(host="localhost",user="your_mysql_username_here",password="your_mysql_password_here",database="mydata") #password ki jageh mysql ka password dalna hai
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
               messagebox.showerror("Error","User already exist,Please try another email")
            else:
               my_cursor.execute("Insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                        self.var_fname.get(),
                        self.var_1name.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.var_securityQ.get(),
                        self.var_securityA.get(),
                        self.var_pass.get()
                                                                                        
                                                                                            ))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success","Register Succesfully")




# calling main method    
if __name__ == "__main__":
     root=Tk()                   
     app=Register(root)
     root.mainloop() 
 