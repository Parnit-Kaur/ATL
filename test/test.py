import playsound
from gtts import gTTS

def work(task):
	if task=='1':
		def speak(text):
		    tts=gTTS(text=text, lang="en-us")
		    filename="voice.mp3"
		    tts.save(filename)
		    playsound.playsound(filename)

		speak("Welcome to the first round of your specialization in c++")    
		print("-------------------------------------------------------------------------------------------------------------------------------------")
		print("                                                   Test For C++ ")
		print("-------------------------------------------------------------------------------------------------------------------------------------\n\n")
		f = open("test.txt", "r")
		print(f.read())
		counter=0
		ques=0
		print("-------------------------------------------------------------------------------------------------------------------------------------")
		code=input("Please read the instructions carefully before answering the code\n1. Find the missing code in the above function\n")
		ques=ques+1

		if "del->prev->next=del->next" in code:
			counter=counter+1
			print("-------------------------------------------------------------------------------------------------------------------------------------")
			print("Your answer is correct :) \n")
			
		else :
			print("-------------------------------------------------------------------------------------------------------------------------------------")
			print("Incorrect Answer :( \n")
			


		f = open("test1.txt", "r")
		print(f.read())
		print("-------------------------------------------------------------------------------------------------------------------------------------")
		code=input("Please read the instructions carefully before answering the code\n2. Find the missing code in the above function\n")
		ques=ques+1

		if "struct Node" in code:
			counter=counter+1
			print("-------------------------------------------------------------------------------------------------------------------------------------")
			print("Your answer is correct :) \n")
			
		else :
			print("-------------------------------------------------------------------------------------------------------------------------------------")
			print("Incorrect Answer :( \n")
			

		print("\n\n-------------------------------------------------------------------------------------------------------------------------------------")
		print("Your score is: {}% " .format((counter*100)/ques))
		print("-------------------------------------------------------------------------------------------------------------------------------------")
		speak("Your score is : {}%".format((counter*100)/ques))

	else:
		print("ERROR IN ACTIVITY")