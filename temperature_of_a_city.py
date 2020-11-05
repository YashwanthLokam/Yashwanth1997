"""Program to print temperature of a city"""
import requests
import speech_recognition as sr 

print("Tell your location to find temp: ")
r = sr.Recognizer()
try:
	with sr.Microphone() as source:
		audio_data = r.record(source, duration = 2)
		location = r.recognize_google(audio_data)
		URL =  "http://api.openweathermap.org/data/2.5/find?&appid=7a9f30882737a25fea0fcf2974889d24&units=metric&q=" + location
		weather_report = requests.get(url = URL)
		if weather_report.status_code == 200:
			weather_report = weather_report.json()
			temperature_of_a_city = weather_report['list'][0]['main']['temp']
			print("The temperature in " + location + " is " + str(temperature_of_a_city) + chr(176) + "C.")
		else:
			print("PLEASE TELL A VALID CITY.")
except:
	print("PLEASE TELL A VALID CITY.")