# if no is divisible by 3 it should print fizz
# if no is divisible by 5 it should print buzz
# if no is divisible bt both it should print both

for i in range(1, 100):
    if i % 3 == 0 and i % 5 ==0:
        print("FIZZBUZZ!")
    elif i % 3 == 0:
        print("FIZZ")
    elif i % 5 == 0:
        print("BUZZ!")
    else:
        print(i)