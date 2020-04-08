counter = 0
start = "The system is now running..."
started = False
print(start)
while counter >= 0:
    command = input('>')
    if command == "help" or command == "HELP":
        print("start - to start a car")
        print("stop - to stop a car")
        print("quit - to exit")

    elif command == "start" or command == "START":
        if started:
            print("Car is already started")
        else:
            started = True
            print("The car engine is starting...")
        counter += 1
    elif command == "stop" or command == "STOP":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("The car engine is stopped!")
        counter += 1
    elif command == "quit" or command == "QUIT":
        break
    else:
        print("Cannot understand the command. Type again")
        counter += 1


