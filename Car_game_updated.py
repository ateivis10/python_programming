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
