import speech_recognition as sr
import pyttsx3
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
#engine.setProperty('voice',voices[2].id)
engine.say("I'm russian, my name is Tihon")
engine.say("Я русский , меня зовут Тихон")
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()


try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            engine.say(command)
            command = command.lower()
            engine.runAndWait()
            talk(command)

except:
        pass
     #return command
