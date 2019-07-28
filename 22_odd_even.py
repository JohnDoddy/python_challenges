# hackerrank challenge

# for this program
# if figure N is between 6 and 20 it should return "weird"
# if figure N isn't an odd number it should return "not weird"
# if figure N is an odd number it should return "weird"
# limits 1 >= N <= 100

def is_weird(N):
    if N < 101:
        if N % 2 == 0:
            if N in range(6,21):
                print("Weird")
            else:
                print("Not Weird")
        else:
            print("Weird")
 
if __name__ == '__main__':
    N = int(input())
    is_weird()

   