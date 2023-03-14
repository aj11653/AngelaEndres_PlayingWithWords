from colorama import Fore, Back, Style

# Function that prints out a letter with a colorful background
def printColorfulLetter(letter, isLetterInWord, isLetterInCorrectPlace=False):
  # If it's not in the word, display it with a red background
  if (not isLetterInWord):
    print(Back.RED + Fore.WHITE + f" {letter} ", end="")
  # If it's in the word...
  else:
    # ...and it's also in the right place, display it with a green background
    if (isLetterInCorrectPlace):
      print(Back.LIGHTGREEN_EX + Fore.WHITE + f" {letter} ", end="")
    # ...but in the wrong place, display it with a yellow background
    else:
      print(Back.LIGHTYELLOW_EX + Fore.BLACK + f" {letter} ", end="")

# Display a guess, where each letter is color-coded by it's accuracy
def printGuessAccuracy(guess, actual):
  # Loop through each index/position
  for index in range(6):
    # Grab the letter from the guess
    letter = guess[index]
    # Check if the letter at this index of the user's guess is in the secret word AT ALL or not
    if (letter in actual):
      # If the letter is in the secret word, is it also AT THE CURRENT INDEX in the secret word?
      if (letter == actual[index]):
        # Then print it out with a green background
        printColorfulLetter(letter, True, True)
      # If it's not at the current index, we know by this point in the code that it's still used in the secret word somewhere...
      else:
        # ...so we'll print it out with a yellow background
        printColorfulLetter(letter, True, False)
    # ...but if the letter is not in the word at all...
    else:
      # ...print it out with a red background
      printColorfulLetter(letter, False, False)
    print(Style.RESET_ALL + " ", end="")

# Create a function called getSixLetterInput() that prompts the user to enter a guess, and ensures the guess is six characters long.
def getSixLetterInput():
  wordGuess = input("Enter a 6 letter word: ")
# If they enter a guess that is too short or too long, it should continue to re-prompt the user to enter a new guess until they enter one that is exactly six characters long
  while (not len(wordGuess) == 6):
    wordGuess = input("Enter a 6 letter word: ")
  return wordGuess

# Create a function that makes sure the guess only consists of letters
def onlyContainsLetters(guess):
  while (not guess.isalpha()):
    print("Please only use letters!")
    guess = getSixLetterInput()
  return guess

# Introduce the game rules
print("Welcome to Word Play!")
print("=====================")
print("You have five tries to guess the correct word.")
print(
  "The word is SIX characters long, and you must enter a guess of this length."
)
print("If a letter is in the correct position, it will be green.")
print(
  "If a letter is in the word but NOT in the correct position, it will be yellow."
)
print("If the letter is NOT in the word, it will be red.")
# Come up with a "secret word" that the user's goal is to guess. This word must be exactly six characters long - no more, no less
secretWord = "forest"

# The game should give the user a turn until they either guess the word correctly or have six incorrect guesses. On each turn, the user should be prompted to enter a six letter word then display the color-coded guess to find out close their guess is.
for turn in range(6):
  wordGuess = getSixLetterInput()
  wordGuess = onlyContainsLetters(wordGuess)
  # Turns all letters to lower case
  if (not wordGuess.islower()):
    wordGuess = wordGuess.lower()
  printGuessAccuracy(wordGuess, secretWord)
  # Checks if they got the secret word
  if (wordGuess == secretWord):
    print()
    print("You win!")
    # Ends the game when they get the secret word
    break
# At the end of the 6 turns, if they did not guess the word, they lose
if (wordGuess != secretWord):
  print()
  print("You lose!")
