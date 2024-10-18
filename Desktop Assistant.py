
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Setting voice to the second voice


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 17:
        speak("Good Afternoon!")

    elif hour >= 17 and hour < 19:
        speak("Good Evening!")

    else:
        speak("Hi! I am Minal!")
    speak("I am a Program Developer!")
    speak("The beauty of nature makes us feel good.")


def takeCommand():
    # It takes microphone input from the user and returns string output

    rr = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        rr.pause_threshold = 1
        audio = rr.listen(source)

    try:
        print("Recognizing...")
        query = rr.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        speak("Connection error")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rajgireminal4@gmail.com', 'rajgireminal@1999')  # Be cautious with hardcoded credentials
    server.sendmail('rajgireminal4@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "hello" in query or "hello Trushali" in query:
            hello1 = "Hello! How may I help you?"
            print(hello1)
            speak(hello1)

        elif "who are you" in query or "about you" in query or "your details" in query:
            who_are_you = "I am Trushali, an AI-based computer program. I can assist you with many tasks!"
            print(who_are_you)
            speak(who_are_you)

        elif 'who make you' in query or 'who made you' in query or 'who created you' in query:
            speak("For your information, Prasun Roy created me! Would you like to see his LinkedIn profile? Yes or no.")
            ans_from_user = takeCommand()
            if 'yes' in ans_from_user:
                webbrowser.open("https://www.linkedin.com/in/minal-rajgire-a49b14244/?originalSubdomain=in")
                speak("Opening his profile. Please wait.")
            elif 'no' in ans_from_user:
                speak("Alright!")
            else:
                speak("I can't understand. Please say that again!")

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
            speak("Opening YouTube")

        elif 'open github' in query:  # Corrected the line break
            webbrowser.open("https://www.github.com")
            speak("Opening GitHub")

        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com")
            speak("Opening Facebook")

        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")
            speak("Opening Instagram")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("Opening Google")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("Opening Stack Overflow")

        elif 'open yahoo' in query:
            webbrowser.open("https://www.yahoo.com")
            speak("Opening Yahoo")

        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com")
            speak("Opening Gmail")

        elif 'open snapdeal' in query:
            webbrowser.open("https://www.snapdeal.com")
            speak("Opening Snapdeal")

        elif 'open amazon' in query or 'shop online' in query:
            webbrowser.open("https://www.amazon.com")
            speak("Opening Amazon")

        elif 'open flipkart' in query:
            webbrowser.open("https://www.flipkart.com")
            speak("Opening Flipkart")

        elif 'play music' in query:
            speak("Okay, I am playing music")
            music_dir = 'E:\\My MUSIC'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'video from pc' in query or "video" in query:
            speak("Okay, I am playing videos")
            video_dir = 'E:\\My Videos'
            Videos = os.listdir(video_dir)
            print(Videos)
            os.startfile(os.path.join(video_dir, Videos[0]))

        elif 'goodbye' in query:
            speak("Goodbye!")
            exit()

        elif "shutdown" in query:
            speak("Shutting down")
            os.system('shutdown -s')

        elif "your name" in query or "sweet name" in query:
            naa_mme = "Thanks for asking! My name is Suzi."
            print(naa_mme)
            speak(naa_mme)

        elif "how are you" in query:
            setMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!']
            ans_qus = random.choice(setMsgs)
            speak(ans_qus)
            speak("How are you?")
            ans_from_user = takeCommand()
            if 'fine' in ans_from_user or 'happy' in ans_from_user:
                speak('Great!')
            elif 'not' in ans_from_user or 'sad' in ans_from_user:
                speak('Tell me how I can make you happy')
            else:
                speak("I can't understand. Please say that again!")

        elif 'exit' in query or 'stop' in query:
            speak('See you soon. Bye!')
            exit()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            codePath = "D:\\vs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("Opening Visual Studio Code")

        elif 'email to prasun' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "rajgireminal4@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email")

        else:
            tempp = query.replace(' ', '+')
            search_url = "https://www.google.com/search?q="
            res = "Sorry, I can't understand, but I'll search the internet for an answer."
            print(res)
            speak(res)
            webbrowser.open(search_url + tempp)
