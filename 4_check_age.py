# this should accept input(your age) to determine
# if you are of age
# by John Doddy

your_age = int(input("What's your age: "))

if your_age >= 18:
    print("You are of age")
elif your_age < 18 and your_age > 0:
    print("You are not of age")
else:
    print("Invalid input")