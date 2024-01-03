from helpers import grid, generate_grid

# Let player one choose X or O
options = ['X', 'O']
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

# Allow player 1 to choose their mark
while True:
    choice = input(f"Player 1, choose X or O: ").upper()
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
    """Change whose turn it is"""
    for player in players:
        if player['turn'] == True:
            player['turn'] = False
        else:
            player['turn'] = True

def check_player_choice(move, turn):
    """Check to make sure player choice in available grid options, if not reprompt"""
    while True:
        if move in grid.keys() and grid[move] == " ":
            grid[move] = turn['mark']
            turn['moves'].append(move)
            break
        else:
            print("Please enter valid move")
            move = input(f"{turn['name']}: ").lower()

def determine_tie():
    """If grid all filled and no winner, it's a tie"""
    for space in grid.values():
        if space == " ":
            return False
    # Return True if tie, False if not
    return True

def determine_turn():
    """Check who's turn it is"""
    for player in players:
        if player['turn'] == True:
            turn = player
            return turn
        
def determine_winner():
    """Determine if a player has three in a row"""
    # Count how many of players move start w/ a/b/c and end w/ 1/2/3
        # If any count = 3, then they have horizontal or vertical win
    for player in players:
        moves = player['moves']
        if moves:
            a, b, c = 0, 0, 0
            o, tw, th = 0, 0, 0
            diagonal_space = []
            diagonal_wins = [['a1', 'b2', 'c3'], ['a3', 'b2', 'c1']]
            for move in moves:
                if move[0] == 'a':
                    a += 1
                elif move[0] == 'b':
                    b += 1
                elif move[0] == 'c':
                    c += 1
                
                if move[1] == '1':
                    o += 1
                elif move[1] == '2':
                    tw += 1
                elif move[1] == '3':
                    th += 1
                
                if move == 'a1' or move == 'a3' or move == 'b2' or move == 'c1' or move == 'c3':
                    diagonal_space.append(move)

            # Determine horizontal win
            if a == 3 or b == 3 or c == 3 or o == 3 or tw == 3 or th == 3:
                return player['name']
            
            # Determine diagonal win
            if diagonal_space:
                diagonal_space.sort()
                for win in diagonal_wins:
                    if win == diagonal_space:
                        return player['name']

    return None

# Start Game
while game_active:
    # Generate updated grid
    generate_grid()

    # Determine if there's already a winner
    winner = determine_winner()
    if winner: 
        print(f"{winner} wins!") 
        break

    # ...Or already a tie
    tie = determine_tie()
    if tie:
        print("It's a tie!")
        break

    # Determine who's turn it is
    turn = determine_turn()

    # Prompt player to make choice, and check if it's a valid one
    move = input(f"{turn['name']}: ").lower()
    check_player_choice(move, turn)

    # Switch who's turn it is    
    change_turns()      