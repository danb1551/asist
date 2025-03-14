import pyttsx3
import speech_recognition as sr
import datetime
import pyjokes
import pywhatkit
import pyautogui
import wikipedia
import webbrowser

listner = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 250)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Poslouchám...")
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            command = command.lower()
            print(command)
            return command
    except:
        return ""

def greeting():
    current_time = datetime.datetime.now()
    hour = current_time.hour
    if 3 <= hour < 12:
        talk('dobre rano')
    elif 12 <= hour < 18:
        talk('dobre odpoledne')
    else:
        talk('ahoj')
def run_jarvis():
    command = take_command()
    if 'ahoj' in command:
        talk('ahoj jak se mas')

    elif 'vtip' in command:
        talk(pyjokes.get_joke())

    elif 'exit' in command:
        talk('goodbye')
        exit()

    elif 'play' in command:
        song = command.replace('play', "")
        talk('playing', + song)
        pywhatkit.playonyt(song)

    elif 'open' in command:
        command = command.replace('open', '')
        pyautogui.press('super')
        pyautogui.write(command)
        pyautogui.sleep(1)
        pyautogui.press('enter')
        talk('opening', + command)

    elif 'close' in command:
        pyautogui.hotkey('alt', 'f4')
        talk("closing sir")

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'remember that' in command:
        rememberMessage = command.replace('remember that', '')
        talk('you told me to remember that', + rememberMessage)
        remember = open('remember.txt' , "a")
        remember.write(rememberMessage)
        remember.close()

    elif 'what do yo remember' in command:
        remember = open('remember.txt' , "r")
        print(remember)
        talk("you told me to remember" + remember.read())

    elif 'clear remember file' in command:
        file = open('remember.txt' , "w")
        file.write(f"")
        talk("done sir, everything that i remember is deleted")

    elif 'time' in command:
        time = datetime.datetime.now().strfLine("%I:%M %p")
        print(time)
        talk("current time is ", + time)

    elif 'shutdown' in command:
        talk("shuting down the pc in")
        talk("3. 2. 1.")
        os.system("shutdown /s /t 1")

    elif 'restart' in command:
        talk("restarting the pc in")
        talk("3. 2. 1.")
        os.system("shutdown /r /t 1")

    elif 'search' in command:
        usercm = command.replace("search" , "")
        usercm = usercm.lower()
        webbrowser = open(f"{usercm}")
        talk("that is what i found on the internet")

    elif 'pause' in command or 'start' in command:
        pyautogui.press("k")
        talk("done sir!")

    elif 'full screen' in command:
        pyautogui.press("f")
        talk("done sir!")

    elif 'theather screen' in command:
        pyautogui.press("t")
        talk("done sir!")
        
    elif 'theather screen' in command:
        pyautogui.press("t")
        talk("done sir!")

 #   else:
  #      talk('nastala chyba')

while True:
    run_jarvis()