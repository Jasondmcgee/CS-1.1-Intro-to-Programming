import unittest

#putting the fucntions I want to test at the top.
def is_word_guessed(secret_word, letters_guessed):
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


def is_guess_in_word(guess, secret_word):
    for i in secret_word:
        if i == guess:
            return True
    pass


def get_guessed_word(secret_word, letters_guessed):
    string = []
    for i in secret_word:
        if i in letters_guessed:
            string.append(i)
        else:
            string.append("_")
    return("".join(string))


#actually testing them
class TestStringMethods(unittest.TestCase):

    def test_is_word_guessed(self):
        secret_word = "apple"
        self.assertTrue(is_word_guessed(secret_word, 'apple'), True)
        self.assertFalse(is_word_guessed(secret_word, 'bad'), False)


    def test_is_guess_in_word(self):
        test_guess = ['a', 'aa', 'apple', 'APPLE', '!', '1']
        secret_word = 'apple'
        self.assertTrue(is_guess_in_word(test_guess[0], secret_word), True)
        for i in range(1, 5):
            self.assertFalse(is_guess_in_word(test_guess[i], secret_word), False)
            print(i)

    def test_get_guessed_word(self):
        secret_word = 'apple'
        letters_guessed = ['a', 'p', 'l', 'l', 'l' , 'e', '4', '!!!']
        self.assertEqual(get_guessed_word(secret_word, letters_guessed), 'apple')

if __name__ == '__main__':
    unittest.main()
