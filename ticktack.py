# Let player one choose X or O
options = ['X', 'O']
message = "Player 1, choose X or O"

while True:
    choice = input(f"{message}: ").upper()
    if choice in options:
        break

# Define players
player_1 = choice
for option in options:
    if option != choice:
        player_2 = option

print(f"Player 1: {player_1} \n Player 2: {player_2}")