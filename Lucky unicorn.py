#imports the random number generator
import random

#How many times you have loss
loses = 0 

#Your starting balance
balance = 0

#Your money earned
payout = 0

#Tells the game to keep going
keepgoingL = "yes"

#Welcomes the player
print("Welcome to lucky unicorn")

#Asks user for money input
balance = int(input("How much money would you like to spend? "))

#checks if balance is over or 10 or under 1
while balance > 10 or balance < 1:
  print("Must be between 1 and 10 dollars")
  balance = int(input("How much money would you like to spend? "))

while keepgoingL == "yes":

  bet = int(input(f"You have ${balance}, How much would you like to bet on your spin? "))
  start = input("Press enter to spin")

#Checks that you can afford it
  if balance >= bet:
    
    #Chances balance
    balance -= bet

    #Shows your money loss
    loses += bet

    #Generates a random number
    num = random.randrange(1,100)

    #Checks number, 2% chance of unicorn
    if num <= 2:
      #prints the result and money earned
      print("""
      Unicorn
      """)
      print(f"You won ${bet * 5}!!!")
      #adds money to payout and balance
      balance += bet * 5
      payout += bet * 5
    elif num > 2   and num <= 40 :
      print("""
      Zebra
      """)
      print(f"You won ${bet / 2}!!!")
      payout += bet / 2
      balance += bet / 2
    elif num > 40 and num <= 70:
      print("""
      Horse
      """)
      print(f"You won ${bet / 2}!!!")
      payout += bet / 2
      balance += bet / 2
    else:
      print("""
      Donkey
      """)
      print("You won nothing!!!")
    
  else:
    #if you dont have enough money this would output
    print("Sorry you dont have enough balance")
    keepgoing = "no"
  #Checks if you have enough balance to spin again
  if balance == 0:
    print("You are out of money")
    keepgoingL = 'no'

  #Tells user their balance earnings and losses and asks them if they woulf like to continue 
  if keepgoingL == "yes": 
    print(f"So far you have won ${payout} ")
    print(f"You have loss ${loses}")
    keepgoing = input(f"Would you like to spin again you have ${balance}. (Yes/No) ")
    keepgoingL = keepgoing.lower()

#output for if user does not want to continue
if keepgoingL == "no":
  print(f"Thanks for playing you won ${payout}")
