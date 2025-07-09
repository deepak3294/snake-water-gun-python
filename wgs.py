import random  # Importing the random module to allow the computer to make a random choice

"""
Game Rules:
- snake drinks water → snake wins
- water douses gun → water wins
- gun kills snake → gun wins

Mapping:
- snake = 1
- gun = 0
- water = -1
"""

# Computer randomly selects one of the three options
computer = random.choice([1, 0, -1])

# Prompt the user to enter their choice: 's' for snake, 'w' for water, 'g' for gun
youstr = input("Enter your choice (s for snake, w for water, g for gun): ")

# Dictionary to convert user input into corresponding numeric value
you_dict = {"s": 1, "w": -1, "g": 0}

# Dictionary to convert numeric values back to string for display
reverse_dict = {1: "snake", -1: "water", 0: "gun"}

# Convert the user's input string to its numeric representation
you = you_dict[youstr]

# Display both choices
print(f"Your choice: {reverse_dict[you]}\nComputer's choice: {reverse_dict[computer]}")

# Determine the result of the game
if computer == you:
    print("Match draw")  # Both choices are the same
else:
    # You lose if the computer beats your choice based on the game rules
    if (computer - you == -1) or (computer - you == 2):
        print("You lose")
    else:
        print("You win")  # Otherwise, you win



        