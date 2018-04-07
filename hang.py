import random
import string

WORDLIST_FILENAME = "palavras.txt"

class Word:
    def __init__(self, guesses):
        self.guesses = guesses
        self.secretWord = self.loadWords()
        self.lettersGuessed = []
        self.availableLetters = string.ascii_lowercase
        

    def loadWords(self):
        """
        Depending on the size of the word list, this function may
        take a while to finish.
        """
        print "Loading word list from file..."
        # inFile: file
        inFile = open(WORDLIST_FILENAME, 'r', 0)
        # line: string
        line = inFile.readline()
        # wordlist: list of strings
        wordlist = string.split(line)
        print "  ", len(wordlist), "words loaded."
        return random.choice(wordlist)

    def getGuessedWord(self):
        guessed = ''
        for letter in self.secretWord:
                if letter in self.lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '
                    
        return guessed

    def isWordGuessed(self):

    #    for letter in secretWord:
    #        if letter in secretLetters:
    #            secretLetters.append(letter)
    #        else:
    #            pass

        for letter in self.secretWord:
            if letter in self.lettersGuessed:
                pass
            else:
                return False

        return True


def hangman():
    guesses = 8
    word = Word(guesses)

    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is', len(word.secretWord), ' letters long.'
    print '-------------'

    while  word.isWordGuessed() == False and guesses >0:
        print 'You have ', guesses, 'guesses left.'

        #available = word.getAvailableLetters()
        for letter in word.availableLetters:
            if letter in word.lettersGuessed:
                word.availableLetters = word.availableLetters.replace(letter, '')

        print 'Available letters', word.availableLetters
        letter = raw_input('Please guess a letter: ')
        if letter in word.lettersGuessed:
            print 'Oops! You have already guessed that letter: ', word.getGuessedWord()

        elif letter in word.secretWord:
            word.lettersGuessed.append(letter)
            print 'Good Guess: ', word.getGuessedWord()

        else:
            guesses -=1
            word.lettersGuessed.append(letter)
            print 'Oops! That letter is not in my word: ', word.getGuessedWord()

        print '------------'

    else:
        if word.isWordGuessed() == True:
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was ', word.secretWord, '.'


hangman()