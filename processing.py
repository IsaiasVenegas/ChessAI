def check_color(n_mov, pow):
    """
    Checks which player has played
    Arguments:
    - n_mov: turn in which the move was played
    - pow: position in final code representing which color has played
    """
    if n_mov % 2 == 0:
        # white piece movement
        return 1*10**pow
    # black piece movement
    return 2*10**pow


def parse_special_move(n_mov, move, pow):
    """
    Returns tuple of
    movement without special characters (x, +, #, =, O-O, O-O-O)
    with 
        1 for normal move
        2 for captures
    or  3 for castling (O-O or O-O-O)
    Arguments:
    - n_mov: turn in which the move was played
    - move: current move
    - pow: position in final code representing the existing special move
    """
    char_remove = ''
    char_replace = ''
    value = 1
    if "x" in move:
        source_col = move[move.find("x")-1]
        if(source_col.islower()):
            char_remove = source_col
        char_remove += "x"
        value = 2
        move = move.replace(char_remove, char_replace)
    if "=" in move:
        char_remove = "="
        piece_promo = move[move.find("=")+1]
        char_remove += piece_promo
        move = move.replace(char_remove, char_replace)
    if "+" in move:
        char_remove = "+"
    elif "#" in move:
        char_remove = "#"
    move = move.replace(char_remove, char_replace)
    if "O-O-O" in move:
        char_remove = "O-O-O"
        if(check_color(n_mov, 0) == 1):
            char_replace = "Kc1"
        else:
            char_replace = "Kc8"
        value = 3
    elif "O-O" in move:
        char_remove = "O-O"
        if(check_color(n_mov, 0) == 1):
            char_replace = "Kg1"
        else:
            char_replace = "Kg8"
        value = 3
    move = move.replace(char_remove, char_replace)
    return move, value*10**pow


def parse_piece(piece, pow):
    """
    Checks which piece has been moved
    Arguments:
    - piece: current piece represented by a letter (except for the pawn)
    - pow: position in final code representing the moved piece
    """
    values = {"N": 2, "B": 3, "R": 4, "Q": 5, "K": 6}
    if piece.islower():
        # is a pawn
        value = 1
    else:
        value = values[piece]
    return value*10**pow


def parse_column(pos, pow):
    """
    Checks the column
    Arguments:
    - pos: current column represented by a letter
    - pow: position in final code representing the queried column
    """
    values = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
    value = values[pos]
    return value*10**pow


def parse_movements(game):
    """
    Returns a list of chess movements in a numerical notation
    following
        color|piece |movement|sourceCol|sourceRow|targetCol|targetRow       
        {1,2}|{1,,6}|{1,,3}  |0        |0        |{1,,8}   |{1,,8}
    structure and values
    Arguments:
    - game: list of moves in string format
    """
    movements = []
    for n_mov in range(0, len(game)):
        mov = game[n_mov]
        mov, code = parse_special_move(n_mov, mov, 4)
        code += parse_piece(mov[0], 5)
        if code//(10**5) != 1:
            # is not a pawn
            mov = mov[1:]
            # disambiguation case
            while(len(mov) > 2):
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
