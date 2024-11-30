import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

# Initialize the speech engine
engine = pyttsx3.init()

# Set rate (speed of speech)
engine.setProperty('rate', 150)

# Set volume
engine.setProperty('volume', 1.0)

# Flag to control listening state
listening = True

def speak(text):
    """Function to speak the provided text."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Function to listen for voice input and return recognized text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(Fore.GREEN + "Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
    try:
        print(Fore.YELLOW + "Recognizing...")
        command = recognizer.recognize_google(audio)
        print(Fore.CYAN + f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print(Fore.RED + "Sorry, I could not understand. Please repeat.")
        return None
    except sr.RequestError:
        print(Fore.RED + "Sorry, there was an issue with the speech service.")
        return None

def greet():
    """Function to greet the user based on the time of day."""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning!")
        print(Fore.MAGENTA + "Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
        print(Fore.MAGENTA + "Good afternoon!")
    else:
        speak("Good evening!")
        print(Fore.MAGENTA + "Good evening!")

def open_website(command):
    """Function to open a website based on user command."""
    if "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
        print(Fore.CYAN + "Opening YouTube...")
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
        print(Fore.CYAN + "Opening Google...")
    elif "open facebook" in command:
        webbrowser.open("https://www.facebook.com")
        speak("Opening Facebook")
        print(Fore.CYAN + "Opening Facebook...")
    else:
        speak("I don't know how to open that website.")
        print(Fore.RED + "I don't know how to open that website.")

def tell_time():
    """Function to tell the current time."""
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    speak(f"The time is {current_time}")
    print(Fore.YELLOW + f"The time is {current_time}")

def tell_date():
    """Function to tell the current date."""
    today = datetime.datetime.now()
    date = today.strftime("%B %d, %Y")
    speak(f"Today's date is {date}")
    print(Fore.YELLOW + f"Today's date is {date}")

def execute_command(command):
    """Function to execute commands based on user input."""
    global listening  # We will modify the listening state here
    
    if 'hello' in command or 'hi' in command:
        speak("Hello! How can I assist you today?")
        print(Fore.GREEN + "Hello! How can I assist you today?")
    elif 'time' in command:
        tell_time()
    elif 'date' in command:
        tell_date()
    elif 'open' in command:
        open_website(command)
    elif 'stop listening' in command or 'shut down' in command:
        speak("Goodbye! I will stop listening now.")
        print(Fore.RED + "Goodbye! I will stop listening now.")
        listening = False  # Stop listening
    elif 'start listening' in command:
        speak("I will start listening again.")
        print(Fore.GREEN + "I will start listening again.")
        listening = True  # Resume listening
    else:
        speak("Sorry, I didn't understand that command.")
        print(Fore.RED + "Sorry, I didn't understand that command.")

def main():
    """Main function to run the voice assistant."""
    greet()
    while True:
        if listening:
            command = listen()
            if command:
                execute_command(command)
        else:
            break  # Exit the loop if we're not listening anymore

if __name__ == "__main__":
    main()
