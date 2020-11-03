"""Program to print temperature of a city"""
import requests

location = input("Enter city name: ")
URL =  "http://api.openweathermap.org/data/2.5/find?&appid=7a9f30882737a25fea0fcf2974889d24&units=metric&q=" + location
weather_report = requests.get(url = URL)
weather_report = weather_report.json()
temperature_of_a_city = weather_report['list'][0]['main']['temp']
print("The temperature in " + location + " is " + str(temperature_of_a_city) + chr(176) + "C.")