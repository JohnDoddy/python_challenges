# prime number is only divisible by 1 and itself

def prime(number):
    """
    Return true if a 
    number is prime
    """
    if number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

#test

for n in range(1, 21):
    print(n, prime(n))