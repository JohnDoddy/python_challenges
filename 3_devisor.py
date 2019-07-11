# This should let the user check all the numbers that are divisible
# with their given number between 1 and 100
# By John Doddy

your_input = int(input("Pick a number: "))
for i in range(1, 100):
    if i % your_input == 0:
        print(i)
