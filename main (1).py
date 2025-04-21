import random
from tkinter import Tk

while True:
    player = input(
        "Your Move, (rock, paper, scissors), or Quit: ").lower().strip()
    if player == "quit":
        print("Exit game, thanks for playing")
        break

    if player != "rock" and player != "paper" and player != "scissors":
        print("input something else dude wtf")
        continue

    options = ("rock", "paper", "scissors")
    computer = random.choice(options)

    print(f"player: {player}")
    print(f"computer: {computer}")

    if player == computer:
        print("Tie!")
    elif player == "scissors" and computer == "paper":
        print("Win!")
    elif player == "paper" and computer == "rock":
        print("Win!")
    elif player == "rock" and computer == "scissors":
        print("Win!")
    else:
        print("LOSER! Get good. Try again?")
