from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk   #pip install pillow
from tkinter import messagebox,Toplevel
import mysql.connector
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

# creating class defining Login_Window
class Login_Window:
    # initialising  constructor
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        # Initialize email and password variables
        self.var_email = StringVar()
        self.var_pass = StringVar()

        # for image
        self.bg=ImageTk.PhotoImage(file=r"D:\prayas2k25\prayas2k25\images\SDT_Zoom-Backgrounds_April-8_Windansea-1.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        #  for frame
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)
        
        # for image inside frame
        img1=Image.open(r"D:\prayas2k25\prayas2k25\images\login-icon.png")
        img1=img1.resize((100,100), Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)
        
        #label get started
        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)
        
        # username label
        username_lbl=Label(frame,text="Enter Email",font=("times new roman",15,"bold"),fg="white",bg="black")
        username_lbl.place(x=70,y=150)
        
        #empty field
        self.txtuser=ttk.Entry(frame, font=("times new roman",15,"bold"))  
        self.txtuser.place(x=40,y=180,width=270)
        
        # label for passsword
        password_lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password_lbl.place(x=70,y=225)
        
        #empty field
        self.txtpass=ttk.Entry(frame, font=("times new roman",15,"bold"))  
        self.txtpass.place(x=40,y=250,width=270)
        
        # =====Icon Images=====
        # for username
        img2=Image.open(r"D:\prayas2k25\prayas2k25\images\login-icon.png")
        img2=img2.resize((25,25), Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=323,width=25,height=25)
        
        #for password
        img3=Image.open(r"D:\prayas2k25\prayas2k25\images\lock-512.png")
        img3=img3.resize((25,25), Image.Resampling.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=394,width=25,height=25)
        
        #for login btn
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)
        
        #for register btn
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)
        
        #for forgot password
        fgtpasbtn=Button(frame,text="Forgot Pasword",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        fgtpasbtn.place(x=10,y=370,width=160)

    #new register window
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window) 
    
    #login func
    def login(self):
        email = self.txtuser.get()
        password = self.txtpass.get()


        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all fields required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="your_mysql_username_here",password="your_mysql_password_here",database="mydata") #password ki jageh mysql ka password dalna hai
                my_cursor=conn.cursor()
                my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                            email,
                                                                                            password,
                                                                                        ))
                row=my_cursor.fetchone()
                print(row)
                if row==None:
                    messagebox.showerror("Error","Invalid Username & Password")
                else:
                    open_main=messagebox.askyesno("YesNo","Access only Admin")
                    # if open_main>0:
                    if open_main:
                        # self.new_window=Toplevel(self.new_window)
                        self.new_window=Toplevel(self.root)
                        self.app=Face_Recognition_System(self.new_window) #yha pe project name dalna hai
                    else:
                        return
                        # if not open_main:
                        #     return
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")
            finally:
                if conn:
                    conn.commit()
                    conn.close()
    #======================reset password=============================
    def reset_pass(self):
        if self.combo_security_Q.get()=="select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="your_mysql_username_here",password="your_mysql_password_here",database="mydata") #password ki jageh mysql ka password dalna hai
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset,Please login with new Password",parent=self.root2)
                self.root2.destroy()
   
    #============================forgot password windows =========
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the Email address to reset the password")
        else:
            conn=mysql.connector.connect(host="localhost",user="your_mysql_username_here",password="your_mysql_password_here",database="mydata") #password ki jageh mysql ka password dalna hai
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
           # print(row)
            if row==None:
                messagebox.showerror("Error","Please enter the valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),borderwidth=0,fg="red",bg="white")
                l.place(x=0,y=0,relwidth=1)
                
                security_Q=Label(self.root2,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)
                
                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Pet Name"," Your Favorite Book Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)
                
                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)
                
                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)
                
                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_newpass.place(x=50,y=250,width=250)
        
                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)

                # messagebox.showerror("Error","Invalid username&password")
                
#  defining class  Register
class Register:

    # initialising  constructor
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        #====================variables=======================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
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
        
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15)) 
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
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2")
        b1.place(x=370,y=420,width=200)        

   
   # ====================function declartion===================

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & Confirm password must be same",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and condition",parent=self.root)
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
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()
                                                                                    ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Succesfully")
    
    def return_login(self):
        self.root.destroy()


    # connecting with project
    
class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0");
        self.root.title("face recognition system");
        
        #bg image
        img3=Image.open(r"D:\prayas2k25\prayas2k25\college images\bgimg.jpg");
        img3=img3.resize((1920,1080))#,Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=790)

        #title
        title_lbl=Label(bg_img,text="DIGITAL ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=40,y=0,width=1400,height=45)

        #student image
        img4=Image.open(r"D:\prayas2k25\prayas2k25\college images\student_detail.jpeg");
        img4=img4.resize((220,220))#,Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2", font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)

        #detect face image or button
        img5=Image.open(r"D:\prayas2k25\prayas2k25\college images\facedetector.jpg");
        img5=img5.resize((220,220))#,Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data, font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)

        #Attendance image or button
        img6=Image.open(r"D:\prayas2k25\prayas2k25\college images\attendance.jpg");
        img6=img6.resize((220,220))#,Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data, font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)

        #help desk image or button
        img7=Image.open(r"D:\prayas2k25\prayas2k25\college images\help.jpg");
        img7=img7.resize((220,220))#,Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2", font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)

        #train face image or button
        img8=Image.open(r"D:\prayas2k25\prayas2k25\college images\traindata.jpeg");
        img8=img8.resize((220,220))#,Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Train Face",cursor="hand2",command=self.train_data, font=("times new roman",15,"bold"),bg="dark blue",fg="white") #command=self.train_data,
        b1_1.place(x=200,y=580,width=220,height=40)

        #photos image or button
        img9=Image.open(r"D:\prayas2k25\prayas2k25\college images\photo.jpeg");
        img9=img9.resize((220,220))#,Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img, font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=500,y=580,width=220,height=40)

        #developer image or button
        img10=Image.open(r"D:\prayas2k25\prayas2k25\college images\developer.jpg");
        img10=img10.resize((220,220))#,Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",cursor="hand2", font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=800,y=580,width=220,height=40)

        #exit image or button
        img11=Image.open(r"D:\prayas2k25\prayas2k25\college images\exit.png");
        img11=img11.resize((220,220))#,Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1100,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit, font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=1100,y=580,width=220,height=40)

    
    #==================Funtion Buttons=====================

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    def  open_img(self):
        os.startfile("data")
        
    def iExit(self):
        self.iExit=messagebox.askyesno("Face Recognition","Are you sure exit this project" ,parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return


    def student_details(self):
     self.new_window=Toplevel(self.root)
     self.app=Student(self.new_window)
     
     
    def train_data(self):
     self.new_window=Toplevel(self.root)
     self.app=Train(self.new_window)
     
          
    def face_data(self):
     self.new_window=Toplevel(self.root)
     self.app=Face_Recognition(self.new_window)
     
    def attendance_data(self):
     self.new_window=Toplevel(self.root)
     self.app=Attendance(self.new_window)
     
     
     


            
# calling main method    
if __name__ == "__main__":
    main()
 
    # root=Tk()
    # app=Login_Window(root)
    # root.mainloop()
        
        