import random

letters_guessed = []


def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns:
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns:
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''

    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    # Added a duplicate_check because duplicates were throwing errors

    check = []
    duplicate_check = []
    for letter in letters_guessed:
        if letters_guessed.count(letter) > 2:
            duplicate_check.append(letter)

    # Removing all the duplicates and adding one of them back

    for i in range(len(duplicate_check)):
        letters_guessed.remove(duplicate_check[i])
        if letters_guessed.count(duplicate_check[i]) < 1:
            letters_guessed.append(duplicate_check[i])

    for letter in secret_word:
        if letter in letters_guessed:
            check.append(letter)
        if set(check) == set(secret_word):
            return True
    pass


def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns:
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    string = []
    for i in secret_word:
        if i in letters_guessed:
            string.append(i)
        else:
            string.append("_")
    print("".join(string))
    pass


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''
    #TODO: check if the letter guess is in the secret word
    for i in secret_word:
        if i == guess:
            return True
    pass




def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''
    trys = 0
    finished = 0
    while finished < 1:
    #TODO: show the player information about the game according to the project spec

        print("Guess the secret word!")
        if trys == 0:
            print("you only have 7 guesses.")
    #TODO: Ask the player to guess one letter per round and check that it is only one letter

        guess = input("guess a letter:")
        while len(guess) < 1:
            guess = input("guess a better letter:")
    # taking the first letter of whatever they guess as the users guess

        guess = str(guess)
        guess = guess[0]
        letters_guessed.append(guess)
    #TODO: Check if the guessed letter is in the secret or not and give the player feedback

        if is_guess_in_word(guess, secret_word):
            print("good guess!")
            print("only "+str(7 - trys)+" guesses left!")
            get_guessed_word(secret_word, letters_guessed)
        else:
            print("try again :(")
            get_guessed_word(secret_word, letters_guessed)
            trys += 1
            print("only "+str(7 - trys)+" guesses left!")
    #TODO: show the guessed word so far

        if is_word_guessed(secret_word, letters_guessed):
            finished += 1
            print("Yay you win!")

        elif trys >= 7:
            finished += 1
            print("sorry, better luck next time")

    #TODO: check if the game has been won or lost


#These function calls that will start the game
secret_word = load_word()
spaceman(load_word())
