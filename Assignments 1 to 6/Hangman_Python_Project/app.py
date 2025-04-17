import random

# List of words for the game
word_list = ["python", "developer", "programming", "hangman", "challenge", "learning"]

def choose_word():
    return random.choice(word_list).lower()

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def play_hangman():
    word = choose_word()
    guessed_letters = set()
    wrong_guesses = set()
    max_attempts = 6
    
    print("\n🎩 Welcome to Hangman! Try to guess the word. 💀")
    
    while len(wrong_guesses) < max_attempts:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"❌ Wrong guesses: {', '.join(wrong_guesses) if wrong_guesses else 'None'}")
        print(f"❤️ Lives left: {max_attempts - len(wrong_guesses)}")
        
        guess = input("🔤 Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Please enter a single valid letter.")
            continue
        
        if guess in guessed_letters or guess in wrong_guesses:
            print("⏳ You already guessed that letter. Try another!")
            continue
        
        if guess in word:
            guessed_letters.add(guess)
            print("✅ Good guess!")
        else:
            wrong_guesses.add(guess)
            print("❌ Wrong guess!")
        
        if all(letter in guessed_letters for letter in word):
            print(f"\n🎉 Congrats! You guessed the word: {word} 🏆")
            return
    
    print(f"\n💀 Game Over! The word was: {word}. Better luck next time!")

# Run the game
play_hangman()