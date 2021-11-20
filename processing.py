"""
Checks which player has played
Arguments:
- n_mov: turn in which the move was played
- pow: position in final code representing which color has played
"""
def check_color(n_mov, pow):
    if n_mov % 2 == 0:
        # white piece movement
        return 1*10**pow
    # black piece movement
    return 2*10**pow


"""
Checks if the move was a normal move, capture (x), check (+),
mate (#) or castling (O-O or O-O-O)
returning a value and removing the corresponding symbol
Arguments:
- n_mov: turn in which the move was played
- move: current move
- pow: position in final code representing the existing special move
"""
def parse_special_move(n_mov, move, pow):
    char_remove = ''
    char_replace = ''
    value = 1
    if "x" in move:
        char_remove = "x"
        if check_color(n_mov, 0) == 1:
            # white piece movement
            # TODO
            source_row = -1  # pawn
        else:
            # black piece movement
            # TODO
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
    return move, value*10**pow


"""
Checks which piece has been moved
Arguments:
- piece: current piece represented by a letter (except for the pawn)
- pow: position in final code representing the moved piece
"""
def parse_piece(piece, pow):
    values = {"N": 2, "B": 3, "R": 4, "Q": 5, "K": 6}
    if piece.islower():
        # is a pawn
        value = 1
    else:
        value = values[piece]
    return value*10**pow


"""
Checks the column
Arguments:
- pos: current column represented by a letter
- pow: position in final code representing the queried column
"""
def parse_column(pos, pow):
    values = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
    value = values[pos]
    return value*10**pow


"""
Returns chess movements in a numerical notation
following   
    color|piece |movement|sourceCol|sourceRow|targetCol|targetRow       
    {1,2}|{1,,6}|{1,,4}  |{0,,8}   |{0,,8}   |{1,,8}   |{1,,8}
structure and values, removing one character after each checkup
ONLY the capture movements indicate their source.
Arguments:
- game: list of moves in string format
"""
def parse_movements(game):
    movements = []
    for n_mov in range(0, len(game)):
        mov = game[n_mov]
        mov, code = parse_special_move(n_mov, mov, 4)
        if len(mov) != 0:  # castling
            code += parse_piece(mov[0], 5)
            if code//(10**5) != 1:
                # is not a pawn
                mov = mov[1:]
            while len(mov) > 0:
                pow = len(mov)-1
                code += parse_column(mov[0], pow)
                mov = mov[1:]
                code += int(mov[0]) * 10**(pow-1)
                mov = mov[1:]

            code += check_color(n_mov, 6)
            movements.append(code)
    return movements
