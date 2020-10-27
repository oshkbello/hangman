#used to randomly choose a item from a list or sequence
import random 
#used to access the time of your computer 
import time

#invite player into the game
print('\nWelcome to the Hangman game by Zika \n')
name = input('Enter your name: ')
print('Hello '+ name +'! Best of Luck')
#halt the execution of the game for 2 seconds
time.sleep(2) 
print('The game is about to start!\nLets play Hangman')
#halt the execution of the game by 3 seconds
time.sleep(3) 

#defining the main function 
def main():
	#initializing global variables to be used throughout the program
	global count
	global display 
	global word
	global already_guessed
	global length 
	global play_game
	#List of hangman words for user to guess 
	words_to_guess = ['january','border','image','film','promise','kids','lungs','rhyme','damage','plants']
	#randomly select a word and save it in the variable word
	word = random.choice(words_to_guess)
	#length of the string
	length = len(word)
	count = 0
	#use to draw a lineacording to the length of the word
	display = '_' * length
	#contains the string index of correctly guess words
	already_guessed = []
	play_game = ''

#a loop to re-execute the game when the first round ends
def play_loop():
	global play_game
	play_game = input('Do you want to play again? y = yes, n = no \n')
	#different variations of y and n
	while play_game not in ['Y','y','N','n']:
		play_game = input('Do you want to play again? y = yes, n = no \n')
	if play_game == 'y':
		main()
	elif play_game =='n':
		print('Thanks for Playing. Come back next time!')
		exit()

#check for character in multiple positions
def charposition(string, char):
    pos = [] #list to store positions for each 'char' in 'string'
    for n in range(len(string)):
        if string[n] == char:
            pos.append(n)
    return pos

def hangman():
	global count
	global display
	global word
	global already_guessed
	global play_game
	limit = 5
	guess = input('This is the Hangman Word '+ display + ' Enter your guess: \n')
	guess = guess.strip()
	if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= '9':
		print('Invalid Input, Try a letter\n')
		hangman()
	elif guess in word:
		already_guessed.extend([guess])
		#this check how many times the character entered occured in the hangman word
		posit = charposition(word, guess)
		if len(posit) > 1:
			for x in range(len(posit)):
				word = word[:posit[x]] + '_' + word[posit[x] + 1:]
				display = display[:posit[x]] + guess + display[posit[x] + 1:]
		else:
			index = word.find(guess)
			word = word[:index] + '_' + word[index + 1:]
			display = display[:index] + guess + display[index + 1:]
		#index = word.find(guess)
		#word = word[:index] + '_' + word[index + 1:]
		#display = display[:index] + guess + display[index + 1:]
		print(display + '\n')
	elif guess in already_guessed:
		print('Letter already guessed. Try another letter. \n')
	else:
		count += 1
		if count == 1:
			time.sleep(1)
			print('  ______ \n'
				  ' |       \n'
				  ' |       \n'
				  ' |       \n'
				  ' |       \n'
				  ' |       \n'
				  ' |       \n'
				  '_|_\n')
			print('Wrong guess. '+ str(limit - count) + 'guesses remaining\n')
		elif count == 2:
			time.sleep(1)
			print('  ______ \n'
				  ' |      |\n'
				  ' |      |\n'
				  ' |       \n'
				  ' |       \n'
				  ' |       \n'
				  ' |       \n'
				  '_|_\n')
			print('Wrong guess. '+ str(limit - count) + 'guesses remaining\n')
		elif count == 3:
			time.sleep(1)
			print('  ______ \n'
				  ' |      |\n'
				  ' |      |\n'
				  ' |      |\n'
				  ' |       \n'
				  ' |       \n'
				  ' |       \n'
				  '_|_\n')
			print('Wrong guess. '+ str(limit - count) + 'guesses remaining\n')
		elif count == 4:
			time.sleep(1)
			print('  ______ \n'
				  ' |      |\n'
				  ' |      |\n'
				  ' |      |\n'
				  ' |      o\n'
				  ' |       \n'
				  ' |       \n'
				  '_|_\n')
			print('Wrong guess. '+ str(limit - count) + ' guesses remaining\n')
		elif count == 5:
			time.sleep(1)
			print('  ______ \n'
				  ' |      |\n'
				  ' |      |\n'
				  ' |      |\n'
				  ' |      o\n'
				  ' |     /|\  \n'
				  ' |     /|\  \n'
				  '_|_\n')
			print('Wrong guess. You are hanged!!! \n')
			print('The word was:', already_guessed,word)
			play_loop()

	if word == '_'* length:
		print('Congrats! You have guess the word correctly!')
		play_loop()

	elif count != limit:
		hangman()

main()
hangman()
