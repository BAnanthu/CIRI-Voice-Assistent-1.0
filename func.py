import aiml
from ml2en import ml2en
import re
import webbrowser
import pyttsx3
import eel
import datetime
from translate import Translator

kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")
eel.init('web', allowed_extensions=['.js', '.html'])

x = 0

@eel.expose
def assistant(command):
    if 'open college website' in command:
        reg_ex = re.search('open reddit (.*)', command)
        url = 'https://www.ukfcet.ac.in/'
        engine = pyttsx3.init()
        sound = engine.getProperty('voices')
        engine.setProperty('voice', sound[1].id)
        engine.say(" opening website")
        engine.runAndWait()
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')
    elif '* website' in command:
        reg_ex = re.search('open reddit (.*)', command)
        url = 'https://www.ukfcet.ac.in/'
        engine = pyttsx3.init()
        sound = engine.getProperty('voices')
        engine.setProperty('voice', sound[1].id)
        engine.say(" opening website")
        engine.runAndWait()
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')
    elif 'open the college website' in command:
        reg_ex = re.search('open reddit (.*)', command)
        url = 'https://www.ukfcet.ac.in/'
        engine = pyttsx3.init()
        sound = engine.getProperty('voices')
        engine.setProperty('voice', sound[1].id)
        engine.say(" opening website")
        engine.runAndWait()
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')
    elif 'open the college web site' in command:
        reg_ex = re.search('open reddit (.*)', command)
        url = 'https://www.ukfcet.ac.in/'
        engine = pyttsx3.init()
        sound = engine.getProperty('voices')
        engine.setProperty('voice', sound[1].id)
        engine.say(" opening website")
        engine.runAndWait()
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')
    elif 'show me the time' in command:
        now = datetime.datetime.now()
        print("Current date and time : ")
        print(now.strftime("%Y-%m-%d %H:%M:%S"))
        engine = pyttsx3.init()
        sound = engine.getProperty('voices')
        engine.setProperty('voice', sound[1].id)
        engine.say(now.strftime("%Y-%m-%d %H:%M:%S"))
        engine.runAndWait()
    elif 'date' in command:
        now = datetime.datetime.now()
        print("Current date and time : ")
        print(now.strftime("%Y-%m-%d %H:%M:%S"))
        engine = pyttsx3.init()
        sound = engine.getProperty('voices')
        engine.setProperty('voice', sound[1].id)
        engine.say(now.strftime("%Y-%m-%d %H:%M:%S"))
        engine.runAndWait()
    elif 'what is today' in command:
        now = datetime.datetime.now()
        print("Current date and time : ")
        print(now.strftime("%Y-%m-%d %H:%M:%S"))
        engine = pyttsx3.init()
        sound = engine.getProperty('voices')
        engine.setProperty('voice', sound[1].id)
        engine.say("today is")
        engine.say(now.strftime("%Y-%m-%d %H:%M:%S"))
        engine.runAndWait()
    elif 'open website' in command:
        reg_ex = re.search('open reddit (.*)', command)
        url = 'https://www.ukfcet.ac.in/'
        engine = pyttsx3.init()
        sound = engine.getProperty('voices')
        engine.setProperty('voice', sound[1].id)
        engine.say(" opening website")
        engine.runAndWait()
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
    else:
        engine = pyttsx3.init()
        sound = engine.getProperty('voices')
        engine.setProperty('voice', sound[1].id)
        engine.say(kernel.respond(command))
        engine.runAndWait()
        out = kernel.respond(command)
        eel.js(out)
        print(out)

    return command




def assistant1(command):
    if 'open college website' in command:
        reg_ex = re.search('open reddit (.*)', command)
        url = 'https://www.ukfcet.ac.in/'
        engine = pyttsx3.init()
        sound = engine.getProperty('voices')
        engine.setProperty('voice', sound[1].id)
        engine.say(" opening website")
        engine.runAndWait()
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')
    elif '* website' in command:
        reg_ex = re.search('open reddit (.*)', command)
        url = 'https://www.ukfcet.ac.in/'
        engine = pyttsx3.init()
        sound = engine.getProperty('voices')
        engine.setProperty('voice', sound[1].id)
        engine.say(" opening website")
        engine.runAndWait()
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')
    elif 'open the college website' in command:
        reg_ex = re.search('open reddit (.*)', command)
        url = 'https://www.ukfcet.ac.in/'
        engine = pyttsx3.init()
        sound = engine.getProperty('voices')
        engine.setProperty('voice', sound[1].id)
        engine.say(" opening website")
        engine.runAndWait()
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')
    elif 'open the college web site' in command:
        reg_ex = re.search('open reddit (.*)', command)
        url = 'https://www.ukfcet.ac.in/'
        engine = pyttsx3.init()
        sound = engine.getProperty('voices')
        engine.setProperty('voice', sound[1].id)
        engine.say(" opening website")
        engine.runAndWait()
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')
    elif 'show me the time' in command:
        now = datetime.datetime.now()
        print("Current date and time : ")
        print(now.strftime("%Y-%m-%d %H:%M:%S"))
        engine = pyttsx3.init()
        sound = engine.getProperty('voices')
        engine.setProperty('voice', sound[1].id)
        engine.say(now.strftime("%Y-%m-%d %H:%M:%S"))
        engine.runAndWait()
    elif 'date' in command:
        now = datetime.datetime.now()
        print("Current date and time : ")
        print(now.strftime("%Y-%m-%d %H:%M:%S"))
        engine = pyttsx3.init()
        sound = engine.getProperty('voices')
        engine.setProperty('voice', sound[1].id)
        engine.say(now.strftime("%Y-%m-%d %H:%M:%S"))
        engine.runAndWait()
    elif 'what is today' in command:
        now = datetime.datetime.now()
        print("Current date and time : ")
        print(now.strftime("%Y-%m-%d %H:%M:%S"))
        engine = pyttsx3.init()
        sound = engine.getProperty('voices')
        engine.setProperty('voice', sound[1].id)
        engine.say("today is")
        engine.say(now.strftime("%Y-%m-%d %H:%M:%S"))
        engine.runAndWait()
    elif 'open website' in command:
        reg_ex = re.search('open reddit (.*)', command)
        url = 'https://www.ukfcet.ac.in/'
        engine = pyttsx3.init()
        sound = engine.getProperty('voices')
        engine.setProperty('voice', sound[1].id)
        engine.say(" opening website")
        engine.runAndWait()
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
    else:
        translator = Translator(from_lang="english", to_lang="malayalam")
        t = translator.translate(kernel.respond(command))
        print(t)
        converter = ml2en()
        result = converter.transliterate(t)
        eel.js(t)
        print(result)
        engine = pyttsx3.init()
        sound = engine.getProperty('voices')
        engine.setProperty('voice', sound[1].id)
        engine.setProperty('rate', 150)
        engine.say(result)
        engine.runAndWait()
        engine.setProperty('rate', 200)

    return command


def ru():
    print("")
