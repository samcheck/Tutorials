#Guess the number game
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number from 1 to 20')

#Ask the player to guess 6 times
for guessesTaken in range(1, 7):
	print('Take a guess')
	guess = int(input())
	
	if guess < secretNumber:
		print('Your guess is too low.')
	elif guess > secretNumber:
		print('Your guess is too high.')
	else:
		break #This condition is the correct guess!
		
if guess == secretNumber:
	print('Good Job! You guessed the number in', str(guessesTaken), 'guesses!')
else:
	print('Nope. The number was', str(secretNumber))
