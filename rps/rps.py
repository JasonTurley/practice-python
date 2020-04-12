"""
Simple command line rock-paper-scissors game.
"""

import random
import time

def display_menu():
    print("Welcome to my simple command line rock-paper-scissors game!")
    print("")
    print("Chose option:")
    print("- Rock")
    print("- Paper")
    print("- Scissors")
    print("")


def get_player_option():
    p = input("> ")

    p = p.lower()

    if p != "rock" and p != "paper" and p != "scissors":
        print("{} not a valid option.".format(p))
        exit()

    return p


def get_computer_option():
    options = ["rock", "paper", "scissors"]
    num = random.randint(0, len(options) - 1)

    return options[num]

def display_results():
    print("")

    # This will not print unless we flush stdout
    print("Calculating", end="", flush=True)

    for i in range(4):
        time.sleep(1)
        print(".", end="", flush=True)

    time.sleep(1)
    print("\nResults:")

def battle(player, computer):
    # TODO: find cleaner way to write this function
    display_results()

    if player == computer:
        print("Tie!")

    elif player == "rock":
        if computer == "scissors":
            print("You win!")
        else:
            print("You lose!")

    elif player == "paper":
        if computer == "rock":
            print("You win!")
        else:
            print("You lose!")

    elif player == "scissors":
        if computer == "paper":
            print("You win!")
        else:
            print("You lose!")

    # You can add more options here

def game_loop():
    display_menu()

    player = get_player_option()
    computer = get_computer_option()

    battle(player, computer)

if __name__ == "__main__":
    game_loop()
