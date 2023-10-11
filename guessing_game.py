"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""

#	Import the random and statistics modules.
import random
from statistics import mean, median, mode

#	Create print_stats function to display stats to player after completing the game
def print_stats(list):
	print(f"""
		all scores = {list}
		number of games played = {len(list)}
		mean = {mean(list)}
		median = {median(list)}
		mode = {mode(list)}""")

#	Create the start_game function.
def start_game():

#   Display an intro/welcome message to the player.
	print("Hello! Welcome to the number guessing game.")
	
#   Store a random number as the answer/solution.
	answer = random.randint(1, 100)
	scores = []
	guesses = 0


#   Continuously prompt the player for a guess.
	while True:
		guess = input("Guess a number between 1 and 100:   ")
		try:
			guess = int(guess)
			if guess < 1 or guess > 100:
				print("Your guess must be a number between 1 and 100.") 
		except ValueError as err:
			print("Please choose a number.")
		else:
			guesses += 1

#   Once the guess is correct, stop looping, inform the user they "Got it" and store the number of guesses it took in a list.
			if guess == answer:
				scores.append(guesses)
				print("You guessed the right number!")
				print("It took {} attempts.".format(guesses))
				print_stats(scores)

#	Prompt to play again
				continue_playing = input("Do you want to continue playing? Y/N   ")

				if continue_playing.lower() == "y":
					guesses = 0
					answer = random.randint(1, 100)
					print("The high score is", min(scores), "- see if you can beat it!")
				else:
					print("Thank you for playing! Goodbye!")
					break
				
#	If the guess is greater than the solution, display to the player "It's lower".
			elif guess > answer:
				print("It's high.")
				continue

#   If the guess is less than the solution, display to the player "It's higher".
			elif guess < answer:
				print("It's low.")
				continue

start_game()