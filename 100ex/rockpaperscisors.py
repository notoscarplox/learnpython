import random
print("Rock, Paper, Scissors")
# pc_choice = random.randint(1, 3)
wins = 0
ties = 0
loses = 0

while True:
    ran_choice = random.randint(1, 3)
    if ran_choice == 1:
        pc_choice = "r"
    elif ran_choice == 2:
        pc_choice = "p"
    else:
        pc_choice = "s"

    player_choice = input("Enter your move, r, p, s, q=quit"\n)
    if player_choice == "q":
        break

    if pc_choice == "r":
        if player_choice == "r":
            ties += 1
            print("You tied")
        elif player_choice == "p":
            wins += 1
            print("You win")
        else:
            loses += 1
            print("You lose")

    elif pc_choice == "p":
        if player_choice == "p":
            ties += 1
            print("You tied")
        elif player_choice == "s":
            wins += 1
            print("You win")
        else:
            loses += 1
            print("You lose")

    else:
        if player_choice == "s":
            ties += 1
            print("You tied")
        elif player_choice == "r":
            wins += 1
            print("You win")
        else:
            loses += 1
            print("You lose")

    print(f"Wins: {wins}, Ties: {ties}, Loses: {loses}")