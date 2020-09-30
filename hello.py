import speech_recognition as sr
import webbrowser
import pyttsx3

print("***************************************       Welcome To My Tools       ***************************************")
pyttsx3.speak("welcome to my tools, How can i help you ")

while True:	
	print("Tell Your requirements : ", end='')
	# ch = input()

	r = sr.Recognizer()

	with sr.Microphone() as source:
   		print('start say ..')
   		audio = r.listen(source)
	print('we got it, speech done ..')

	ch = r.recognize_google(audio)

	if ("date" in ch) and (("run" in ch) or ("execute" in ch)or("open" in ch)):
	   	webbrowser.open("http://192.168.1.103/cgi-bin/cmd.py?c=date")
	elif ("docker" in ch) and (("run" in ch) or ("execute" in ch) or ("open" in ch)):
	        webbrowser.open("http://192.168.1.103/drun.html")
	elif ("redhat" in ch) and (("run" in ch) or ("execute" in ch) or ("open" in ch)):
   		webbrowser.open("http://192.168.1.103/home.html")
	elif ("exit" in ch) or ("quit" in ch):
		break
	else:
 	   print("not understand")
