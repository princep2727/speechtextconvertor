import pyttsx3

data = input("this text you should speak up!.:\n")

engine = pyttsx3.init()
engine.say(data)
engine.runAndWait()