"""
MY VOICE ASSISTANT
------------------
A simple, beginner-friendly voice assistant for Windows.

COMMANDS YOU CAN SAY:
    - "what time is it"              → real Islamabad time from internet
    - "what is today's date"
    - "what day is it"
    - "play [song name] on youtube"  → plays song directly!
    - "search google for [anything]"
    - "open google / youtube / facebook / instagram / whatsapp / gmail / claude"
    - "open my setup"                → opens PyCharm, Claude, Chrome, YouTube
    - "wikipedia [topic]"
    - "calculate [math]"
    - "tell me a joke"
    - "tell me a fact"
    - "my name is [name]"
    - "what is my name"
    - "how are you"
    - "stop / exit / quit / bye"
"""

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import pywhatkit
import pytz
import subprocess
import random
import os
import time

# ---- Set up the voice engine ----
engine = pyttsx3.init()
engine.setProperty('rate', 170)

# ---- Remember user's name ----
user_name = ""

# ---- PyCharm path — update this if yours is different ----
PYCHARM_PATH = r"C:\Program Files\JetBrains\PyCharm 2026.1.2\bin\pycharm64.exe"

# ---- Fun facts ----
facts = [
    "Honey never spoils. Archaeologists found 3000-year-old honey in Egyptian tombs that was still good.",
    "A group of flamingos is called a flamboyance.",
    "Bananas are slightly radioactive because they contain potassium-40.",
    "Octopuses have three hearts and blue blood.",
    "The Eiffel Tower can grow up to 15 centimetres taller in summer due to heat expansion.",
    "A day on Venus is longer than a year on Venus.",
    "Sharks are older than trees. They have existed for around 450 million years.",
    "There are more stars in the universe than grains of sand on all of Earth's beaches.",
]

# ---- Jokes ----
jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "I told my computer I needed a break. Now it won't stop sending me Kit-Kat ads.",
    "Why don't scientists trust atoms? Because they make up everything!",
    "What do you call a fish without eyes? A fsh!",
    "Why did the math book look sad? Because it had too many problems.",
]


def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(mic)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en-in")
        print(f"You said: {query}")
        return query.lower()
    except Exception:
        speak("Sorry, I didn't catch that. Please say it again.")
        return ""


def greet():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    if user_name:
        speak(f"Welcome back, {user_name}! How can I help you?")
    else:
        speak("I am your assistant. How can I help you?")


def get_islamabad_time():
    """Get the real current time in Islamabad using timezone."""
    try:
        islamabad_tz = pytz.timezone("Asia/Karachi")
        islamabad_time = datetime.datetime.now(islamabad_tz)
        return islamabad_time.strftime("%I:%M %p")
    except Exception:
        return None


def open_my_setup():
    """Open PyCharm, Claude, Chrome, and YouTube together."""
    speak("Opening your setup. Just a moment!")

    # 1. Open PyCharm
    try:
        if os.path.exists(PYCHARM_PATH):
            subprocess.Popen([PYCHARM_PATH])
            speak("PyCharm is opening.")
        else:
            # Try to find PyCharm in common locations
            possible_paths = [
                r"C:\Program Files\JetBrains\PyCharm Community Edition 2023.3\bin\pycharm64.exe",
                r"C:\Program Files\JetBrains\PyCharm Community Edition 2024.3\bin\pycharm64.exe",
                r"C:\Program Files\JetBrains\PyCharm 2024.1\bin\pycharm64.exe",
                r"C:\Program Files\JetBrains\PyCharm 2023.3\bin\pycharm64.exe",
            ]
            found = False
            for path in possible_paths:
                if os.path.exists(path):
                    subprocess.Popen([path])
                    speak("PyCharm is opening.")
                    found = True
                    break
            if not found:
                speak("I couldn't find PyCharm. Please update the path in the code.")
    except Exception:
        speak("Could not open PyCharm.")

    time.sleep(2)

    # 2. Open Claude
    webbrowser.open("https://claude.ai")
    speak("Claude is opening.")

    time.sleep(1)

    # 3. Open YouTube home (your recommendations will show since you are logged in)
    webbrowser.open("https://www.youtube.com")
    speak("YouTube is opening with your recommendations. Enjoy!")


def simple_calculate(command):
    try:
        expression = command.replace("calculate", "").strip()
        expression = expression.replace("plus", "+").replace("minus", "-")
        expression = expression.replace("times", "*").replace("multiplied by", "*")
        expression = expression.replace("divided by", "/")
        result = eval(expression)
        speak(f"The answer is {result}")
    except Exception:
        speak("Sorry, I couldn't calculate that. Please try again.")


def run_assistant():
    global user_name
    greet()

    while True:
        command = listen()

        if command == "":
            continue

        # ---- TIME (real Islamabad time) ----
        elif "time" in command:
            time_now = get_islamabad_time()
            if time_now:
                speak(f"The current time in Islamabad is {time_now}")
            else:
                speak("Sorry, I couldn't get the time right now.")

        # ---- DATE ----
        elif "date" in command:
            islamabad_tz = pytz.timezone("Asia/Karachi")
            current_date = datetime.datetime.now(islamabad_tz).strftime("%B %d, %Y")
            speak(f"Today's date is {current_date}")

        # ---- DAY ----
        elif "day" in command:
            islamabad_tz = pytz.timezone("Asia/Karachi")
            current_day = datetime.datetime.now(islamabad_tz).strftime("%A")
            speak(f"Today is {current_day}")

        # ---- PLAY SONG DIRECTLY ON YOUTUBE ----
        elif "play" in command and ("youtube" in command or "song" in command or "music" in command):
            song = command.replace("play", "")
            song = song.replace("on youtube", "").replace("youtube", "")
            song = song.replace("song", "").replace("music", "").strip()
            if song:
                speak(f"Playing {song} on YouTube right now!")
                pywhatkit.playonyt(song)
            else:
                speak("What song do you want me to play?")

        # ---- SEARCH GOOGLE ----
        elif "search google for" in command:
            query = command.replace("search google for", "").strip()
            if query:
                speak(f"Searching Google for {query}")
                webbrowser.open(f"https://www.google.com/search?q={query.replace(' ', '+')}")
            else:
                speak("What do you want me to search for?")

        elif "search google" in command:
            query = command.replace("search google", "").strip()
            if query:
                speak(f"Searching Google for {query}")
                webbrowser.open(f"https://www.google.com/search?q={query.replace(' ', '+')}")
            else:
                speak("What do you want me to search for?")

        # ---- OPEN MY SETUP ----
        elif "open my setup" in command or "open setup" in command:
            open_my_setup()

        # ---- OPEN WEBSITES ----
        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "open facebook" in command:
            speak("Opening Facebook")
            webbrowser.open("https://www.facebook.com")

        elif "open instagram" in command:
            speak("Opening Instagram")
            webbrowser.open("https://www.instagram.com")

        elif "open whatsapp" in command:
            speak("Opening WhatsApp Web")
            webbrowser.open("https://web.whatsapp.com")

        elif "open gmail" in command or "open email" in command:
            speak("Opening Gmail")
            webbrowser.open("https://mail.google.com")

        elif "open claude" in command:
            speak("Opening Claude")
            webbrowser.open("https://claude.ai")

        # ---- WIKIPEDIA ----
        elif "wikipedia" in command:
            speak("Searching Wikipedia...")
            topic = command.replace("wikipedia", "").strip()
            try:
                result = wikipedia.summary(topic, sentences=2)
                speak(result)
            except Exception:
                speak("I couldn't find anything on that topic.")

        # ---- CALCULATE ----
        elif "calculate" in command:
            simple_calculate(command)

        # ---- JOKES ----
        elif "joke" in command:
            speak(random.choice(jokes))

        # ---- FACTS ----
        elif "fact" in command or "tell me something" in command:
            speak(random.choice(facts))

        # ---- NAME ----
        elif "my name is" in command:
            user_name = command.replace("my name is", "").strip().title()
            speak(f"Nice to meet you, {user_name}! I will remember your name.")

        elif "what is my name" in command or "do you know my name" in command:
            if user_name:
                speak(f"Your name is {user_name}!")
            else:
                speak("I don't know your name yet. Say 'my name is' followed by your name.")

        # ---- GREETINGS ----
        elif "hello" in command or "hi" in command or "hey" in command:
            if user_name:
                speak(f"Hello {user_name}! How can I help you?")
            else:
                speak("Hello! How can I help you?")

        elif "how are you" in command:
            speak("I am doing great, thank you for asking! How can I help you?")

        # ---- STOP ----
        elif "stop" in command or "exit" in command or "quit" in command or "bye" in command:
            if user_name:
                speak(f"Goodbye {user_name}! Have a great day!")
            else:
                speak("Goodbye! Shutting down now.")
            break

        else:
            speak("I don't know how to do that yet. Try saying: play a song, search Google, open my setup, or tell me a joke.")


if __name__ == "__main__":
    run_assistant()
