import random
# List of words for the game
words = ['python', 'developer', 'hangman', 'challenge', 'keyboard', 'notebook']
# Choose a random word from the list
word = random.choice(words)
word_letters = set(word)
guessed_letters = set()
tries = 6
print("🎮 Welcome to Hangman!")
print("_ " * len(word))
# Main game loop
while len(word_letters) > 0 and tries > 0:
    print("\nYou have", tries, "tries left")
    print("Guessed letters:", " ".join(sorted(guessed_letters)))
    # Show the current state of the word
    display_word = [letter if letter in guessed_letters else '_' for letter in word]
    print("Word: ", " ".join(display_word))
    # Get user input
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print("❗ You already guessed that letter.")
    elif guess in word_letters:
        guessed_letters.add(guess)
        word_letters.remove(guess)
        print("✅ Correct!")
    else:
        guessed_letters.add(guess)
        tries -= 1
        print("❌ Wrong guess.")
# Game over
if tries == 0:
    print("\n💀 Game over! The word was:", word)
else:
    print("\n🎉 Congratulations! You guessed the word:", word)
