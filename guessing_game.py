"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""

# Import the random and statistics modules.
import random
from statistics import mean, median, mode

# Create print_stats function to display stats to player after completing the game
def print_stats(list):
	print(f"""
		all scores = {list}
		number of games played = {len(list)}
		mean = {mean(list)}
		median = {median(list)}
		mode = {mode(list)}""")

# Create the start_game function.
def start_game():

#   1. Display an intro/welcome message to the player.
	print("Hello! Welcome to the number guessing game.")
	
#   2. Store a random number as the answer/solution.
	answer = random.randint(1, 100)
	scores = []
	tries = 0


#   3. Continuously prompt the player for a guess.
	while True:
		guess = input("Guess a number between 1 and 100:   ")
		try:
			guess = int(guess)
			if guess < 1 or guess > 100:
			print("Your guess must be a number between 1 and 100.")
		except ValueError as err:
			print("please choose a number.")

		if guess == answer:
			print("You guessed the right number!")
			break
#     a. If the guess is greater than the solution, display to the player "It's lower".
		elif guess < answer:
			print("It's low.")
			continue
#     b. If the guess is less than the solution, display to the player "It's higher".
		elif guess > answer:
			print("It's high.")
			continue



# Write your code inside this function.

#   When the program starts, we want to:
#   ------------------------------------



#   4. Once the guess is correct, stop looping, inform the user they "Got it" and store the number of guesses it took in a list.
#   5. Display the following data to the player
#     a. How many attempts it took them to get the correct number in this game
#     b. The mean of the saved attempts list
#     c. The median of the saved attempts list
#     d. The mode of the saved attempts list
#   6. Prompt the player to play again
#     a. If they decide to play again, start the game loop over.
#     b. If they decide to quit, show them a goodbye message.

# ( You can add more features/enhancements if you'd like to. )


# Kick off the program by calling the start_game function.
