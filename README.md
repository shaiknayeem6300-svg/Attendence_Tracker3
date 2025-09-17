Student Attendance Tracker with Email Alerts
Project Overview
This Python project automates student attendance tracking and sends email notifications to parents if their child is absent on any day. It aims to enhance communication between schools and parents, ensuring timely updates about student attendance.

Features
Manual attendance marking with present/absent status.

Automatic email alerts to parents of absent students via Gmail SMTP.

Simple configuration for student and parent email details.

Easy to run and understand, suitable for beginners.

Requirements
Python 3.7 or higher

pandas library (pip install pandas)

Gmail account with App Password enabled for SMTP access.

Setup Instructions
Clone or download the repository.

Update the attendance_email_alert.py script with your Gmail email and app password.

Modify the students and attendance dictionaries with actual student names, parent emails, and attendance status.

Run the script using:

bash
python attendance_email_alert.py
How It Works
The script checks attendance status.

If a student is absent, it sends an alert email to that student’s parents.

Notes
Ensure 2-step verification is enabled on your Gmail account.

Use Gmail-generated App Password for login in the script.

Keep sensitive information like passwords out of public repositories.

License
This project is open source and free to use under the MIT License.
