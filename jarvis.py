import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from time import ctime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
		speak("Good Morning!")

	elif hour>=12 and hour<18:
		speak("Good Afternoon!")

	else:
		speak("Good Evening!")

	speak("Hello Sir. I am Jarvis, how can i help you")

def takeCommand(ask = False):
	#It takes microphone input from user and returns string output
	r = sr.Recognizer()
	with sr.Microphone() as source:
		if ask:
			print(ask)
			print("Listening...")
			r.pause_threshold = 1
			audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language='en-in')
		print(f"User said: {query}\n")

	except:
		# print(e)
		print("Say that again please...")
		return "None"
	return query

if __name__ == "__main__":
	wishMe()
	while True:
		query = takeCommand().lower()
		#executing tasks based on query

		if 'wikipedia' in query:
			speak('Searching Wikipedia...')
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences=2)
			speak("According to Wikipedia")
			print(results)
			speak(results)

		elif 'who are you' in query:
			speak("I am Jarvis an Artificial Intelligence Voice Assistant")

		elif 'are you human' in query:
			speak("No i am Jarvis an Artificial Intelligence Virtual Machine")

		elif 'what is your name' in query:
			speak("My name is Jarvis an Artificial Intelligence Voice Assistant")

		elif 'open youtube' in query:
			webbrowser.open("youtube.com")
			speak("Okay")

		elif 'open google' in query:
			webbrowser.open("google.com")
			speak("Okay")

		elif 'open github' in query:
			webbrowser.open("github.com")
			speak("Okay")

		elif 'open amazon' in query:
            webbrowser.open("amazon.in")
            speak("Okay")

        elif 'open flipkart' in query:
            webbrowser.open("flipkart.com")
            speak("Okay")

        elif 'open myntra' in query:
            webbrowser.open("myntra.com")
            speak("Okay")

        elif 'play music' in query:
            music_dir = 'E:\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'search' in query:
            speak("What do you want to search")
            search = takeCommand('What do you want to search')
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)
            speak('Here is what i found for' + search)

        elif 'time' in query:
            print(ctime())
            speak(ctime())  