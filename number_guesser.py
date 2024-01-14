print("type quit to save and leave")
# setup

import sys
import time
import random
import pickle
from random import randrange
# streak
try:
 streak = pickle.load(open("streak.p", "rb"))
except:
  print("ERROR: streak.p not found try backup?")
  time.sleep(10)
  sys.quit
# loop

looper = True
while looper == True:
 print("you have a streak of", streak)
 num = randrange(10)
 num2 = randrange(10)
 correct = num + num2
 # guessing

 is_int = False
 print(num, "+", num2, "=")
 guess = input("type answer here: ")
 # see if guess is quit or number
 try:
    guess_int = int(guess)
    is_int = True
 except:
    is_int = False
 if is_int:

  if guess_int == correct:
     print("correct")
     streak += 1
     time.sleep(1)
  else:
     print("wrong")
     streak = 0
     time.sleep(1)
 elif guess == "quit":
   sys.exit()
 else:
   print("epic fail: input was not quit OR a number")
 pickle.dump(streak, open("streak.p", "wb"))  