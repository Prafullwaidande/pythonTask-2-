import speech_recognition as sr
import webbrowser
import pyttsx3

print("Welcome to my Tools")
pyttsx3.speak("welcome to my tools")
print("Enter ur requirements : ", end='')
# ch = input()

r = sr.Recognizer()

with sr.Microphone() as source:
   print('start say ..')
   audio = r.listen(source)
   print('we got it, speech done ..')

ch = r.recognize_google(audio)

if ("date" in ch) and (("run" in ch) or ("execute" in ch)or("open" in ch)):
   webbrowser.open("http://192.168.1.103/cgi-bin/cmd.py?c=date")
elif ("calendar" in ch) and (("run" in ch) or ("execute" in ch)):
   webbrowser.open("http://192.168.1.103/cgi-bin/cmd.py?c=cal")
else:
   print("not understand")