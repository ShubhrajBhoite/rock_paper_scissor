import random

# Define choices and emojis
emojis = {"r": "🪨", "p": "📃", "s": "✂️"}
choices = ("r", "p", "s")  # Ordered as rock, paper, scissors
wins, losses, ties = 0, 0, 0  # Score tracking

while True:
    # Get user input
    user_choice = input("Enter r (rock), p (paper), s (scissors), or q to quit: ").lower().strip()
    
    # Check for quit
    if user_choice == "q":
        print(f"\nGame over! Score: Wins = {wins}, Losses = {losses}, Ties = {ties} 🏆")
        break
    
    # Validate user input
    if user_choice not in choices:
        print("Invalid choice! Please enter 'r', 'p', or 's'.")
        continue
    
    # Computer makes a random choice
    computer_choice = random.choice(choices)
    
    # Print choices
    print(f"Your choice: {emojis[user_choice]}")
    print(f"Computer choice: {emojis[computer_choice]}")
    
    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie! 😐")
        ties += 1
    elif (user_choice, computer_choice) in [("r", "s"), ("p", "r"), ("s", "p")]:
        print(f"You win! {emojis[user_choice]} beats {emojis[computer_choice]} 🎉")
        wins += 1
    else:
        print(f"You lose! {emojis[computer_choice]} beats {emojis[user_choice]} 😢")
        losses += 1
    
    # Ask to continue
    while True:
        should_continue = input("Continue? (y/n): ").lower().strip()
        if should_continue in ("y", "n"):
            break
        print("Invalid input! Please enter 'y' or 'n'.")
    
    if should_continue == "n":
        print(f"\nGame over! Score: Wins = {wins}, Losses = {losses}, Ties = {ties} 🏆")
        break
     