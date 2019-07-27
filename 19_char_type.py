# check the character type of an input


print("Enter blank to exit or...")
while True:
    I = input("Enter any word and I'll check it character type: ")

    if I.isalpha():
        print("It's a string")
    elif I.isdigit():
        print("It's a digit!")
    elif I.isalnum():
        print("It's an alphanumeric!")
    else:
        break
