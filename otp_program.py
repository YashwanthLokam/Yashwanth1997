"""OTP program"""
import requests
import random

def get_mobile_number():
	mobile_number = input("Enter mobile_number: ")
	return mobile_number

def get_random_number():
	random_number = random.randint(1000, 9999)
	print(random_number)
	return random_number

def send_otp_to_mobile_number(mobile_number, random_number):
	URL = "http://psms.goforsms.com/API/sms.php?username=srushtiimages&password=tecnics&from=WEBSMS&to=" + mobile_number + "&msg=" + str(random_number) + " is your one time password.&type=1&dnd_check=0%22"
	response = requests.get(url = URL)

def validate_otp():
	random_number = get_random_number()
	mobile_number = get_mobile_number()
	status = check_mobile_number_valid_or_not(mobile_number)
	if status == False:
		print("MOBILE NUMBER IS INVALID.")
		exit()
	send_otp_to_mobile_number(mobile_number, random_number)
	otp = int(input("Enter otp: "))
	if otp == random_number:
		print("Access is granted.")
	else:
		print("ACCESS IS DENIED.")
		exit()

def check_mobile_number_valid_or_not(mobile_number):
	status = False
	if mobile_number.isdigit() == True and len(mobile_number) == 10 and mobile_number[0] != '0':
		status = True
	return status

