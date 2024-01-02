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
}
player_2 = {
    'mark': "",
    'moves': [],
    'name': "Player 2",
    'turn': False,
}
players = [player_1, player_2]
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

print(f"Player 1: {player_1['mark']} \nPlayer 2: {player_2['mark']}")
game_active = True

def change_turns():
    """Change whose turn it is  """
    for player in players:
        if player['turn'] == True:
            player['turn'] = False
        else:
            player['turn'] = True

def determine_winner():
    """ Determine if a player has three in a row """
     # List of players moves and see if they have any of these lists
    # Return player_1, player_2, or None
    for player in players:
        moves = player['moves']
        if moves:
            moves.sort()
            if moves in winning_combinations:
                player['winner'] = True
                return player['name']
    return None

def determine_tie():
    """If grid all filled and no winner, it's a tie"""
    for thing in grid.values():
        if thing == " ":
            return False
    # Return True if tie, False if not
    return True

# Start Game
generate_grid()
while game_active:
    # First, determine if there's already a winner or tie
        # If so, print the winner and exit game
    results = determine_winner()
    if results: 
        print(f"{results} wins!") 
        game_active = False
        break
    
    tie = determine_tie()
    if tie:
        print("It's a tie!")
        game_active = False
        break

    # Determine who's turn it is, then prompt them to make move
    for player in players:
        if player['turn'] == True:
            turn = player

    # Check to make sure player choice is in available grid options, if not reprompt
    move = input(f"{turn['name']}: ").lower()
    while True:
        if move in grid.keys() and grid[move] == " ":
            grid[move] = turn['mark']
            turn['moves'].append(move)
            break
        else:
            print("Please enter valid move")
            move = input(f"{turn['name']}: ").lower()
            
    # Switch who's turn it is and generate updated grid    
    change_turns()
    generate_grid()       

print(player_1, "\n", player_2)
# play_again = input("Game Over! Play again? Y/N : ").title()
# if play_again == 'Y':
    # Clear user data and generate new grid
#     continue
# else:
#     print("Goodbye!")
#     game_active = False