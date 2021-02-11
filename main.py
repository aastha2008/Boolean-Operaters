'''
02/08/2021
Boolean Operators 
-Used as conjuntions to combine or exclude keywords in a search

A=True
B=False
C=5>3 #True
D=6==4 #False

if(A and B): #True and False>>False

elif(C of D): #True of False>>True

Truth table
  A       B    A and B    A or B    not A   
  True    True    True      True    False
  True    False   False     True    False
  False   True    False     True    True
  False   False   False     False   True


print(5=="five" or not(5>1 and not 0!=0) or False and not 6>=6 and 10<=11)
print(5=="five" or not(True and not False))


## Side Note
Assignment operators
Addition
A += 1 >> A = A + 1

Incrementation
A++ >> A= A + 1

Decremanation


=========================================================================
Random Number Generator

A Function that let the computer pick a number within a range.




a = 0
# Import a random library
import random
coin = random.randint(0,1)

if (coin == 1):
  print ("head")
else:
  print ("tail")

## print (random.randint(0, 10))


# Rollin a dice (6 sides)
import random
dice = random.randint(1,6)
#print ("Dice value is: " + str(dice))

if (dice == 1):
  print ("you rolled a 1")
elif (dice == 2):
  print ("you rolled a 2")
elif (dice == 3):
  print ("you rolled a 3")
elif (dice == 4):
  print ("you rolled a 4")
elif (dice == 5):
  print ("you rolled a 5")
else:
  print ("You rolled a 6")

  # Exercise:  Rock Paper Scissors (RPS)
'''

import random
print ("Welcome to RPS")
print ("1. rock")
print ("2. paper")
print ("3. scissors")
p1 = input("Enter your choice: ")

cpu = random.randint(1,3)
print("The computer choice is: " + str(cpu))

# convert 1: rock
if (p1 == "1" or p1 == "rock"):
  p1 = 1

# convert 2: paper
elif (p1 == "2" or p1 == "paper"):
  p1 = 2

# convert 3: scissors
elif (p1 == "3" or p1 == "scissors"):
  p1 = 3


# Rock vs Rock.    (t)
# Rock vs Paper.   (l)
# Rock vs Scissors (w)

# Paper vs Rock      (w)
# Paper vs Paper.    (t)
# Paper vs Scissors. (l)  

# Scissors vs Rock.    (l)
# Sciccors vs Paper.    (w)
# Sciccors vs Scissors. (t)

#player tied
if(p1==cpu):
  print("You've tied")

#player won
elif ( (p1==2 and cpu==1) or (p1==3 and cpu==2) or (p1==1 and cpu==3) ):
  print("Player has won")

#player lost
elif ((p1==1 and cpu==2) or (p1==3 and cpu==1) or (p1==2 and cpu==3) ):
  print("Player has lost")

'''
if (p1 == cpu):
  print ("Tied")

# player won:
elif (p1 == 1 and cpu == 3):
  print ("Player won")

# player won:
elif (p1 == 2 and cpu == 1):
  print ("Player won")

# player won:
elif (p1 == 3 and cpu == 2):
  print ("Player won")

# player lost:
elif (p1 == 1 and cpu == 2):
  print ("Player lost")

# player won:
elif (p1 == 2 and cpu == 3):
  print ("Player lost")

# player won:
elif (p1 == 3 and cpu == 1):
  print ("Player lost")
'''






