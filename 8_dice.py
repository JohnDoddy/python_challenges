# this program should simulate a dice by choosing a random number between 1 and 6

import random

roll_again = True
while True:
    print("The dice rolled is " + str(random.randint(1, 6))) 
    again = input("Press enter to roll again... else ctrl-c: ")