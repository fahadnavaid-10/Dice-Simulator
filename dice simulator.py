from random import randint
import time

def make_dice(num):
    patterns = {
        1: '''
           -------
          |       |
          |   •   |
          |       |
           -------  
        ''',
        2: '''
           -------
          | •     |
          |       |
          |     • |
           -------  
        ''',
        3: '''
           -------
          | •     |
          |   •   |
          |     • |
           -------  
        ''',
        4: '''
           -------
          | •   • |
          |       |
          | •   • |
           -------  
        ''',
        5: '''
           -------
          | •   • |
          |   •   |
          | •   • |
           -------  
        ''',
        6: '''
           -------
          | •   • |
          | •   • |
          | •   • |
           -------  
        '''
    }
    print(patterns[num])

print("Welcome to the Dice Roller!")
print("Press 'C' to roll the dice or 'E' to exit.")

while True:
    user_input = input('Command [C,E]: ').lower()
    if user_input == 'e':
        print("Thank you for using the Dice Roller. Goodbye!")
        break
    elif user_input == 'c':
        random_number = randint(1, 6)
        print("Rolling the dice...")
        time.sleep(1)  # Pause for 2 seconds
        make_dice(random_number)
    else:
        print("Invalid input. Please press 'C' to roll the dice or 'E' to exit.")
