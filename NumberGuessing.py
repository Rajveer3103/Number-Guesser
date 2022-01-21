import random
import math

x = random.randint(1,10)

count = 0

while count < math.log(10 - 1 + 1, 2):
	count += 1

	guess = int(input("Guess a number:- "))

	if x == guess:
		print("Congratulations you did it in ",
			count, " try")
		break
	elif x > guess:
		print("You guessed too small!")
	elif x < guess:
		print("You Guessed too high!")


