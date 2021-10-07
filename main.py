import speech_recognition as sr
import pyttsx3
import pyjokes
import wikipedia
import pywhatkit
import datetime
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_hand_command():
     try:
         command = input("What can I do for you ?")
     except:
         pass
     return command
def take_voice_command():
    try:
        with sr.Microphone() as source:
                print('Listening...')
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                engine.say(command)
                command = command.lower()
                engine.runAndWait()
                talk(command)
    except:
       pass
    return command
def run_germain():
        command = take_hand_command()
        if 'time' in command:
            time = datetime.datetime.now().strftime('%H:%M:%S')
            print('Current time is : ' + time)
            talk('Current time is ' + time)
        elif 'joke' in command:
            joke = pyjokes.get_joke()
            print(joke)
            talk(joke)
        elif 'play' in command:
            command = command.replace('play', '')
            pywhatkit.playonyt(command)
        elif 'who is ' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 5)
            print(info)
            talk(info)
        else:
            talk('please say the command one more time, what can I do for you ?')
while True:
 run_germain()




