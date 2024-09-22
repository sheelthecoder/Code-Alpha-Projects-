import random

#Providing the words list from where random word will be taken
def select_random_word():
    word_list= ['Python','Java','Data','Code','Development','Algorithm',
                'Function','Structure','Programming','Compilier','Assembler','Syntax',
                'Object','Class','Variable','Debug','bug','Application']
    return random.choice(word_list)


#Display the guessed letter 
def display_word(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)


#Main game
def hangman():
    word = select_random_word().lower()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    guessed_word = display_word(word, guessed_letters)

    print("Welcome to Hangman Game!")
    print("All words are related to programing!")
    print(f"Your word: {guessed_word}")

    while incorrect_guesses < max_incorrect_guesses:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! The letter '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Wrong guess! The letter '{guess}' is not in the word.")
            print(f"You have {max_incorrect_guesses - incorrect_guesses} guesses left.")

        guessed_word = display_word(word, guessed_letters)
        print(f"Current word: {guessed_word}")

        if '_' not in guessed_word:
            print("Congratulations! You've guessed the word!")
            break
    else:
        print(f"Game over! The word was '{word}'.")

if __name__ == "__main__":
    hangman()
        
