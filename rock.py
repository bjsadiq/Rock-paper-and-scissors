import random

options = ["r","p","s"]
trial = 3
score = 0
while trial > 0:
    print("""\nselect R for rock, P for paper and S for scissors.""")
    com_choice = random.choice(options)
    player_choice = input(">").lower()
    if player_choice in options:
        if player_choice == options[0] and com_choice ==options[2]:
            print("You win")
            print("Computer choose", com_choice)
            trial+=1
            score+=2
        elif player_choice == options[2] and com_choice== options[1]:
            print("You win")
            print("Computer choose", com_choice)
            trial+=1
            score+=2
        elif player_choice == options[1] and com_choice== options[0]:
            print("You win")
            print("Computer choose", com_choice)
            trial+=1
            score+=2
        elif player_choice == com_choice:
            print("It's a tie")
        else:
            print("You lose")
            print("Computer choose", com_choice.title())
            trial-=1
    else:
        print("Invalid input")
        trial-=1
    print(f"{trial} trial(s) left")
print("Game over")
print("You scored", score)