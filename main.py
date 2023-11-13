import random

computer_wins = 0
player_wins = 0

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)

    player = None

    while player not in choices:
        player = input("Choose: rock / paper / scissors: ").lower()
    if player == "rock":
        if computer == "paper":
            computer_wins += 1
            print("computer: "+computer)
            print("player: "+player)
            print("You lose!")
        if computer == "scissors":
            player_wins += 1
            print("computer: " + computer)
            print("player: " + player)
            print("You win!")
        if computer == "rock":
            print("computer: " + computer)
            print("player: " + player)
            print("Draw!")
    elif player == "paper":
        if computer == "paper":
            print("computer: "+computer)
            print("player: "+player)
            print("Draw!")
        if computer == "scissors":
            computer_wins += 1
            print("computer: " + computer)
            print("player: " + player)
            print("You lose!")
        if computer == "rock":
            player_wins += 1
            print("computer: " + computer)
            print("player: " + player)
            print("You win!")
    elif player == "scissors":
        if computer == "paper":
            player_wins += 1
            print("computer: "+computer)
            print("player: "+player)
            print("You win!")
        if computer == "scissors":
            print("computer: " + computer)
            print("player: " + player)
            print("Draw!")
        if computer == "rock":
            computer_wins += 1
            print("computer: " + computer)
            print("player: " + player)
            print("You lose!")

    print("\nScore: Player ["+str(player_wins)+"]  Computer ["+str(computer_wins)+"] ")

    replay = input("\nPlay again? (yes/no): ").lower()

    if replay != "yes":
        break
print("Bye!")
