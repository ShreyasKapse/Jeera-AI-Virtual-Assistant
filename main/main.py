# Shreyas Kapse
# (Pocket Assistant for Students)

from tkinter import *
from urllib import response
from cv2 import meanShift
from httpx import QueryParams
from more_itertools import value_chain
import pyttsx3                              #main voice command module
import speech_recognition as sr             #for the input of voice command
from gtts import gTTS                       #google module
from playsound import playsound             
import datetime
import wikipedia
import os
import webbrowser
import smtplib
import shutil
import pyjokes
import subprocess
import wolframalpha
import tkinter
import json
import operator
import winshell
import ctypes
import time
import requests
from twilio.rest import Client
from bs4 import BeautifulSoup
from urllib.request import urlopen
import numpy as np
import cv2
import PIL.Image, PIL.ImageTk
from PIL import Image
import random


#...............................................................................................

engine = pyttsx3.init('sapi5')            #here we are importing engine voice to our program
voices = engine.getProperty('voices')
print(voices[2].id)
engine.setProperty('voice',voices[2].id)  #selecting the voices which is available in windows(default)
engine.setProperty('rate',170)

window = Tk()

global var
global var1

var = StringVar()
var1 = StringVar()

#...............................................................................................

def speak(audio):                         #this is the speak function which tell the selected voices to return the output query
    print("     ")
    print(f": {audio}")
    print("     ")
    engine.say(audio)
    engine.runAndWait()

"""This is the Function for google assistant voice"""
# def speak_assis(audio):
#     kk = gTTS(audio)
#     kk.save('Assis.mp3')
#     playsound('Assis.mp3')

#...............................................................................................
  
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning!")

    elif hour >= 12 and hour < 18:
        speak("good afternoon")

    else:
        speak("good evening")

def username():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns
     
    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))
     
    speak("How can i Help you, Sir")

#...............................................................................................

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        var.set("Listening...")
        window.update()
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        var.set("Recognizing...")
        window.update()
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
        var1.set(query)
        window.update()

    return query

'''def takeCommand_hindi():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='hi') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query
'''
#...............................................................................................

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    
    # Enable low security in gmail
    server.login('shreyaskapse1234@gmail.com', '')
    server.sendmail('kaleajinkya2003@gmail.com', to, content)
    server.close()

def speak_news():
    url = 'http://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=87787834dc284581a80bcc53cb7fcb6e'
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    speak('Source: The Times Of India')
    speak('Todays Headlines are..')
    for index, articles in enumerate(arts):
        speak(articles['title'])
        if index == len(arts)-1:
            break
        speak('Moving on the next news headline..')
    speak('These were the top headlines, Have a nice day Sir!!..')

def getNewsUrl():
    return 'http://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=87787834dc284581a80bcc53cb7fcb6e'

def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]

def meaning():
    meanby = QueryParams.split("by",1)
    try:
        soup = BeautifulSoup(requests.get(f"https://www.google.com/search?q={meanby[1]+meanShift}").text, "html.parser")
        word = soup.find("div", class_="v9i61e")
        words = ["noun", "exclamation"]
        word_list = word.text.split()
        response(meanby[1]+ " " + "means" + " " + ' '.join([i for i in word_list if i not in words]))
        print(meanby[1]+ " " + "means" + " " + ' '.join([i for i in word_list if i not in words]))
    except:
        soup = BeautifulSoup(requests.get(f"https://www.google.com/search?q={meanby[1]+meanShift}").text, "html.parser")
        word = soup.find("div", class_="BNeawe s3v9rd AP7Wnd")
        words = ["noun", "exclamation"]
        word_list = word.text.split()
        response(meanby[1]+ " " + "means" + " " + ' '.join([i for i in word_list if i not in words]))
        print(meanby[1]+ " " + "means" + " " + ' '.join([i for i in word_list if i not in words]))


#...............................................................................................

# if __name__ == "__main__":

def play():   
    btn2['state'] = 'disabled'
    btn0['state'] = 'disabled'
    btn1.configure(bg = 'orange')

    # This Function will clean any
    # command before execution of this python file
    # clear()
    wishMe()
    # username()
    speak("hello my name is Jeera")
    speak("How can i Help you, Sir")

    while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'your name' in query:
            namecmd = ['my full name is jeera, but you can call me AI','did you forgot me? i am Ai']
            speak(random.choices(namecmd))

        elif 'made you' in  query:
            speak('i am created by Sir Shreyas Kapse and Sir Ajinkya Kale, for there final year project')

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'search on youtube' in query:
            try:
                speak('what you want to search')
                ytcontent = takeCommand()
                url = 'https://www.youtube.com/results?search_query=' +(str(ytcontent))
                speak('opening youtube...')
                webbrowser.open_new_tab(url)

            except:
                speak('sorry i cannot search')

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'search on google' in query:
            try:
                speak('What you want to search?')
                content = takeCommand()
                url = "https://www.google.co.in/search?q=" +(str(content))+ "&oq="+(str(content))+"&gs_l=serp.12..0i71l8.0.0.0.6391.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.UiQhpfaBsuU"
                speak('opening google...')
                webbrowser.open_new_tab(url)
            
            except:
                speak('sorry i can not search')

        elif 'open stack overflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com") 

        elif 'play songs' in query or "play music" in query:
            music_dir = 'F:\songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\shreyas kapse\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to Shreyas' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "shreyaskapse1234@gmail.com"   
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'send a mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("whome should i send")
                to = input()   
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'shutdown my pc' in query:
            shut_down_path = 'C:\\Users\\shutdown.bat'
            speak('turning off your pc...')
            os.startfile(shut_down_path)

        elif 'create a file' in query:
            try:
                speak('please tell me a file name')
                filename = takeCommand()
                f = open(filename+'.txt',"w+")
                speak('successfully created a new text file')
                f.close()

            except:
                print('something went wrong...')

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif "calculate" in query:
             
            app_id = "K6AAVE-JQW46QXQ6W"                                      #Wolframalpha api id
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif 'search' in query or 'play' in query:
             
            query = query.replace("search", "")
            query = query.replace("play", "")         
            webbrowser.open(query)

        elif 'news' in query:
             
            speak('Ofcourse sir..')
            speak_news()
            speak('Do you want to read the full news...')
            test = takeCommand()
            if 'yes' in test:
                speak('Ok Sir, Opening browser...')
                webbrowser.open(getNewsUrl())
                speak('You can now read the full news from this website.')
            else:
                speak('No Problem Sir')

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/"+location+"")

        # elif "camera" in query or "take a photo" in query:
        #     ec.capture(0, "Jarvis Camera ", "img.jpg")
        
        
        elif 'power point presentation' in query:
            speak("opening Power Point presentation")
            power = r"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk"
            os.startfile(power)

        elif 'open bluestack' in query:
            appli = r"C:\\Users\\Public\\Desktop\\BlueStacks 5.lnk"
            os.startfile(appli)

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                       0,
                                                       "F:\\wallpapers",
                                                       0)
            speak("Background changed successfully")

        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop me from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jeera.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("jeera.txt","r")
            print(file.read())
            speak(file.read(6))

        # elif "update assistant" in query:
        #     speak("After downloading file please replace this file with the downloaded one")
        #     url = '# url after uploading file'
        #     r = requests.get(url, stream = True)
             
        #     with open("Voice.py", "wb") as Pypdf:
                 
        #         total_length = int(r.headers.get('content-length'))
                 
        #         for ch in progress.bar(r.iter_content(chunk_size = 2391975),
        #                                expected_size =(total_length / 1024) + 1):
        #             if ch:
        #               Pypdf.write(ch)

        elif 'weather' in query:
            search = "weather in Aurangabad"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"current {search} is {temp}")

        elif "send message " in query:
            speak("sir what should i say")
            msz = takeCommand()

            account_sid = 'AC3b39461291b1a4494138978cccedcfcc'
            auth_token = '004343b9a5f9dc1ba0524fa1e10f5606'

            client = Client(account_sid, auth_token)
        
            message = client.messages \
                .create(
                    body = takeCommand(),
                    from_='+19403604054',
                    to ='+918530444068'
                )
        
            print(message.sid)

        elif "what is" in query or "who is" in query:
             
            # Use the same API key
            # that we have generated earlier
            client = wolframalpha.Client("K6AAVE-JQW46QXQ6W")
            res = client.query(query)
             
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")

        elif "mean by" in query:
            meaning()



        elif "jeera" in query: 
            wishMe()
            speak("Jeera in your service sir")

        elif "Good Morning" in query:
            speak("A warm" +query)
            speak("How are you sir")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "who i am" in query:
            speak("If you talk then definitely your human.")
 
        elif "why you came to world" in query:
            speak("Thanks to Shreyas and Ajinkya. further It's a secret")
        
        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")
 
        elif "who are you" in query:
            speak("I am your virtual assistant")
 
        elif 'reason for you' in query:
            speak("I was created as a final year project by shreyas and ajinkya ")
        
        elif "how are you" in query:
            speak("I'm fine, glad you me that")

        elif "say hello" in query:
            speak("hello everyone!, my self jeera i am a voice assistant, developed for students")

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()



        
def update(ind):
    frame = frames[(ind)%100]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)

label2 = Label(window, textvariable = var1, bg = '#FAB60C')
label2.config(font=("Courier", 20))
var1.set('User Said:')
label2.pack()

label1 = Label(window, textvariable = var, bg = '#ADD8E6')
label1.config(font=("Courier", 20))
var.set('Welcome')
label1.pack()

frames = [PhotoImage(file='C:\\Users\\shreyas kapse\\OneDrive\\Documents\\final year project\\shreyas\\data base\\main images\\assist.gif',format = 'gif -index %i' %(i)) for i in range(100)]
window.title('JEERA')

label = Label(window, width = 500, height = 500)
label.pack()
window.after(0, update, 0)

btn0 = Button(text = 'WISH ME',width = 20, command = wishMe, bg = '#5C85FB')
btn0.config(font=("Courier", 12))
btn0.pack()
btn1 = Button(text = 'START',width = 20,command = play, bg = '#5C85FB')
btn1.config(font=("Courier", 12))
btn1.pack()
btn2 = Button(text = 'EXIT',width = 20, command = window.destroy, bg = '#5C85FB')
btn2.config(font=("Courier", 12))
btn2.pack()


window.mainloop()   





        









































