import random
options = ("rock","paper","scissors")
running = True                             
while running:                    
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Enter a Choices(rock,paper,scissors):")
    print(f"player:{player}")
    print(f"computer:{computer}")
    if player == computer:                                     
        print("It's tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!") 
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("you lost!")
    if not input("play again? (y/n): ").lower() == "y":
        break
print("Thanks for playing")