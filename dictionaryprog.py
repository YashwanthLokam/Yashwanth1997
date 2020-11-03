"""Program to print meaning of given word"""
import requests
import os

user_word = input("Enter a word to find its meaning and pronunciation: ")
URL = 'https://od-api.oxforddictionaries.com/api/v2/entries/en-gb/' + user_word + '?strictMatch=True'

headers = {
  'Accept': 'application/json',
  'app_id': '039aed36',
  'app_key': '7587dd82e9284ea113e15d15e7207b15'
}

information_of_word = requests.get(url = URL, headers = headers).json()
audio_file_url = information_of_word['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']
meaning_of_word = information_of_word['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
print(meaning_of_word)
command = 'vlc -I null --play-and-exit ' + audio_file_url
os.system(command)