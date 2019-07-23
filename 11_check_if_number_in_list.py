# this program should check if an issued number is on a list


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def check(numbers):
    check = int(input("Enter the number you want to check: "))
    found = bool
    for i in numbers:
        if i == check:
            found = True
            print("Yes, that number is on the list")
        elif check not in numbers:
            found = False
            print("No, the number is not on the list")
            break

check(numbers)