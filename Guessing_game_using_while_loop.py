# Guessing game
secret_num = 5
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count = guess_count + 1
    if guess == secret_num:
        print("You Won!")
        break
else:
    print("You have failed!")