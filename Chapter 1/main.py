# print("Hello world") #our first python programm.

#installing the module in python 
#installing pyttx 

import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("""i love you so much from the bottom of my heart.
i will always be there for you.""")
engine.runAndWait()