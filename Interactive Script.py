# Python Activity by Divyansh Chaturvedi
# # Interactive Script in Python # #

import webbrowser
import time

sentence = "Ohh...! You are " 
name = str(input("Write your name. \n"))

final = (sentence+name)
print(final)

time.sleep(1.5)
word = str(input("But... Sorry, didn't recognize you. May I know your full name? \n"))

if word == "Divyansh Chaturvedi":
    time.sleep(2)
    print ("Ohh... I got it now ! Welcome Back !")
else:
    time.sleep(2)
    print ("Pardon me, let me see if I can do something for you.")

time.sleep(3)
Task = str (input("I can do a work for you. I can open the browser. Shall I? \n"))

if Task == "Sure":
    webbrowser.open("https://www.google.com")
    time.sleep(5)
    print("Have fun mate !")
else:
    print("Alright, as you wish.")

# Here's the end. Hope you liked my project.
