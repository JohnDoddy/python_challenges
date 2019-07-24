# password system

correct = bool
attempts = 0
while correct:
    password = input("What's your password: ")
    if len(password) <= 9:
        attempts += 1
        print("A password should usually be more than 9 characters long") 
    elif attempts >= 3:
        print("You have maxed out your attempts")
        break
    elif password != "acoolpassword":
        attempts += 1
        print("Wrong Password")
    else:
        ("Wrong password")