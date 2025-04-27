from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np
import dlib
import mysql.connector
from datetime import datetime
import time
import random

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("blink 3-4 times to mark attendance")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Top image
        img_top = Image.open("college images/studentdetails.jpg")
        img_top = img_top.resize((650, 700))
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl_left = Label(self.root, image=self.photoimg_top)
        f_lbl_left.place(x=0, y=55, width=650, height=700)

        # Right image
        img_bottom = img_top.resize((950, 700))
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        self.f_lbl_right = Label(self.root, image=self.photoimg_bottom)
        self.f_lbl_right.place(x=650, y=55, width=950, height=700)

        # Button
        btn = Button(self.f_lbl_right, text="Face Recognition", cursor="hand2", command=self.face_recog,
                     font=("times new roman", 18, "bold"), bg="darkgreen", fg="white")
        btn.place(x=365, y=620, width=200, height=40)

        # dlib detector
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    def mark_attendance(self, i, r, n, d):
        with open("attendance.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = [line.split(",")[0] for line in myDataList]
            if i not in name_list:
                now = datetime.now()
                dtString = now.strftime("%H:%M:%S")
                d1 = now.strftime("%d/%m/%Y")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

    def calculate_ear(self, eye):
        A = np.linalg.norm(eye[1] - eye[5])
        B = np.linalg.norm(eye[2] - eye[4])
        C = np.linalg.norm(eye[0] - eye[3])
        ear = (A + B) / (2.0 * C)
        return ear

    def is_blinking(self, landmarks):
        left_eye = np.array([[landmarks.part(i).x, landmarks.part(i).y] for i in range(36, 42)])
        right_eye = np.array([[landmarks.part(i).x, landmarks.part(i).y] for i in range(42, 48)])
        left_ear = self.calculate_ear(left_eye)
        right_ear = self.calculate_ear(right_eye)
        return left_ear < 0.2 or right_ear < 0.2
    
    def get_random_instruction(self):
        instructions = [
            "Blink your eyes",
            "Turn your head left",
            "Turn your head right"
        ]
        return random.choice(instructions)

    
    def face_recog(self):
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        attendance_recorded = False
        instruction = self.get_random_instruction()
        liveness_confirmed = False
        liveness_attempts = 0
        instruction_displayed_time = time.time()

        while True:
            ret, img = video_cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            faces = self.detector(img_rgb)

            cv2.putText(img, f"Instruction: {instruction}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)

            for face in faces:
                landmarks = self.predictor(img_rgb, face)
                blinking = self.is_blinking(landmarks)

                # Simulate liveness check based on instruction
                if instruction == "Blink your eyes" and blinking:
                    liveness_confirmed = True
                elif instruction == "Turn your head left" and face.left() < img.shape[1] // 3:
                    liveness_confirmed = True
                elif instruction == "Turn your head right" and face.right() > 2 * img.shape[1] // 3:
                    liveness_confirmed = True

                if liveness_confirmed:
                    x, y, w, h = face.left(), face.top(), face.width(), face.height()
                    id, predict = clf.predict(gray[y:y+h, x:x+w])
                    confidence = int((100 * (1 - predict / 300)))

                    if confidence > 80:
                        conn = mysql.connector.connect(host="localhost", username="your_mysql_username_here", password="your_mysql_username_here", database="face_recognizer")
                        my_cursor = conn.cursor()

                        my_cursor.execute("SELECT Student_id, Roll, Name, Dep FROM student WHERE Student_id=%s", (str(id),))
                        data = my_cursor.fetchone()
                        conn.close()

                        if data:
                            i, r, n, d = data
                            cv2.putText(img, "Liveness Verified. Detecting face...", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                            cv2.imshow("Face Recognition", img)
                            cv2.waitKey(3000)  # wait 3 seconds before marking
                            self.mark_attendance(str(i), str(r), str(n), str(d))
                            attendance_recorded = True
                            break
                    else:
                        cv2.putText(img, "Face not recognized", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

            cv2.imshow("Face Recognition", img)

            if cv2.waitKey(1) == 13 or attendance_recorded:
                break

            # Timeout fallback to avoid infinite loop
            liveness_attempts += 1
            if liveness_attempts > 200:
                break

        video_cap.release()
        cv2.destroyAllWindows()

        if attendance_recorded:
            messagebox.showinfo("Attendance", "✅ Attendance successfully recorded!")
        elif not liveness_confirmed:
            messagebox.showwarning("Liveness Check", "❌ Liveness detection failed or Unknown face.  Try again.")
        else:
            messagebox.showwarning("Face Recognition", "❌ Face not recognized.")


   

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()

