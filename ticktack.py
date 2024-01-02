from helpers import grid, winning_combinations, generate_grid

# Let player one choose X or O
options = ['X', 'O']
message = "Player 1, choose X or O"
game_active = False
# Player_1 is initialized to start game
player_1 = {
    'mark': "",
    'moves': [],
    'name': "Player 1",
    'turn': True,
    'winner': False,
}
player_2 = {
    'mark': "",
    'moves': ['b1', 'c1', 'a1'],
    'name': "Player 2",
    'turn': False,
    'winner': False,
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
    players = [player_1, player_2]
    for player in players:
        moves = player['moves']
        if moves:
            moves.sort()
            if moves in winning_combinations:
                player['winner'] = True
                return player['name']
            else:
                continue
    # List of players moves and see if they have any of these lists
    # Return player_1, player_2, or None
    return None

def determine_tie():
    """If grid all filled and no winner, it's a tie"""
    # Return True if tie, False if not
    ...

generate_grid()
while game_active:
    # First, determine if there's already a winner (determine_winner function)
        # If so, print the winner and exit game
    results = determine_winner()
    print(results)
    if results: 
        if results  == 'tie':
            print(f"It's a tie!")
        else:
            print(f"{results} wins!") 
    # Determine who's turn it is, then prompt them to make move
    # Check to make sure player choice is in available grid options, if not reprompt
        # if move in grid.keys():
            # grid[move] = player
    # Switch who's turn it is and generate updated grid
    play_again = input("Game Over! Play again? Y/N : ").title()
    if play_again == 'Y':
        continue
    else:
        print("Goodbye!")
        game_active = False

