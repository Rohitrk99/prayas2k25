﻿
## Installation Setup
### Before running the project, ensure that you have the following setup:
- Ensure that Python is installed on your machine. 

- Install the required Python libraries using pip:

```bash
pip install -r requirements.txt //install the necessary dependencies for the project.
```

- You need to have MySQL Server installed and running on your machine. You can download MySQL from here.
- Ensure that you have access to a terminal or shell (Command Prompt, PowerShell, or Git Bash on Windows, or Terminal on macOS/Linux).

## Steps to Set Up the Project
- Clone the project repository to your local machine:
```bash
git clone https://github.com/Rohitrk99/prayas2k25.git
```
> - Configure MySQL Database
You'll need to configure two databases: mydata and face_recognizer.

Create Databases in MySQL:
> - Log into your MySQL server and run the following commands to create the required databases:

```sql
CREATE DATABASE mydata;
CREATE DATABASE face_recognizer;
```
Create Tables:
> Under mydata Database: Create the register table with the following schema:

```sql
USE mydata;

CREATE TABLE register (
    fname VARCHAR(45),
    lname VARCHAR(45),
    contact VARCHAR(45),
    email VARCHAR(45) PRIMARY KEY,
    securityQ VARCHAR(45),
    securityA VARCHAR(45),
    password VARCHAR(45)
);
```
> Under face_recognizer Database: Create the student table with the following schema:

```sql
USE face_recognizer;

CREATE TABLE student (
    Dep VARCHAR(45),
    course VARCHAR(45),
    Year VARCHAR(45),
    Semester VARCHAR(45),
    Student_id VARCHAR(45) PRIMARY KEY,
    Name VARCHAR(45),
    Division VARCHAR(45),
    Roll VARCHAR(45),
    Gender VARCHAR(45),
    Dob VARCHAR(45),
    Email VARCHAR(45),
    Phone VARCHAR(45),
    Address VARCHAR(45),
    Teacher VARCHAR(45),
    PhotoSample VARCHAR(45)
);
```

- Configure the Application
> - ***Replace your_mysql_user_name and your_mysql_password from the code.***
> - ***Update the paths to the images as per your device in the application files.***

# How the Project Works
## 1. **Register as a New User**
- Run the login.py file.

- Register as a new user by entering your details. Your email and password will be saved for login.

## 2. **Login**
- After registering, use the registered email and password to login to the system.

## 3. **Student Details**
- After logging in, click on "Student Details."

- Add your student details and select your data from the treeview.

- Click "Take Photo." The system will capture 100 photos for face recognition.

## 4. **Training the Data**
- After taking the photos, close the "Student Details" window.

- Go to "Train Data" and click "Train Data" to train the model with the captured photos.

- Once the training is complete, close the window.

## 5. **Face Recognition**
- Go to "Face Recognizer."

- Follow the on-screen instructions.

- The system will check if the person in front of the webcam is in the data folder (where the photos are stored).

- If the person is not in the folder or if an image is shown instead of a live person, attendance will not be marked.

## 6. **Check Attendance**
- Once the face recognition process is complete, you can check your attendance.

- Go to "Attendance" and **click "Import CSV."**

- It will show the attendance with date and time.

## 7. **ID Constraints**
 - ***The user IDs should be in a sequence (i.e., the first user ID should be 1, followed by 2, 3, 4, and so on).***



## Directory Structure
 **login.py & register.py**: Script for user login and registration.

 **student.py**: Handles student details input and photo capturing.

 **train_data.py**: Script to train the face recognition model.

 **face_recognition.py**: Script for real-time face recognition and attendance marking.

 **data**: captured photosamples gets stored here.



## Notes
 - Ensure your webcam is connected and working properly for the face recognition system to work.
 - The application works best with a good quality webcam and clear lighting conditions for capturing face photos.

## Contributing
If you wish to contribute to this project, feel free to fork the repository, make improvements, and submit a pull request.

