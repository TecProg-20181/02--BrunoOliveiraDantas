import random
import string

WORDLIST_FILENAME = "words.txt"

class Word:
    def __init__(self, guesses):
        self.guesses = guesses
        self.secretWord = self.loadWords()
        self.lettersGuessed = []
        self.availableLetters = string.ascii_lowercase

    def loadOtherWord (self, wordlist):
        while True:
            self.secretWord = random.choice(wordlist).lower()
            if self.differentLetters() <= self.guesses:
                break

        return self.secretWord
        
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
        return self.loadOtherWord(wordlist)

    def getGuessedWord(self):
        guessed = ''
        for letter in self.secretWord:
                if letter in self.lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '
                    
        return guessed

    def isWordGuessed(self):
        for letter in self.secretWord:
            if not letter in self.lettersGuessed:
                return False
            else:
                pass

        return True

    def availableWords(self):
        if self.isWordGuessed() == False and self.guesses > 0:
                return True
        else:
                return False

    def differentLetters(self):
        differentLetters = []
        for letter in self.secretWord:
            if letter not in differentLetters:
                differentLetters.append(letter)
        return len(differentLetters)

    def startMensseger (self):
        print '*****************************'
        print 'Welcome to the game, Hangman!'
        print '*****************************'
        print 'I am thinking of a word that is', len(self.secretWord), ' letters long.'
        print 'And this word has', self.differentLetters(), ' different letters.'
        print '-------------'

    def endMenssenger (self):
        if self.isWordGuessed() == True:
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses.'
            print 'The word was ', self.secretWord, '.'

def hangman():
    guesses = 8
    word = Word(guesses)

    word.startMensseger()

    while  word.availableWords():
        print 'You have ', word.guesses, 'guesses left.'


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
            word.guesses -=1
            word.lettersGuessed.append(letter)
            print 'Oops! That letter is not in my word: ', word.getGuessedWord()
        print '------------'

    else:
        word.endMenssenger()


hangman()