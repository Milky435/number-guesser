# setup
import random
from random import randrange
looper = True
while looper == True:
 
 num = randrange(10)
 num2 = randrange(10)
 correct = num + num2
 
 print(num, "+", num2, "=")
 guess = int(input("type answer here: "))
 
 if guess == correct:
     print("correct")
 else:
     print("wrong")