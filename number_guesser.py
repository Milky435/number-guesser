print("type quit to save and leave")
# setup

import sys
import time
import random
from random import randrange
# streak
streak = 0
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

  if guess == correct:
     print("correct")
     streak += 1
     time.sleep(1)
  elif guess == str(quit):
    sys.exit()
  else:
     print("wrong")
     streak = 0
     time.sleep(1)
 elif guess == "quit":
   sys.exit()
 else:
   print("epic fail: input was not quit OR a number")