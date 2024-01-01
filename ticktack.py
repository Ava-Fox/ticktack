from helpers import grid, generate_grid

# Let player one choose X or O
options = ['X', 'O']
message = "Player 1, choose X or O"
game_active = False

while True:
    choice = input(f"{message}: ").upper()
    if choice in options:
        break

# Define players
player_1 = choice
for option in options:
    if option != choice:
        player_2 = option
        break

print(f"Player 1: {player_1} \nPlayer 2: {player_2}")
game_active = True

# Start Game
generate_grid()
while game_active:
    # First, determine if there's already a winner (determine_winner function)
        # If so, print the winner and exit game 
    # Determine who's turn it is, then prompt them to make move
    # Check to make sure player choice is in available grid options, if not reprompt
        # if move in grid.keys():
            # grid[move] = player
    # Switch who's turn it is and generate updated grid
    break