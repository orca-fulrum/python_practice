# Problem Set 2, hangman.py
# Name: Max Chemerysky
# Collaborators:
# Time spent: 2 days approximately, most time spent on match_with_gaps((

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    if str(secret_word).lower() == str(letters_guessed).lower():
      return True
    else:
      return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    word = str()
    for a in secret_word:
        if a in letters_guessed:
            word += a
        else:
            word += "_ "
    return word



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    word = str()
    for a in string.ascii_lowercase:
        if a not in letters_guessed:
            word += a
        else:
            continue
    return word
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    lenght = len(secret_word)
    guesses_rem = 6
    warnings_rem = 3
    letter = str()
    letters_list = []
    letters_guessed = []
    print("Welcome to the Hangman!")
    print(f"My word is {lenght} letters long")
    print(f"Your amount of warnings: {warnings_rem}")
    print("Let the game begin!")
    print("___________________")
    while guesses_rem != 0:
      print(f"You have {guesses_rem} guesses left")
      print(f"Available letters: {get_available_letters(letters_guessed)}")
      letter_check = get_available_letters(letters_guessed)
      while True:
        letter = str(input("Guess a letter: "))
        if letter.isalpha() == False or len(letter) != 1:
          warnings_rem -= 1
          print(f"Invalid input, you'll pay for your mistake: you have {warnings_rem} warning(s) left")
          if warnings_rem == 0:
            break
          continue
        elif letter not in letter_check:
          print("You've already guessed this letter")
          continue
        else:
          letters_guessed.append(letter)
          break
      if letter in str(secret_word):
        letters_list.append(letter)
        print(f"Well played, you're right! {get_guessed_word(secret_word, letters_list)}")
      else:
        print(f"You're wrong( {get_guessed_word(secret_word, letters_list)}")
        if letter in "aeoui":
          guesses_rem -= 2
        elif letter in "bcdfghjklmnpqrstvwxyz":
          guesses_rem -= 1
      print("________________________")
      if is_word_guessed(secret_word, get_guessed_word(secret_word, letters_list)) == True:
        break
      if warnings_rem == 0:
        break

    
    if is_word_guessed(secret_word, get_guessed_word(secret_word, letters_list)) == True:
      print(f"Congrats, you won! Your score: {guesses_rem * len(set(secret_word))}")
    else:
      print(f"You lost, but nice try anyway, secret word was: {secret_word}")




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word_letters = str(my_word).replace(" ", "")
    if len(my_word_letters) == len(other_word): #only words file with same lenght as my_word
        for a in range(len(my_word_letters)):
            if my_word_letters[a] == other_word[a]: #letters match
                continue
            elif my_word_letters[a] == "_" and other_word[a] not in my_word_letters: #"_" in my word and unknown yet letter in other word
                continue
            else:
                return False #letters dont match or this letter is already known/checked
        return True
    else:
        return False



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    matches = 0
    print("My word is somewhere here, choose wisely: ")
    for a in wordlist:
      if match_with_gaps(my_word, a) == True:
        print(a, end = " ")
        matches += 1
        continue
      else:
        continue
    if matches == 0:
      print("Zero matches found")
    print("")
    



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    lenght = len(secret_word)
    guesses_rem = 6
    warnings_rem = 3
    letter = str()
    letters_list = []
    letters_guessed = []
    print("Welcome to the Hangman with hints!")
    print(f"My word is {lenght} letters long")
    print(f"Your amount of warnings: {warnings_rem}")
    print("Let the game begin!")
    print("___________________")
    while guesses_rem != 0:
      print(f"You have {guesses_rem} guesses left")
      print(f"Available letters: {get_available_letters(letters_guessed)}")
      letter_check = get_available_letters(letters_guessed)
      while True:
        letter = str(input("Guess a letter: "))
        if letter == "*":
          show_possible_matches(get_guessed_word(secret_word, letters_list))
          continue
        if letter.isalpha() == False or len(letter) != 1:
          warnings_rem -= 1
          print(f"Invalid input, you'll pay for your mistake: you have {warnings_rem} warning(s) left")
          if warnings_rem == 0:
            break
          continue
        elif letter not in letter_check:
          print("You've already guessed this letter")
          continue
        else:
          letters_guessed.append(letter)
          break
      if letter in str(secret_word):
        letters_list.append(letter)
        print(f"Well played, you're right! {get_guessed_word(secret_word, letters_list)}")
      else:
        print(f"You're wrong( {get_guessed_word(secret_word, letters_list)}")
        if letter in "aeoui":
          guesses_rem -= 2
        elif letter in "bcdfghjklmnpqrstvwxyz":
          guesses_rem -= 1
      print("________________________")
      if is_word_guessed(secret_word, get_guessed_word(secret_word, letters_list)) == True:
        break
      if warnings_rem == 0:
        break

    
    if is_word_guessed(secret_word, get_guessed_word(secret_word, letters_list)) == True:
      print(f"Congrats, you won! Your score: {guesses_rem * len(set(secret_word))}")
    else:
      print(f"You lost, but nice try anyway, secret word was: {secret_word}")



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    #secret_word = "vigil"
    hangman_with_hints(secret_word)