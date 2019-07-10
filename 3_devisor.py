# This should let the user check all the numbers that are divisible
# with their given number between 1 and 100
# By John Doddy

your_input = int(input("Pick a number: "))
list_range = range(1, 100)

for i in list_range:
	if i % your_input == 0:
		print(i)