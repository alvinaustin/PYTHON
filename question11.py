# Initial number of sticks
sticks = 16  # You can change this number if you want

print("Welcome to the Sticks Game!")
print("There are", sticks, "sticks.")
print("Each player can remove 1, 2, or 3 sticks on their turn.")
print("The player who removes the last stick wins!")

# Start the game loop
while sticks > 0:
    # Player 1's turn
    print("\nThere are", sticks, "sticks left.")
    move = int(input("Player 1, how many sticks do you want to remove (1, 2, or 3)? "))
    
    # Check if the move is valid (1, 2, or 3 sticks, and not more than the remaining sticks)
    if move in [1, 2, 3] and move <= sticks:
        sticks -= move
    else:
        print("Invalid move. Please choose 1, 2, or 3 sticks, and not more than the remaining sticks.")
        continue

    if sticks == 0:
        print("Player 1 wins! All sticks have been removed.")
        break

    # Player 2's turn
    print("\nThere are", sticks, "sticks left.")
    move = int(input("Player 2, how many sticks do you want to remove (1, 2, or 3)? "))
    
    # Check if the move is valid (1, 2, or 3 sticks, and not more than the remaining sticks)
    if move in [1, 2, 3] and move <= sticks:
        sticks -= move
    else:
        print("Invalid move. Please choose 1, 2, or 3 sticks, and not more than the remaining sticks.")
        continue

    if sticks == 0:
        print("Player 2 wins! All sticks have been removed.")
        break
