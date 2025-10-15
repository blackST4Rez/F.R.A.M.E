# Face-Recognition Attendance System

A system to automate attendance tracking using face recognition. Students (or users) are recognized via webcam / images; attendance is recorded without manual entry.

---

## Features

- Face detection & recognition  
- Attendance recording and storage  
- GUI / web frontend to display attendance  
- Ability to enroll new faces / users  
- Export attendance reports  

---

## Tech Stack

| Component | Technology / Library |
|---|---|
| Backend / Logic | Python |
| Face Recognition | OpenCV, KNN algorithm |
| Web / Frontend | Flask / HTML / JS / Templates |
| Data Storage | MySQL |
| UI | Webcam |

---

## How It Works

1. The system captures frames from webcam or input images.  
2. It detects faces using a detection model (Haar cascades).  
3. For each detected face, it matches against known / enrolled faces.  
4. If recognized, it marks that user as “present” in the attendance log with timestamp.  
5. The frontend or UI layer shows attendance records.  

You can also enroll new users by capturing their face images and adding them to the dataset.

---
