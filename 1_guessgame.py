import random
print("Welcome to the guessgame: ")
print("I'm thinking of a number between 0 and 10...")

while True:
    n = random.randint(0, 10)
    while True:
        guess = int(input("Take a guess: "))
        if guess >= 11:
            print("That's out of range")
        elif guess > n:
            print("That's too high")
        elif guess < n:
            print("That's too low")
        else:
            print("That was correct")
            break
