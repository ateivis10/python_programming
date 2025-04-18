# Car Game
print(" Press help to see Menu")
choice = ""

while choice.upper() != "QUIT":
    choice = input("> ").upper()
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