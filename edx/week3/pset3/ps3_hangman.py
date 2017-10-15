# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
    False otherwise
    
    >> isWordGuessed("apple", ['e', 'i', 'k', 'p', 'r', 's'])
    False
    '''
    size = len(secretWord)
    counter = 0
    # check letter by letter
    for letter in secretWord:
        if letter in lettersGuessed:
            counter += 1
    
    return counter == size



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
    what letters in secretWord have been guessed so far.
    
    >> print(getGuessedWord("apple", ['e', 'i', 'k', 'p', 'r', 's']))
    _ pp _ e
    '''
    guessed = ""
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed = guessed + letter
        else:
            guessed += " _ "
    
    return guessed



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
    yet been guessed.
    
    >>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
    >>> print(getAvailableLetters(lettersGuessed))
    abcdfghjlmnoqtuvwxyz
    '''
    # import the alphabet in string
    from string import ascii_lowercase
    # alphabet string
    abc_string = ascii_lowercase
    # alphabet list
    abc_list = list(abc_string)
    
    # remove letters guessed
    for letter in abc_string:
        if letter in lettersGuessed:
            abc_list.remove(letter)
    
    # join list into string and return it
    abc_string = ''.join(abc_list)
    return abc_string



def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    size = len(secretWord)
    numGuesses = 8
    
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", size, "letters long.")
    print("-------------")
    
    lettersGuessed = []
    availableLetters = getAvailableLetters(lettersGuessed)
    
    while numGuesses > 0:
        print("You have", numGuesses, "guesses left.")
        print("Available letters:", availableLetters, " ")
        
        letterGuess = input("Please guess a letter: ")
        
        # When the letterGuess is new
        if letterGuess in availableLetters:
            # Append letter in lettersGuessed list
            lettersGuessed.append(letterGuess)
            # correct guess
            if letterGuess in secretWord:
                # show positions of letterGuess in secretWord
                print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
            else:
                # Substract one from numGuesses
                print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
                numGuesses -= 1
            # Refresh the availableLetters
            availableLetters = getAvailableLetters(lettersGuessed)
        # When letterGuess is NOT new
        else:
            # Notify that letter has been guessed before
            print("Oops! You've already guessed that letter:",getGuessedWord(secretWord, lettersGuessed))
        print("-------------")
        # Break the loop user if the user guess the whole word
        if isWordGuessed(secretWord, lettersGuessed):
            break
    
    if numGuesses > 0:
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was", secretWord, ".")
            


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
