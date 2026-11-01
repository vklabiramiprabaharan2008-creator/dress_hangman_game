import random

# Simple Hangman Game - 1st Year Level
print("--- Hangman Game ---")
print("Guess the dress name!")

# list of words - string
words = ["saree", "kurti", "dress", "lehenga", "salwar"]

# random word pick
secret = random.choice(words)

# empty guess
guess_word = ""
for i in secret:
    guess_word = guess_word + "_"

print("Word:", guess_word)
print("Length:", len(secret))

# chances
chances = 6
guessed_letters = ""

while chances > 0:
    print("\nChances left:", chances)
    letter = input("Enter a letter: ")
    letter = letter.lower()  # string function
    
    if len(letter) != 1:
        print("Only 1 letter!")
        continue
    
    if letter in guessed_letters:
        print("Already guessed")
        continue
    
    guessed_letters = guessed_letters + letter
    
    if letter in secret:
        print("Correct!")
        # update the word
        new_word = ""
        for i in range(len(secret)):
            if secret[i] == letter:
                new_word = new_word + letter
            else:
                # if already guessed before, keep it
                if guess_word[i] != "_":
                    new_word = new_word + guess_word[i]
                else:
                    new_word = new_word + "_"
        guess_word = new_word
        print("Now:", guess_word)
        
        if "_" not in guess_word:
            print("\nYou WIN! Word is", secret)
            break
    else:
        print("Wrong!")
        chances = chances - 1
        print("Now:", guess_word)

if chances == 0:
    print("\nYou LOSE! Word was", secret)

print("Game Over")
