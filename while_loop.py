# While loop
i = 1
while i<=5:
    print(i)
    i = i+1
print("Done")

# * Triangle with while
i = 1
while i<=5:
    print('*' * i)
    i = i+1

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

# Car Game
print(" Press help to see Menu")
choice = ""

while choice.upper() != "QUIT":
    choice = input("Enter your choice: ").upper()
    if choice.upper() == "HELP":
        print("""Start - To start the car
Stop - To stop the car
Quit - To quit the game""")
    elif choice == "START":
        print("Car started....")
    elif choice == "STOP":
        print("Car stopped....")
    elif choice == "QUIT":
        print("Quiting the game....")
        break
    else:
        print("Wrong Choice")


# Car Game Updated
print("Press help to see Menu")
started = False
stopped = False
choice = ""

while choice.upper() != "QUIT":
    choice = input("> ").upper()
    if choice == "HELP":
        print("""Start - To start the car
Stop - To stop the car
Quit - To quit the game""")
        choice = input("> ").upper()
    if choice == "START":
        if started:
            print("Car has already started")
        else:
            started = True
            print("Car started....")
    elif choice == "STOP":
        if stopped:
            print("Car has already stopped")
        else:
            stopped = True
            started = False
            print("Car stopped....")
    elif choice == "QUIT":
        print("Quiting the game....")
        break
    else:
        print("Wrong Choice")

