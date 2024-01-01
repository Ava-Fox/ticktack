# Let player one choose x or o

options = ['X', 'O']
message = "Player 1, choose X or O"

while True:
    choice = input(f"{message}: ").upper()
    if choice in options:
        break

print(f"You chose {choice}")