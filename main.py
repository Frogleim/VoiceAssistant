import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3

def talk(words):
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()

talk("Привет скажите что нибудь")

def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Говорите")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio =  r.listen(source)
    try:
        test = r.recognize_google(audio, language="ru-RU ").lower()
        print("Вы сказали" + test)
    except sr.UnknownValueError:
        talk("Я вас не понимаю. ")
        test = command()

    return test

def makeSomething(test):
    if "открыть сайт " in test:
        talk("Открываю...")
        url = 'https://jut.su'
        webbrowser.open(url)
    if "имя" in test:
        talk("Меня зовут Аня")
    if "Расскажи о себе" in test:
        talk("Я Аня! Ваш помощник.")

    elif "стоп" in test:
        talk("Хорошо!..")
        sys.exit()

while True:
    makeSomething(command())

