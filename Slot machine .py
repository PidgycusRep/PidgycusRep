import random
import time

# List of slot symbols
symbols = ["🍒", "🍋", "🍊", "🍉", "⭐", "🍀"]

# Function to spin the slot machine
def spin():
    # Randomly pick three symbols from the list
    return random.choices(symbols, k=3)

# Function to check for a win
def check_win(spin_result):
    if spin_result[0] == spin_result[1] == spin_result[2]:
        return True
    return False

# Main game loop
def slot_machine():
    print("Welcome to the Slot Machine!")
    balance = 999  # Starting balance
    while balance > 0:
        print(f"Your current balance: ${balance}")
        input("Press Enter to spin the slot machine...")

        # Deduct a small amount per spin
        balance -= 10
        print("Spinning...\n")
        time.sleep(1)  # Pause for dramatic effect

        spin_result = spin()
        print(" | ".join(spin_result))

        if check_win(spin_result):
            print("Congratulations! You won!")
            balance += 50  # Reward for winning
        else:
            print("Sorry, you lost this round.")

        if balance <= 0:
            print("You've run out of money! Game over.")
            break

# Run the game
slot_machine()
