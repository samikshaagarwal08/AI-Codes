import random

def hangman():
    words = ['python', 'programming', 'hangman', 'developer', 'function', 'variable']
    stages = [
        '''
           -----
           |   |
           |   O
           |  /|\\
           |  / \\
           |
        ''', '''
           -----
           |   |
           |   O
           |  /|\\
           |  / 
           |
        ''', '''
           -----
           |   |
           |   O
           |  /|\\
           |  
           |
        ''', '''
           -----
           |   |
           |   O
           |  /|
           |  
           |
        ''', '''
           -----
           |   |
           |   O
           |   |
           |   
           |
        ''', '''
           -----
           |   |
           |   O
           |   
           |   
           |
        ''', '''
           -----
           |   |
           |   
           |   
           |   
           |
        '''
    ]
    
    word = random.choice(words)
    guessed = set()
    tries = 6

    print("Let's play Hangman!")

    while tries >= 0:
        display = [c if c in guessed else '_' for c in word]
        print(' '.join(display))
        print(stages[tries])

        if '_' not in display:
            print("You won! 🎉 Word was:", word)
            break

        guess = input("Guess a letter: ").lower()
        if guess in guessed or not guess.isalpha() or len(guess) != 1:
            print("Invalid guess. Try again.")
            continue

        guessed.add(guess)
        if guess not in word:
            tries -= 1
            if tries < 0:
                print("You lost! ❌ Word was:", word)
                break

if __name__ == "__main__":
    hangman()
