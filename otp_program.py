"""OTP program"""
import requests
import random

mobile_number = input("Enter mobile_number: ")
random_number = random.randint(1000, 9999)
URL = "http://psms.goforsms.com/API/sms.php?username=srushtiimages&password=tecnics&from=WEBSMS&to=" + str(mobile_number) + "&msg=" + str(random_number) + " is your one time password.&type=1&dnd_check=0%22"
response = requests.get(url = URL)

otp = int(input("Enter otp: "))
if otp == random_number:
	print("Access is granted.")
else:
	print("ACCESS IS DENIED.")
