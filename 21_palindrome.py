# check if a word is a palindrome

def check_palindrome(words):
    if words == words[::-1]:
        print("Yes, {} is a palindrome".format(words))
    else: 
        print("No, {} is not a palindrome".format(words))


check_palindrome(words=str(input("Enter a word you think is a palindrome: ")))
