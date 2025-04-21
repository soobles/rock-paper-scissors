import random

options = ("rock", "paper", "scissors")
computer = random.choice(options)

player = input("Your Move, (rock, paper, scissors): ").lower()

print(f"Player: {player}")
print(f"Computer: {computer}")

if player != ("rock", "paper", "scissors")
    print ("Try again")

if player == computer:
    print("Tie!")
elif player == "scissors" and computer == "paper":
    print("Win!")
elif player == "paper" and computer == "rock":
    print("Win!")
elif player == "rock" and computer == "scissors":
    print("Win!")
else: 
    print("LOSER! Get good.")