import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from googletrans import Translator, LANGUAGES

listener= sr.Recognizer()#understands and listens to our words
engine=pyttsx3.init()
# engine.say("hii this is Jarvis, what can i do for you?")
#try and include this

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:#sometimes mic might not work
        with sr.Microphone() as source:
            
            print("listening")#indication that it is ready to hear
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'jarvis' in command:
                # talk(command)#jarvis repeating back what we said
                command=command.replace('jarvis','')#removing alexa from the command
                print(command)#checks if jarvis is mentioned or not
            # print(command)
    except:
        pass
    return command

def run_alexa():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk("playing"+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M:%S %p')
        print(time)
        talk("Current time is"+time)
    elif 'wikipedia' or 'tell me about' or 'who' in command:
        for i in ['who','tell me about']:#make this better
            person=command.replace(i,'')
        
        info=wikipedia.summary(person,3)#give back all that information in one line
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'cutest' in command:
        talk("someone whose name ends with murthy")
    elif 'what' in command:
        talk("he is extremely sweet, seems very adorable when he speaks in kannada, pro max handsome and looks even better with his teddy")
        
    
    else:
        talk('Could you please repeat the command again') 

while True:
    run_alexa()

run_alexa()

# input_text="hello"
# output_text=""
# dest_lang='hindi'

# def translate():
#     translator=Translator()
#     translated=translator.translate(text=input_text.get(),dest=dest_lang.get())
#     output_text.delete(1.0,END)
#     output_text.insert(END,translated.text)
    
# translate()