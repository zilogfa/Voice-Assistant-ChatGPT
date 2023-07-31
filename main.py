"""
Basic fully functional voice assistant  involves multiple components, 
including speech recognition, natural language processing, 
and text-to-speech capabilities - 

Using Python3 language and SpeaachRecognition/pyttsx3 libraries. 

commands: 
. reminder
. to-do list
. search
. exit

2023
"""

import speech_recognition as sr
import pyttsx3
import datetime
#pip PyAudio

# Configuring text-to-speech engine with pyttsx3
engine = pyttsx3.init()

# Speak the Assistant's response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# recognizing speech using SpeechRecognition library as sr
def recognize_speech():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-US")
        print(f"User: {query}\n")
        return query
    except Exception as e:
        print("Error: Couldn't recognize speech.")
        return ""

# Setting a reminder function
def set_reminder():
    speak("Sure, please tell me what would you like me to remind you about?")
    reminder_text = recognize_speech()

    if reminder_text:
        speak("When would you like to be reminded?")
        time_text = recognize_speech()

        if time_text:
            try:
                reminder_time = datetime.datetime.strptime(time_text, "%H:%M")
                now = datetime.datetime.now()
                delta = (reminder_time - now).seconds
                if delta > 0:
                    speak(f"Reminder set for {time_text}.")
                    # Code I/P to schedule a reminder - (timers, notifications, etc).
                else:
                    speak("Sorry, the specified time is in the past. Please provide a future time.")
            except ValueError:
                speak("Sorry, I couldn't understand the time. Please try again.")

# creating a to-do list function - Code I/P
def create_todo_list():
    pass
    # Code I/P - managing a to-do list.

# Function to search the web
def search_web():
    speak("Sure, what would you like to search for?")
    search_query = recognize_speech()

    if search_query:
        pass
        # Code I/P to perform a web search and display the results.

if __name__ == "__main__":
    speak("Hello! I am your voice assistant. How can I help you today?")
    
    while True:
        user_input = recognize_speech().lower()

        if "reminder" in user_input:
            set_reminder()
        elif "to-do list" in user_input:
            create_todo_list()
        elif "search" in user_input:
            search_web()
        elif "exit" in user_input or "bye" in user_input:
            speak("Goodbye!")
            break
        else:
            speak("I'm sorry, I don't understand. Can you please repeat that?")


