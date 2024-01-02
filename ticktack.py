from helpers import grid, generate_grid

# Let player one choose X or O
options = ['X', 'O']
message = "Player 1, choose X or O"
game_active = False
player_1 = {
    'mark': "",
    'turn': True,
    'winner': False,
    'moves': []
}
player_2 = {
    'mark': "",
    'turn': False,
    'winner': False,
    'moves': []
}

while True:
    choice = input(f"{message}: ").upper()
    if choice in options:
        break

# Define players
player_1['mark'] = choice
for option in options:
    if option != choice:
        player_2['mark'] = option
        break

print(f"Player 1: {player_1} \nPlayer 2: {player_2}")
game_active = True

# Start Game
grid['a1'] = player_1['mark']

def determine_winner():
    """ Determine if a player has three in a row """
    winning_combinations = [
        # Vertical
        ['a1', 'a2', 'a3'],
        ['b1', 'b2', 'b3'],
        ['c1', 'c2', 'c3'],
        # Horizontal
        ['a1', 'b1', 'c1'],
        ['a2', 'b2', 'c2'],
        ['a3', 'b3', 'c3'],
        # Diagonal
        ['a1', 'b2', 'c3'],
        ['c1', 'b2', 'a3']
    ]
    # List of players moves and see if they have any of these lists
    pass

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