# SLOTH-MACHINE
#This is my first Git repository.
#Author = Himanshu Arodia.
import random
score = 0

def spin_sloth():
    symbols = ["🍒", "🍋", "⭐"]
    
    # Generate random symbols
    sloth1 = symbols[random.randrange(len(symbols))]
    sloth2 = symbols[random.randrange(len(symbols))]
    sloth3 = symbols[random.randrange(len(symbols))]
    
    print(f"{sloth1} {sloth2} {sloth3}")
    return sloth1, sloth2, sloth3

print("Welcome to the 'SLOTH MACHINE'")
yes_no = input("Do you want to spin the sloth machine? (YES/NO): ").strip().lower()

if yes_no == "yes" or yes_no == "y":
    while True:
        # Spin the slot machine and get the results
        sloth1, sloth2, sloth3 = spin_sloth()
        
        # Check for winning combinations
        if sloth1 == sloth2 == sloth3:
            print("Jackpot! You win!")
            score += 1
            print(f"Your score is {score}!")
        else:
            print("Better luck next time!")
        
        # Ask the player if they want to play again
        play_again = input("Do you want to play again? (YES/NO): ").strip().lower()
        if play_again != "yes" and play_again != "y":
            print("Thanks for playing!")
            break
elif yes_no == "no" or yes_no == "n":
    print("Let's try again!")
else:
    print("Invalid input. Please enter 'YES' or 'NO'.")

