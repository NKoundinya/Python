Hangman=(
"""
    ----
   |    |
   |    0
   |
   |
   |
   |
   |
   |
-------
"""
,
"""
    ----
   |    |
   |    0
   |    +
   |    
   |    
   |   
   |   
   |
-------
"""
,
"""
    ----
   |    |
   |    0
   |   -+-
   |    
   |    
   |
   |
   |
-------
"""
,
"""
    ----
   |    |
   |    0
   |  /-+-
   |    
   |
   |   
   |   
   |
-------
"""
,
"""
    ----
   |    |
   |    0
   |  /-+-/
   |    
   |    
   |   
   |   
   |
-------
"""
,
"""
    ----
   |    |
   |    0
   |  /-+-/
   |    |
   |    
   |
   |
   |
-------
"""
,
"""
    ----
   |    |
   |    0
   |  /-+-/
   |    |
   |
   |
   |
   |
-------
"""
,
"""
    ----
   |    |
   |    0
   |  /-+-/
   |    |
   |    |
   |
   |
   |
-------
"""
"""
    ----
   |    |
   |    0
   |  /-+-/
   |    |
   |    |
   |   | |
   |
   |
-------
"""
,

"""
    ----
   |    |
   |    0
   |  /-+-/
   |    |
   |    |
   |   | |
   |   | |
   |
-------
"""
)
import random
Max=len(Hangman)-1
used=[]
wrong=0
words=("Karl","Stark","Tony","Steve","Nat","Mine","Bucky")
word=""
diff=input(" Difficult level : \n1.Easy \n 2.Medium \n 3.Hard \n Option: ")
if diff==1:
 print "My whole book : ",words
 word=random.choice(words)
elif diff==3:
 word=random.choice(words)
elif diff==2:
 print " Some words are ",words[0:random.randrange(len(words))]
 word=random.choice(words)
else:
 print " There's no such level , Thanks "
 exit()
blank="-"*len(word)
#guess=raw_input("Guess: ")
while wrong<Max and blank!=word:
 print Hangman[wrong]
 print used
 print blank
 guess=raw_input("Guess a letter in Word I picked randomly: ")
 while guess in used:
  print guess," is already done.Can`t you see ",used
  guess=raw_input(" Guess again: ")
 used.append(guess)
 if guess in word:
  print "Yes ",guess," is in word "
  used.append(guess)
  new=""
  for i in range(len(word)):
   if guess==word[i]:
    new+=guess
   else:
    new+=blank[i]
  blank=new
 else:
  print guess," is not in Word"
  wrong+=1
if wrong==Max:
 print Hangman[wrong]
 print " You lost and hanged! Hahaha",word
else:
 print "You've found it"
