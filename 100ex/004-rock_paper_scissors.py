import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


options = [rock, paper, scissors]

player = int(input("Choose option 1-rock, 2-paper and 3-scissors ")) -1

if player > 2 or player < 0:
    print("your a bitch thats not what I ask for")


else:
    # opt = len(options) -1
    cpu = random.randint(0, len(options) - 1)

    #Player chooses Rock
    if player == 0 and cpu == 0:
        print(f"player:\n{rock}\n\ncpu:\n{rock}\n\n Draw")
    if player == 0 and cpu == 1:
        print(f"player:\n{rock}\n\ncpu:\n{paper}\n\n CPU wins")
    if player == 0 and cpu == 2:
        print(f"player:\n{rock}\n\ncpu:\n{scissors}\n\n Player wins")

    #Player chooses Paper
    if player == 1 and cpu == 0:
        print(f"player:\n{paper}\n\ncpu:\n{rock}\n\n Payer wins")
    if player == 1 and cpu == 1:
        print(f"player:\n{paper}\n\ncpu:\n{paper}\n\n Draw")
    if player == 1 and cpu == 2:
        print(f"player:\n{paper}\n\ncpu:\n{scissors}\n\n CPU wins")

    #Player chooses scissors
    if player == 2 and cpu == 0:
        print(f"player:\n{scissors}\n\ncpu:\n{rock}\n\n CPU wins")
    if player == 2 and cpu == 1:
        print(f"player:\n{scissors}\n\ncpu:\n{paper}\n\n Player wins")
    if player == 2 and cpu == 2:
        print(f"player:\n{scissors}\n\ncpu:\n{scissors}\n\n Draw")
