from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0");
        self.root.title("face recognition system");
    
    
    #======variables=====
        self.var_dep=StringVar() 
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar() 
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar() 
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar() 
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar() 
        self.var_teacher=StringVar()
        
        
    
        #bg image
        img3=Image.open(r"D:\prayas2k25\prayas2k25\college images\bgimg.jpg");
        img3=img3.resize((1530,790))#,Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=790)

        #title
        title_lbl=Label(bg_img,text="STUDENT DETAILS", font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1400,height=45)
        
        #main frame
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1330,height=620)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="beige", relief=RIDGE, text="Enter Details", font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=660,height=580)

        #current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="beige", relief=RIDGE, text="Current Course Information", font=("times new roman",12,"bold"))
        current_course_frame.place(x=15,y=10,width=620,height=150)
        
        #department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),width=17,state="readonly")
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),width=17,state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24","2024-25","2025-26","2026-27")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",13,"bold"),width=17,state="readonly")
        semester_combo["values"]=("Select Semester","semester-1","semester-2","semester-3","semseter-4","semester-5","semester-6","semester-7","semseter-8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #class student information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="beige", relief=RIDGE, text="Class Student Information", font=("times new roman",12,"bold"))
        class_student_frame.place(x=15,y=200,width=620,height=300)

        #studentID
        studentId_label=Label(class_student_frame,text="StudentID:",font=("times new roman",13,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10, pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=17,font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #studentname
        studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",13,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=17,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class divison
        class_div_label=Label(class_student_frame,text="Class Divison:",font=("times new roman",13,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",13,"bold"),width=15,state="readonly")
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        
        

        #Roll no
        roll_no_label=Label(class_student_frame,text="Roll No.:",font=("times new roman",13,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=17,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),width=15,state="readonly")
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #dob
        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=17,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #email
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=17,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #phone number
        phone_label=Label(class_student_frame,text="Phone No:",font=("times new roman",13,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=17,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #address
        address_label=Label(class_student_frame,text="Address:",font=("times new roman",13,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=17,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #teacher name
        teacher_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",13,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=17,font=("times new roman",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0,sticky=W)

        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1,sticky=W)

        #bbuttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=613,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=14,font=("times new roman",13,"bold"),bg="white",fg="black")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=15,font=("times new roman",13,"bold"),bg="white",fg="black")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=15,font=("times new roman",13,"bold"),bg="white",fg="black")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=14,font=("times new roman",13,"bold"),bg="white",fg="black")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=613,height=35)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=30,font=("times new roman",13,"bold"),bg="white",fg="black")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",command=self.update_photo_sample,width=30,font=("times new roman",13,"bold"),bg="white",fg="black")
        update_photo_btn.grid(row=0,column=1)


        #Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="beige", relief=RIDGE, text="Search System", font=("times new roman",13,"bold"))
        Right_frame.place(x=680,y=10,width=630,height=580)

        # ==============Search System============
        Search_frame=LabelFrame(Right_frame,bd=2,bg="beige", relief=RIDGE, text="Search System", font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=10,width=620,height=70)

        search_label=Label(Search_frame,text="Search By:",font=("times new roman",15,"bold"),bg="white",fg="black")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(Search_frame,font=("times new roman",13,"bold"),width=9,state="readonly")
        search_combo["values"]=("Select","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(Search_frame,width=17,font=("times new roman",10,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(Search_frame,text="Search",width=15,font=("times new roman",9,"bold"),bg="white",fg="black")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(Search_frame,text="Show All",width=15,font=("times new roman",9,"bold"),bg="white",fg="black")
        showAll_btn.grid(row=0,column=4,padx=4)

        # =============table frame==========
        table_frame=Frame(Right_frame,bd=2,bg="beige", relief=RIDGE)
        table_frame.place(x=5,y=80,width=620,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #====================Function Declaration==================

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Rohit@15032003",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_course.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_semester.get(),
                                                                                                        self.var_std_id.get(),
                                                                                                        self.var_std_name.get(),
                                                                                                        self.var_div.get(),
                                                                                                        self.var_roll.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_teacher.get(),
                                                                                                        self.var_radio1.get()
                                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added succesfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
                
                
    #====================fetch data=========================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Rohit@15032003",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #=====================get cursor================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
        
    # update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Rohit@15032003",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                                                                                                    
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_course.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_semester.get(),
                                                                                                        self.var_std_name.get(),
                                                                                                        self.var_div.get(),
                                                                                                        self.var_roll.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_teacher.get(),
                                                                                                        self.var_radio1.get(),
                                                                                                        self.var_std_id.get(),
                                                                                                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Sucess","Student details successfylly update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root )
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Rohit@15032003",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

         
    #reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
    
    
    #=================Generate Data Set or Take Photo Samples===================
    
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return

        try:
            # ✅ Connect to MySQL database
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="Rohit@15032003",
                database="face_recognizer"
            )
            my_cursor = conn.cursor()

            # ✅ Update student record
            my_cursor.execute("select * from student")
            myresult=my_cursor.fetchall()
                
            id=0
            for x in myresult:
                    id+=1
                    print(id)
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_std_name.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher.get(),
                                                                                                            self.var_radio1.get(),
                                                                                                            self.var_std_id.get()==id+1
                                                                                                        ))
                

            conn.commit()
            self.fetch_data()
            self.reset_data()
            conn.close()

            # ✅ Load Haar Cascade
            face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

            def face_cropped(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    return img[y:y + h, x:x + w]
                return None

            # ✅ Try to auto-detect the working webcam
            cap = None
            for index in range(5):
                test_cap = cv2.VideoCapture(index)
                if test_cap.isOpened():
                    ret, _ = test_cap.read()
                    if ret:
                        cap = test_cap
                        print(f"[INFO] Camera index used: {index}")
                        break
                    test_cap.release()

            if cap is None:
                messagebox.showerror("Error", "No available camera found (including Iriun).", parent=self.root)
                return

            img_id = 0
            

            while True:
                ret, my_frame = cap.read()
                if not ret:
                    break

                face = face_cropped(my_frame)
                if face is not None:
                    img_id += 1
                    face = cv2.resize(face, (450, 450))
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                    file_name_path = r"D:/prayas2k25/prayas2k25/data/user."+str(id)+"."+str(img_id)+".jpg"

                    cv2.imwrite(file_name_path, face)

                    cv2.putText(face, str(img_id), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    cv2.imshow("Capturing Dataset", face)

                if cv2.waitKey(100) == 13 or img_id == 100:
                    break

            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Generating dataset completed successfully!",parent=self.root)

        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    
    #update photo sample method
    def update_photo_sample(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID is required to update photo samples.", parent=self.root)
            return

        try:
            face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

            def face_cropped(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    return img[y:y + h, x:x + w]
                return None

            # ✅ Auto-detect working webcam (including Iriun)
            cap = None
            for index in range(5):
                test_cap = cv2.VideoCapture(index)
                if test_cap.isOpened():
                    ret, _ = test_cap.read()
                    if ret:
                        cap = test_cap
                        print(f"[INFO] Using camera index: {index}")
                        break
                    test_cap.release()

            if cap is None:
                messagebox.showerror("Error", "No available camera found (including Iriun).", parent=self.root)
                return

            img_id = 0
            while True:
                ret, my_frame = cap.read()
                if not ret:
                    break

                if face_cropped(my_frame) is not None:
                    img_id += 1
                    face = cv2.resize(face_cropped(my_frame), (450, 450))
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                    file_name_path = f"D:/prayas2k25/prayas2k25/data/user.{self.var_std_id.get()}.{img_id}.jpg"
                    cv2.imwrite(file_name_path, face)

                    cv2.putText(face, str(img_id), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                    cv2.imshow("Capturing Face Samples", face)

                if cv2.waitKey(100) == 13 or img_id == 100:
                    break

            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Success", "Photo samples updated successfully.", parent=self.root)

        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


        
    

if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()  

