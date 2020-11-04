"""Program to print meaning of given word"""
import requests
import pyttsx3
from playsound import playsound


def word_meaning():
	meaning_of_word = information_of_word['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
	print("The meaning of " + user_word + " is " + meaning_of_word + ".")

def pronunciation_of_word():
	audio_file_url = information_of_word['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']
	playsound(audio_file_url)

def example_sentence_for_given_word():
	example_sentence = information_of_word['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['examples'][0]['text']
	print("An example sentence where you can use " + user_word + ": " + example_sentence)
	speaker = pyttsx3.init()
	speaker.say(example_sentence)
	speaker.runAndWait()

def confirm_to_exit():
	print("Do you want to leave? ")
	user_choice = input("Press Y or N: ")
	if user_choice == 'Y':
		exit()

user_word = input("Enter a word to find its meaning and pronunciation: ")
URL = "https://od-api.oxforddictionaries.com/api/v2/entries/en-gb/" + user_word + "?strictMatch=True"
headers = {
  'Accept': 'application/json',
  'app_id': '039aed36',
  'app_key': '7587dd82e9284ea113e15d15e7207b15'
}

response = requests.get(url = URL, headers = headers)

functions_list = [word_meaning, pronunciation_of_word, example_sentence_for_given_word, confirm_to_exit]

if response.status_code == 200:
	information_of_word = response.json()
	while True:
		print("1. Meaning of the word\n2. Listen to pronunciation of given word\n3. View and listen to an example sentence where the word is used\n4. Exit")
		user_choice = int(input("Enter a number: "))
		if user_choice > 0 and user_choice <=4:
			functions_list[user_choice - 1]()
		else:
			print("ENTER A VALID NUMBER.")
else:
	print("INVALID WORD")

