
import speech_recognition as sr
import pyttsx3
import logging
import datetime
import os
import webbrowser
import wikipedia
import random
import subprocess

# --------------------------
# Logging configuration
# --------------------------
LOG_DIR = "logs"
LOG_FILE_NAME = "application.log"

os.makedirs(LOG_DIR, exist_ok=True)
log_path = os.path.join(LOG_DIR, LOG_FILE_NAME)

logging.basicConfig(
    filename=log_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# --------------------------
# Initialize text-to-speech engine
# --------------------------
engine = pyttsx3.init("sapi5")
engine.setProperty('rate', 200)  # Speech rate
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice

# --------------------------
# Function: Text-to-Speech
# --------------------------
def speak(text):
    """
    Convert text to speech using pyttsx3.

    Args:
        text (str): The text to be converted to speech.

    Returns:
        None
    """
    engine.say(text)
    engine.runAndWait()


# Example usage
speak("Hello, I am Jarvis, your voice assistant. How can I help you today?")

# --------------------------
# Function: Speech Recognition
# --------------------------
def take_command():
    """
    Listen to the user's voice and convert it to text using Google Speech Recognition.

    Returns:
        str: The recognized voice command as text. Returns "None" if recognition fails.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        logging.info(e)
        print("Sorry, I didn't catch that. Could you please repeat?")
        return "None"

    return query
#current time
def greeting():
    """
    Get the current time in HH:MM:SS format.

    Returns:
        str: The current time as a string.
    """
    hour=(datetime.datetime.now().hour)
    if 5 <= hour < 12:
        return "Good morning! How are you doing today?"
    elif 12 <= hour < 17:
        return "Good afternoon! How are you doing today?"
    else:
        return "Good evening! How are you doing today?"


# --------------------------
# Example usage of take_command
# --------------------------
greeting()
while True:
 query = take_command().lower()
 print(f"Recognized command: {query}")
 if "your name" in query:
     speak("My name is Jarvis, your voice assistant.")
     logging.info("User asked for Jarvis's name.")
 elif "time" in query:
     current_time = datetime.datetime.now().strftime("%H:%M:%S")
     speak(f"The current time is {current_time}")
     logging.info("User asked for the current time.")
 elif "how are you" in query:
     speak(" i am functioning properly at full capacity sir!")
     logging.info("User asked how Jarvis was doing.")
 elif "who made you" in query or "who created you" in query:
     speak("I was created by a souvik mondal.a brilliant programmer and a great human being.")
     logging.info("User asked about Jarvis's creator.")
 elif "open google" in query:
     webbrowser.open("https://www.google.com")
     speak("Opening Google.")
     logging.info("User requested to open Google.")
 #open calculator
 elif "open calculator" in query:
     subprocess.Popen('calc.exe')
     speak("Opening Calculator.")
     logging.info("User requested to open Calculator.")
 #youtube search
 elif "open youtube" in query:
     webbrowser.open("https://www.youtube.com")
     speak("Opening YouTube.")
     logging.info("User requested to open YouTube.")
# facebook search
 elif "open facebook" in query:
     webbrowser.open("https://www.facebook.com")
     speak("Opening Facebook.")
     logging.info("User requested to open Facebook.")
#open cemaera
 elif "open camera" in query:
        subprocess.Popen('start microsoft.windows.camera:', shell=True)
        speak("Opening Camera.")
        logging.info("User requested to open Camera.")
#github search
 elif "open github" in query:
     webbrowser.open("https://www.github.com")
     speak("Opening GitHub.")
     logging.info("User requested to open GitHub.")
#linkedin search
 elif "open linkedin" in query:
        webbrowser.open("https://www.linkedin.com")
        speak("Opening LinkedIn.")
        logging.info("User requested to open LinkedIn.")
#instagram search
 elif "open instagram" in query:
        webbrowser.open("https://www.instagram.com")
        speak("Opening Instagram.")
        logging.info("User requested to open Instagram.")
#note pad search
 elif "open notepad" in query:
        subprocess.Popen('notepad.exe')
        speak("Opening Notepad.")
        logging.info("User requested to open Notepad.")
#comand prompt search
 elif "open command prompt" in query:
        subprocess.Popen('cmd.exe')
        speak("Opening Command Prompt.")
        logging.info("User requested to open Command Prompt.")
 elif "open vs code" in query:
        subprocess.Popen('code.exe')
        speak("Opening Visual Studio Code.")
        logging.info("User requested to open Visual Studio Code.")
   
#jokes
 elif "jokes" in query:
     jokes = [
         "Why don't scientists trust atoms? Because they make up everything!",
         "Why did the scarecrow win an award? Because he was outstanding in his field!",
         "Why don't skeletons fight each other? They don't have the guts!",
         "Why did the bicycle fall over? Because it was two-tired!",
         "What do you call a fake noodle? An impasta!",
         "Why did the computer go to the doctor? Because it caught a virus!",
         "Why do programmers prefer dark mode? Because light attracts bugs!",
         "Why did the math book look sad? Because it had too many problems!",
         "Why did the computer show up at work late? It had a hard drive!",
         "Why did the keyboard break up with the mouse? Because it felt clicked!",
         "Why was the computer cold? It left its Windows open!",
         "Why did the laptop go to school? To improve its memory!",
         "Why did the WiFi break up with the computer? There was no connection!",
         "Why did the programmer go broke? Because he used up all his cache!",
         "Why do programmers hate nature? Too many bugs!",
         "Why was the JavaScript developer sad? Because he didn't know how to null his feelings!",
         "Why did the computer cross the road? To get a better connection!",
         "Why did the phone need glasses? It lost its contacts!",
         "Why did the developer go broke? Because he lost his domain!",
         "Why did the coder get stuck in the shower? Because the instructions were: lather, rinse, repeat!",
         "Why do programmers always mix up Christmas and Halloween? Because Oct 31 == Dec 25!",
         "Why was the computer tired? It had too many tabs open!",
         "Why did the server go to therapy? Too many requests!",
         "Why did the database administrator leave his wife? She had too many relations!",
         "Why was the computer good at music? It had great bytes!",
         "Why did the programmer bring a ladder? To reach the high-level code!",
         "Why did the computer get glasses? To improve its web sight!",
         "Why did the coder stay calm? Because he knew how to handle exceptions!",
         "Why did the robot go on vacation? It needed to recharge!",
         "Why was the computer so smart? It listened to its motherboard!",
         "Why did the programmer always carry a pencil? In case he needed to sketch!",
         "Why was the computer bad at football? It kept crashing!",
         "Why did the developer hate debugging? Because it was a real bug hunt!",
         "Why did the computer become a singer? It had good bandwidth!",
         "Why did the coder break up with his girlfriend? She had too many issues!",
         "Why did the browser go to school? To improve its cache!",
         "Why was the laptop always calm? It had good processing!",
         "Why did the robot get promoted? It worked efficiently!",
         "Why was the computer good at art? It had great graphics!",
         "Why did the keyboard go to therapy? Too many pressing issues!",
         "Why did the computer get angry? Someone pressed its buttons!",
         "Why was the internet slow? Too much traffic!",
         "Why did the developer go outside? To touch some grass!",
         "Why did the computer fail the exam? It couldn't process the questions!",
         "Why was the server always busy? Too many clients!",
         "Why did the coder sleep well? No bugs in the code!",
         "Why did the laptop laugh? It heard a funny byte!",
         "Why did the programmer sit in the sun? To improve his cache!",
         "Why did the robot smile? It found the right algorithm!",
         "Why did the computer relax? It finished its tasks!"
     ]
     joke = random.choice(jokes)
     speak(joke)
     logging.info("User requested a joke.")
  #wikipedia search
 elif "wikipedia" in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        try:
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            logging.info(f"User searched Wikipedia for: {query}")
        except Exception as e:
            speak("Sorry, I couldn't find any information on that topic.")
            logging.info(f"Wikipedia search failed for: {query} with error: {e}")

 elif "exit" in query or "quit" in query:
     speak("Goodbye! Have a great day!")
     logging.info("User requested to exit the application.")
     break

 else:
     speak("Sorry, I didn't understand that command.")
     logging.info("User said something that wasn't recognized.")
 

