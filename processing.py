"""
Checks if the move was a normal move, capture (x), check (+),
mate (#) or castling (O-O or O-O-O)
returning a value and removing the corresponding symbol
"""
def parse_special_move(n_mov, move, pow):
    char_remove = ''
    char_replace = ''
    value = 1
    if "x" in move:
        char_remove = "x"
        if n_mov % 2 == 0:
            # white piece movement
            #TODO
            source_row = -1  # pawn
        else:
            # black piece movement
            #TODO
            source_row = 1  # pawn
        char_replace = str(int(move[-1])+source_row)
        value = 2
    elif "+" in move:
        char_remove = "+"
        value = 3
    elif "#" in move:
        char_remove = "#"
        value = 4
    elif "O-O-O" in move:
        char_remove = "O-O-O"
        value = 5
    elif "O-O" in move:
        char_remove = "O-O"
        value = 5
    move = move.replace(char_remove, char_replace)
    return move, value*pow

"""
Checks which player has played
"""
def check_color(n_mov, pow):
    if n_mov % 2 == 0:
        # white piece movement
        return 1*pow
    # black piece movement
    return 2*pow

"""
Checks which piece has been moved
"""
def parse_piece(move, pow):
    piece = move[0]
    values = {"N": 2, "B": 3, "R": 4, "Q": 5, "K": 6}
    if piece.islower():
        # is a pawn
        value = 1
    else:
        value = values[piece]
    return value*pow

"""
Checks the column
"""
def parse_column(move, pow):
    pos = move[0]
    values = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
    value = values[pos]
    return value*pow


"""
Returns chess movements in a numerical notation
following   
    color|piece |movement|sourceCol|sourceRow|targetCol|targetRow       
    {1,2}|{1,,6}|{1,,4}  |{0,,8}   |{0,,8}   |{1,,8}   |{1,,8}
structure and values, removing one character after each checkup
ONLY the capture movements indicate their source.
"""
def parse_movements(game):
    movements = []
    for n_mov in range(0, len(game)):
        mov = game[n_mov]
        mov, code = parse_special_move(n_mov, mov, 10000)
        if len(mov) != 0: # castling
            code += parse_piece(mov, 100000)
            if code//100000 != 1:
                # is not a pawn
                mov = mov[1:]
            pow = 10 ** (len(mov)-1)
            while len(mov) > 0:
                pow = 10 ** (len(mov)-1)
                code += parse_column(mov, pow)
                mov = mov[1:]
                code += int(mov[0]) * pow//10
                mov = mov[1:]

            code += check_color(n_mov, 1000000)
            movements.append(code)
    return movements
