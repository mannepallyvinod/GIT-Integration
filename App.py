command = ''
Started = False
Stopped = True
while True:
    command = input('> ').lower()
    if command == 'start':
        if Started:
            print('Car is already started ')
        else:
            Started = True
            print('Car started')
    elif command == 'stop':
        if not Started:
            print('Car is already stopped')
        else:
            Started = False
            print('Car stopped')
    elif command == 'help':
        print('''
Start - To start the car
Stop - To stop the car
Quit - To quit
        ''')
    elif command == 'quit':
        break
    else:
        print("Sorry I don't understand")
