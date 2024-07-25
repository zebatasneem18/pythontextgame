import time
import random

# Function to simulate typing effect
def print_slow(str):
    for letter in str:
        print(letter, end='', flush=True)
        time.sleep(0.03)
    print()

# Function to handle player's choice
def get_choice(options):
    while True:
        choice = input("Enter your choice: ").strip().lower()
        if choice in options:
            return choice
        else:
            print("Invalid choice. Please try again.")

# Introduction to the game
def intro():
    print_slow("Welcome to the Text Adventure Game!")
    print_slow("You find yourself in a mysterious forest.")
    print_slow("Your goal is to find the hidden treasure.")
    print_slow("You can move: north, south, east, or west.")
    print_slow("Be careful! Danger awaits at every turn.")
    print()

# Function to simulate exploring the forest
def explore_forest():
    print_slow("You start exploring the forest.")
    print_slow("You encounter a fork in the path.")
    print_slow("To the north, you see a dark cave.")
    print_slow("To the east, there is an old hut.")
    print_slow("To the west, a river blocks your path.")
    print_slow("Which way do you want to go? (north/south/east/west)")

    direction = get_choice(['north', 'south', 'east', 'west'])

    if direction == 'north':
        explore_cave()
    elif direction == 'east':
        explore_hut()
    elif direction == 'west':
        print_slow("You cannot cross the river without a boat.")
        print_slow("You decide to turn back and explore another path.")
        explore_forest()
    else:
        print_slow("You head south back to where you started.")
        print_slow("You continue your journey.")
        explore_forest()

# Function to simulate exploring the cave
def explore_cave():
    print_slow("You enter the dark cave.")
    print_slow("Inside, you find a sleeping dragon!")
    print_slow("What will you do? (attack/sneak/run)")

    action = get_choice(['attack', 'sneak', 'run'])

    if action == 'attack':
        print_slow("You attempt to attack the dragon.")
        print_slow("The dragon wakes up and breathes fire at you!")
        print_slow("You have been burnt to ashes. Game Over.")
        game_over()
    elif action == 'sneak':
        print_slow("You try to sneak past the dragon.")
        print_slow("You manage to sneak past without waking it.")
        print_slow("You find a chest of treasure!")
        print_slow("Congratulations! You found the hidden treasure.")
        game_over()
    else:
        print_slow("You run out of the cave in fear.")
        explore_forest()

# Function to simulate exploring the hut
def explore_hut():
    print_slow("You enter the old hut.")
    print_slow("Inside, you find a wise old wizard.")
    print_slow("The wizard offers you a magic potion.")
    print_slow("Do you drink it? (yes/no)")

    choice = get_choice(['yes', 'no'])

    if choice == 'yes':
        print_slow("You drink the magic potion.")
        print_slow("You feel a surge of energy!")
        print_slow("The wizard smiles and wishes you luck on your journey.")
        explore_forest()
    else:
        print_slow("You decide not to drink the potion.")
        print_slow("The wizard nods and lets you leave the hut.")
        print_slow("You continue your journey.")
        explore_forest()

# Function to handle game over scenario
def game_over():
    print_slow("Would you like to play again? (yes/no)")

    choice = get_choice(['yes', 'no'])

    if choice == 'yes':
        print_slow("Restarting the game...")
        time.sleep(1)
        play_game()
    else:
        print_slow("Thank you for playing!")

# Main function to start the game
def play_game():
    intro()
    explore_forest()

# Start the game
if __name__ == "__main__":
    play_game()
