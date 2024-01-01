# Let player one choose X or O
options = ['X', 'O']
message = "Player 1, choose X or O"
grid = """
     a   b   c
       |   |   
1   ___|___|___
       |   |
2   ___|___|___
       |   |
3      |   |
"""

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

grid = {
    'a1': " ",
    'a2': " ",
    'a3': " ",
    'b1': " ",
    'b2': " ",
    'b3': " ",
    'c1': " ",
    'c2': " ",
    'c3': " "
}

def generate_grid():
    """ function to generate grid each time w/ logged markings?? """
    table = f"""
         a   b   c
         {grid['a1']} | {grid['b1']} | {grid['c1']} 
    1   ___|___|___
         {grid['a2']} | {grid['b2']} | {grid['c2']}
    2   ___|___|___
         {grid['a3']} | {grid['b3']} | {grid['c3']}
    3      |   |
    """
    print(table)

grid['b1'] = player_1
grid['c3'] = player_2

generate_grid()