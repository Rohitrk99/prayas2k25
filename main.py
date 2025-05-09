from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance

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
        title_lbl=Label(bg_img,text="WELCOME TO ATTENDIFY", font=("times new roman",35,"bold"),bg="white",fg="black")
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

        b1=Button(bg_img,image=self.photoimg9,command=self.open_img,cursor="hand2")
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
     
     
     

        

if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()

