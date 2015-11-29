#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import ksr10
import time
arm = ksr10.ksr10_class()

# obtain audio from the microphone
while 1:
	r = sr.Recognizer()
	with sr.Microphone() as source:
    		print("Say something!")
   	 	audio = r.listen(source)

	try:
  	  rn = r.recognize_google(audio)
	except sr.UnknownValueError:
	    print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
    	    print("Could not request results from Google Speech Recognition service; {0}".format(e))
	if rn == "up":
		arm.move("elbow","up")
		time.sleep(1.5)
		arm.stop()
	if rn == "down":
		arm.move("elbow","down")
		time.sleep(1.5)
		arm.stop()
	if rn == "light":
		arm.lights()
	if rn == "grip":
		with open ("Save.txt", "r") as file_:
			oc = file_.read()

		if oc == "1":
			arm.move("grip","close")
			time.sleep(1.6)
			arm.stop()
			with open ("Save.txt", "w") as file_:
				file_.write("0")
		elif oc == "0":
			arm.move("grip","open")
			time.sleep(1.4)
			arm.stop()
			with open ("Save.txt", "w") as file_:
				file_.write("1")
		else:
			print "Error, file contains: " + oc
	if rn == "stop":
		break
