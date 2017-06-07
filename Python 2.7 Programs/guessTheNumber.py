#This is a guess the number game.
import random
secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 & 20')

# Ask the player 6 times
for guessTaken in range(1,7):
	print('take the guess.')
	guess = int(raw_input())
	
	if guess < secretNumber :
		print('Your guess is too  low')
	elif guess > secretNumber :
		print('Your guess is too high')
	else:
		break 
if guess == secretNumber :
	print('Good job! You guessed my number in' + str(guessTaken) + 'guesses!')
else:
	print('Nope.The number I was thinking of was' + str(secretNumber))
