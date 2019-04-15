#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522
import time
import string
import os

GPIO.cleanup()
GPIO.setwarnings(False)
reader = SimpleMFRC522.SimpleMFRC522()
repeat = True

# Write function asks the user to input their name, and then assigns it to the individual tag
def write():
	text = input('New data:')
	print("Now place your tag to write")
	reader.write(text)
	print("Written")

# Read function is where most of the program occurs
def read():
	# Clears the terminal to make it look nicer.
	os.system('clear')

	# Prompts the user to scan their tag
	print("\n"+"Please hover your RFID key tag over the blue RFID reader.")

	# Handles the reading of the tags and assings the name associated with the tag into text
	# ID is what is the unique id associated with each tag....Mostly useless
	id, text = reader.read()

	# Strip clears the whitespace from the front and back of text
	text=text.strip()

	# Handles the cases where text includes numbers, as well as when tags are blank
	containsInt = False
	for x in text:
		if x == "0" or  x == "1" or x == "2" or x =="3" or x == "4" or x=="5" or x=="6" or x=="7" or x=="8" or x=="9" or len(text) == 48:
			containsInt = True

	# If the tag includes an integer, or is blank, the user is prompted to rewrite their tag.
	if containsInt:
		print("Invalid tag. Please type in your first and last name or your hacker name.\n")
		write()
	else:
		# Prints the users name and the InfoSec logo
		print("\n"+"Welcome to the InfoSec Lab, "+ "\033[1;36;40m" +  text + "\n")
		print("\033[0m"+"IIIIIIIIII                   ffffffffffffffff                   SSSSSSSSSSSSSSS"+"\n"+"I::::::::I                  f::::::::::::::::f                SS:::::::::::::::S"+"\n"+"I::::::::I                 f::::::::::::::::::f              S:::::SSSSSS::::::S"+"\n"+"II::::::II                 f::::::fffffff:::::f              S:::::S     SSSSSSS"+"\n"+"  I::::Innnn  nnnnnnnn     f:::::f       ffffffooooooooooo   S:::::S                eeeeeeeeeeee        cccccccccccccccc"+"\n"+"  I::::In:::nn::::::::nn   f:::::f           oo:::::::::::oo S:::::S              ee::::::::::::ee    cc:::::::::::::::c"+"\n"+"  I::::In::::::::::::::nn f:::::::ffffff    o:::::::::::::::o S::::SSSS          e::::::eeeee:::::ee c:::::::::::::::::c"+"\n"+"  I::::Inn:::::::::::::::nf::::::::::::f    o:::::ooooo:::::o  SS::::::SSSSS    e::::::e     e:::::ec:::::::cccccc:::::c"+"\n"+"  I::::I  n:::::nnnn:::::nf::::::::::::f    o::::o     o::::o    SSS::::::::SS  e:::::::eeeee::::::ec::::::c     ccccccc"+"\n"+"  I::::I  n::::n    n::::nf:::::::ffffff    o::::o     o::::o       SSSSSS::::S e:::::::::::::::::e c:::::c"+"\n"+"  I::::I  n::::n    n::::n f:::::f          o::::o     o::::o            S:::::Se::::::eeeeeeeeeee  c:::::c"+"\n"+"  I::::I  n::::n    n::::n f:::::f          o::::o     o::::o            S:::::Se:::::::e           c::::::c     ccccccc"+"\n"+"II::::::IIn::::n    n::::nf:::::::f         o:::::ooooo:::::oSSSSSSS     S:::::Se::::::::e          c:::::::cccccc:::::c"+"\n"+"I::::::::In::::n    n::::nf:::::::f         o:::::::::::::::oS::::::SSSSSS:::::S e::::::::eeeeeeee   c:::::::::::::::::c"+"\n"+"I::::::::In::::n    n::::nf:::::::f          oo:::::::::::oo S:::::::::::::::SS   ee:::::::::::::e    cc:::::::::::::::c"+"\n"+"IIIIIIIIIInnnnnn    nnnnnnfffffffff            ooooooooooo    SSSSSSSSSSSSSSS       eeeeeeeeeeeeee      cccccccccccccccc")

		# Gets the time and date for logging
		ts=time.ctime()

		# Creates a new file is one doesn't exist already, that keeps track of all users and the time/date they scanned
		f=open("/home/pi/Desktop/enterancerecord.txt","a+")
		f.write(text.strip() + "\t" + ts +"\n")
		f.close()

		# Waits 5 seconds before the program clears and runs again
		time.sleep(5)

# mainLoop() is the function that handles the infinite loop
def mainLoop():
	while repeat:
		read()

mainLoop()
