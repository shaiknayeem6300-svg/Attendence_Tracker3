import smtplib
from email.mime.text import MIMEText

# List of students with parent emails
students = {
    "Nayeem": "shaiknayeem6300@gmail.com",
    "Zaffu": "zaffu0903@gmail.com",
    "Rafi": "shaikrafee1974@gmail.com",
    "Thameem": "sthameemansari9@gmail.com",
    "Ramya": "shaiknayeem6300@gmail.com"
}

# Attendance status for today (manually enter)
attendance = {
    "Nayeem": "A",
    "Zaffu": "A",
    "Rafi": "A",  # Absent
    "Thameem": "A",
    "Ramya": "A"  # Absent
}

# Email credentials
EMAIL = "shaiknayeem6300@gmail.com"
PASSWORD = "nrlh itnj uiws xexg"  # Use Gmail app password here

def send_email(to_email, student_name):
    subject = "Absent Alert"
    body = f"Dear Parent, your child {student_name} was absent today."
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL
    msg['To'] = to_email

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.sendmail (EMAIL, to_email, msg.as_string())
        print(f"Email sent to {to_email}")

for student, status in attendance.items():
    if status == "A":
        parent_email = students[student]
        send_email(parent_email, student)

