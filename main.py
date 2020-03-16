import os
import re
import sys
from regEx import splitFileName


while True:
	userInput = input("Please type in Season value: ")
	userInput = userInput.lstrip('0')
	userInputInt = int(userInput)
	if (userInputInt > 50 or userInputInt < 0):
		print("Please type in Season value range 0 ~ 50\n")
	else:
		break

userInputVideoName = input("Please type in video name: ")
	#userInput = userInput.lstrip('0')
	#userInputInt = int(userInput)
	#if (userInputInt > 50 or userInputInt < 0):
		#print("Please type in Season value range 0 ~ 50\n")
	#else:
		#break	
print('here')
for unTrimFileName in os.listdir(os.getcwd()):
	print(unTrimFileName)
	trimFileName = splitFileName(userInputVideoName, userInputInt, unTrimFileName)
	if trimFileName is not None:
		os.rename(unTrimFileName, trimFileName)
print('there')