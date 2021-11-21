
secret_word = "wolf"
guess = input("Guess the secret word: ").lower()
guess_count = 1
guess_limit = 3

while guess != secret_word and guess_count < guess_limit:
    print("Try again. Guesses left:" , guess_limit - guess_count)
    guess_count += 1
    guess = input("Please guess the secret word again: ").lower()

if guess_count == guess_limit and guess != secret_word:
    print("You have run out of guesses, game over.")
else:
    print("Well done! You guessed correctly!")
