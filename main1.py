rom tempfile import template
import eel
import speech_recognition as sr
from gevent import os
import pyaudio
from translate import Translator
import pyttsx3
import os
from func import assistant
from func import assistant1

eel.init('web', allowed_extensions=['.js', '.html'])


@eel.expose  # Expose this function to Javascript
def say_hello_py(x):
    print('Hello from %s' % x)
    engine = pyttsx3.init()
    sound = engine.getProperty('voices')
    engine.setProperty('voice', sound[1].id)
    print("\n\n\tCHOOSE A LANGUAGE")
    engine.say("helo! i'am ciri, please choose a language")
    engine.say("1 for english ,2 for malayalam")
    engine.runAndWait()


@eel.expose
def myCommand_english():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        engine = pyttsx3.init()
        sound = engine.getProperty('voices')
        engine.setProperty('voice', sound[1].id)
        print("what can i do for you :")
        engine.say("what can i do for you :")
        engine.runAndWait()
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print('You said : ' + command + '\n')
        eel.js1(command)

    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        engine.say("Sorry could not recognize what you said")
        engine.setProperty('rate', 120)
        engine.setProperty('volume', 0.9)
        engine.runAndWait()
        command = myCommand_english()
        eel.js1(command)
    return assistant(command)


@eel.expose
def repeat():
    while True:
        myCommand_english()


@eel.expose
def myCommand_malayalam():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        engine = pyttsx3.init()
        sound = engine.getProperty('voices')
        engine.setProperty('voice', sound[1].id)
        
        print("എനിക്ക് നിങ്ങളെ എങ്ങനെ സഹായിക്കാനാകും :")
        engine.setProperty('rate', 120)
        engine.setProperty('volume', 0.9)
        engine.say("Enikku ningale engane sahaayikkaam")
        engine.runAndWait()
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        print("കേൾക്കുന്നു...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language='ml-IN')
        print('You said: ' + text + '\n')
        eel.js1(text)
        translator = Translator(from_lang="malayalam", to_lang="english")
        command = translator.translate(text)

    except sr.UnknownValueError:
        print('ക്ഷമിക്കണം ,നിങ്ങൾ എന്താണ് പറഞ്ഞതെന്ന് തിരിച്ചറിയാൻ കഴിഞ്ഞില്ല')
        engine.say("Kshamikkanam ,ningal enthaanu paranjathennu thiricchariyaan kazhinjilla")
        engine.setProperty('rate', 120)
        engine.setProperty('volume', 0.9)
        engine.runAndWait()
        command = myCommand_malayalam()
        eel.js1(command)
    return assistant1(command)


@eel.expose
def repeat1():
    while True:
        myCommand_malayalam()


@eel.expose
def pass_variable():
    variable = 25
    return dict(variable=variable)


eel.start('index.html', size=(1000, 600))
 #it will open the window
