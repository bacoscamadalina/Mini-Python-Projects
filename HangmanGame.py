'''
                                     - HANGMAN GAME -

Domain of discussion: AVIATION

'''

import random


def choose_word():
    words = ['airplane', 'wing', 'tail', 'seatbelt', 'cockpit', 'pilot', 'engine']
    return random.choice(words)


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display


def hangman_game():
    print('Welcome in Hangman Game!')
    secret_word = choose_word()
    display = "_" * len(secret_word)
    print(f'Secret word: {display}')

    guessed_letters = []
    number_attempts = 5

    while number_attempts > 0:
        guess_letters = input('Guess a letter: ').lower()

        if guess_letters in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess_letters)

        if guess_letters in secret_word:
            for i in range(len(secret_word)):
                if secret_word[i] == guess_letters:
                    display = display[:i] + guess_letters + display[i + 1:]
            print(f'Current word is: {display}')

            if display == secret_word:
                print('Congratulations! You guessed the word.')
                break
        else:
            print("Letter doesn't fit")
            number_attempts -= 1

            if number_attempts == 0:
                print(f'Sorry! You have exhausted all attempts. The correct word was: {secret_word}')
                break


hangman_game()

