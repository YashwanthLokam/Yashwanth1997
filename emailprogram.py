"""Program to send email through a python program"""
import smtplib
sender_email_id = input("Enter your email id: ")
sender_email_password = input("Enter your password: ")
recipient_email_id = input("Enter the recipient email id : ")
message = input("Enter your message: ")

email_session = smtplib.SMTP('smtp.gmail.com', 587)
email_session.starttls()
email_session.login(sender_email_id, sender_email_password)
email_session.sendmail(sender_email_id, recipient_email_id, message)
print("Mail is successfully sent.")
email_session.quit()