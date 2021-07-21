command = ""
started = False

while True:
    command = input("> ").lower()
    if command == "help":
        print('''
start - to start the car
stop - to stop the car
quit - to quit
        ''')
    elif command == "start":
        if started:
            print("Car already started")
        else:
            started = True
            print("car started ...ready to go")
    elif command == "stop":
        if not started:
            print('Car is already stopped')
        else:
            started = False
            print("car stopped")
    elif command == 'quit':
        print("Car quit")
        break
    else:
        print("Sorry i do not understand")
