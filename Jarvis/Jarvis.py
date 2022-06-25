import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #needs PyAudio; used pipwin instead of pip
import wikipedia
import smtplib
import webbrowser as wb
import os
from playsound import playsound
import json
import requests
import math
import pyaudio
import wave



from wikipedia import exceptions

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("This is Sage")


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

def date():
    Year = int(datetime.datetime.now().year)
    Month = int(datetime.datetime.now().month)
    Date = int(datetime.datetime.now().day)
    speak("Todays date is ")
    speak(Date)
    speak(Month)
    speak(Year)

def wishme():
    speak("Welcome back sir!")
    time()
    date()
    Hour = datetime.datetime.now().hour 
    if Hour >= 6 and Hour <12:
        speak("Good Morning Sir")
    elif Hour >= 12 and Hour<18:
        speak("Good Afternoon Sir")
    elif Hour >= 18 and Hour<24:
        speak("Good Evening Sir")
    else:
        speak("Good Night Sir")
    speak("How can I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        #r.pause_threshold = 5
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("I couldn't get what it. Please try saying it again...")
        return "None"
    return query

def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.echo()
    server.starttls()
    server.login('xyz@gmail.com', 'password')
    server.sendmail('thesoulrr@gmail.com', to,content)

if __name__ == "__main__":

    while True:
        query = takeCommand().lower()
        if 'time' in query:
            time()
        
        elif 'date' in query:
            date()
        
        elif 'on wikipedia' in query:
            speak("Searching...")
            query = query.replace("on wikipedia","")
            result = wikipedia.summary(query, sentences = 2)
            print(result)
            speak(result)
        
        elif 'chrome search' in query:
            speak("What should I search for ?")
            chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search)

        elif 'log out' in query:
            os.system("shutdown -1")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'send email' in query:
            try:
                speak("What should I say ?")
                content = takeCommand()
                to = 'email'
                sendmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Unable to send email")
               
        
        elif 'okie dokie' in query:
            playsound('korenani.mp3')
            speak("Aayush..... Signing Off! See You Later!")
            quit()
        elif 'weather' in query:
            api_key="8c7f564ad57288c1ea4de926e6e16110"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in celsius unit is " +
                      str(math.ceil(current_temperature-273)) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in celsius unit = " +
                      str(math.ceil(current_temperature-273)) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))
        elif 'start record' in query:
                audio = pyaudio.PyAudio()
                stream = audio.open(format=pyaudio.paInt16, channels=1,rate = 44100,input = True,frames_per_buffer=1024)
                frames = []
                try:
                    while True:
                        data = stream.read(1024)
                        frames.append(data)
                except KeyboardInterrupt:
                    pass
                stream.stop_stream()
                stream.close()
                audio.terminate()

                sound_file = wave.open("myrecording.wav","wb")
                sound_file.setnchannels(1)
                sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
                sound_file.setframerate(44100)
                sound_file.writeframes(b''.join(frames))
                sound_file.close()              
        