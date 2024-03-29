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
        ['a3', 'b2', 'c1'],
    ]

def generate_grid():
    """ Generate grid with logged moves """
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