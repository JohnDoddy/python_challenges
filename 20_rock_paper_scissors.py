import random

options = ["rock", "paper", "scissors"]
def bot(options):
    return random.choice(options)

def game(options):
    while True:
        user_choice = str(input("Pick. rock, paper or scissors:")).lower()
        bot_choice = bot(options)
        print("I choose {}!".format(bot_choice))
        if bot_choice != user_choice:
            if bot_choice is "rock" and user_choice is "scissors":
                print("I win!")
            elif user_choice is "rock" and bot_choice is "scissors":
                print("I lose")
            elif user_choice is "rock" and bot_choice is "paper":
                print("I lose")
            elif bot_choice is "paper" and user_choice is "rock":
                print("I win")
            elif bot_choice is "scissors" and user_choice is "paper":
                print("I win")
            elif user_choice is "scissors" and bot_choice is "paper":
                print("I lose")
            elif bot_choice is "paper" and user_choice is "rock":
                print("I win")
            elif user_choice is "scissors" and bot_choice is "paper":
                print("I lose")
        elif user_choice not in options:
            print("Use either {}".format(options))
        else:
            print("That's a tie!")

if __name__ == "__main__":
    game(options)
