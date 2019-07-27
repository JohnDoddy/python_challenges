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
            if user_choice == "rock" and bot_choice == "scissors":
                print("You win")
            elif user_choice == "rock" and bot_choice == "paper":
                print("I win")
            elif user_choice == "paper" and bot_choice == "rock":
                print("You win")
            elif user_choice == "paper" and bot_choice == "scissors":
                print("I win")
            elif user_choice == "scissors" and bot_choice == "paper":
                print("You win")
            elif user_choice == "scissors" and bot_choice == "rock":
                print("I win")
            else:
                print("Use either {}".format(options))
        else:
            print("That's a tie!")

if __name__ == "__main__":
    game(options)