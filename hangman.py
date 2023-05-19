import os
import random

os.system('cls')


def hangman():
    words_list = ['programming', 'javascript', 'frontend', 'backend', 'python',
                  'framework', 'devops', 'developer']
    solution = list(random.choice(words_list))
    user = list('*' * len(solution))
    letters_used = []
    letters_guessed = []
    hang = 0

    def score():
        os.system('cls')
        if hang < 5:
            print('Guess: {}\n'.format("".join(user)))
        print('Letters guessed: {}\n'.format(letters_guessed))
        print('Letters missed: {}\n'.format(letters_used))
        print('Attempts left: {}'.format(5 - hang))

    while user != solution and user != 'lost':

        letter = input('\nEnter a letter: ')

        if len(letter.lower()) is not 1 or not letter.lower().isalpha():
            score()
            print('\nInvalid input, type only one character!')
        elif letter.lower() in letters_used:
            score()
            print('\nLetter already used!')
        elif letter.lower() in letters_guessed:
            score()
            print('\nLetter already guessed!')
        elif letter.lower() in solution:
            for index, value in enumerate(solution):
                if letter.lower() == value:
                    user[index] = value
            letters_guessed.append(letter.lower())
            score()
        else:
            hang += 1
            letters_used.append(letter.lower())
            score()

        if hang == 5:
            user = solution
            print('\nSolution was: {}\n'.format("".join(solution)))
            print('You lost :( Play again?')
        elif user == solution:
            print('\nCongrats, you won! Play again?')
            

game = True
while game:
    choice = input('\nType "play" to start or "quit" to exit\n\n> ')
    if choice == 'play':
        os.system('cls')
        hangman()
    elif choice == 'quit':
        os.system('cls')
        print('\nBye')
        game = False
    elif not choice or ' ' in choice:
        os.system('cls')
        print('\nEnter a command.')
    else:
        os.system('cls')
        print('\nCommand "{}" unrecognizable, try again'.format(choice))
