from random import randint, choice

EMPTY = ' '
SHIP = 'X'

HIT = 'H'
MISS = 'O'
INVALID = 'I'

STANDARD_SIZE = 10, 10
MAX_ATTEMPTS = 100

GAME_CONFIG = {5: 1, 4: 2, 3: 2, 2: 2}


def create_area(size):
    """
    Creates the board after validation

    :param size: :tuple: Size of the board
    :return: :list: Nested list which contains empty strings
    """
    row, col = size

    if 2 <= row <= 10 and 2 <= col <= 10:
        return [[EMPTY for _ in range(col)] for _ in range(row)]


def fill_area(board, p0, is_horiz, length):
    """
    Fills the board elements with 'SHIP' for the boat

    :param board: :list: Board to fill
    :param p0: :tuple: Start position
    :param is_horiz: :bool: Orientation of the boat
    :param length: :int: Length of the boat
    :return: :None:
    """
    row, col = p0

    if is_horiz:
        board[row][col:col + length] = [SHIP] * length

    else:
        for i in range(row, row + length):
            board[i][col] = SHIP


def print_area(board, title):
    """
    Prints the enumerated board in the console

    :param board: :list: Board to print
    :param title: :str: Title of the board
    :return: :None:
    """
    output = f"{title}\n"
    width, height = len(board[0]), len(board)

    output += f" |{''.join([str(i) for i in range(width)])}|\n"

    for i, row in enumerate(board):
        output += f"{i}|{''.join(row)}|\n"

    output += f" |{''.join([str(i) for i in range(width)])}|\n"

    print(output)


def check_area(board, p0, is_horiz, length, profi_check=False):
    """
    Validates the position of a new boat

    :param board: :list: Board which gets tested
    :param p0: :tuple: Start position of the new boat
    :param is_horiz: :bool: Orientation of the boat
    :param length: :int: Length of the boat
    :param profi_check: :bool: Prevents boats from touching each other
    :return: :bool: True if the position is valid
    """
    width, height = len(board[0]), len(board)
    row, col = p0
    validation = True

    if not (0 <= row < height and 0 <= col < width):
        validation = False

    elif is_horiz:
        if not check_horiz(board, row, col, length):
            validation = False

    else:
        if not check_vertical(board, row, col, length):
            validation = False

    if profi_check:
        if SHIP in flatten(surrounding_area(board, row, col, length, is_horiz=is_horiz)):
            validation = False

    return validation


def check_horiz(board, row, col, length):
    width, height = len(board[0]), len(board)
    validation = True

    if col + length > width:
        validation = False

    elif SHIP in board[row][col:col + length]:
        validation = False

    return validation


def check_vertical(board, row, col, length):
    width, height = len(board[0]), len(board)
    validation = True

    if row + length > height:
        validation = False

    elif SHIP in [board[i][col] for i in range(row, row + length)]:
        validation = False

    return validation


def generate_boat(board, boat_specs, profi_check=False, copy=None):
    """
    Generates boats with the given boat_specs

    :param board: Board to add boats
    :param boat_specs: :int: Length of the boat or :dict: {key: Length of the boat, value: Amount of boats}
    :param profi_check: :bool: Generated ships can not touch eachother
    :param copy: :dict: Copy of boat_specs dict
    :return: :None:
    """
    if type(boat_specs) == dict:
        for length, amount in boat_specs.items():
            for _ in range(amount):
                generate_boat(board, length, profi_check=profi_check, copy=boat_specs)
    else:
        attempt = 0
        while attempt <= MAX_ATTEMPTS:
            attempt += 1

            # Random start location and orientation
            p0 = (randint(0, 9), randint(0, 9))
            is_horiz = choice((True, False))

            if check_area(board, p0, is_horiz, boat_specs, profi_check=profi_check):
                fill_area(board, p0, is_horiz, boat_specs)
                break
        else:
            # Gets called after reaching MAX_ATTEMPTS
            is_horiz = choice((True, False))
            p0 = valid_boat_position(board, is_horiz, boat_specs)

            # Sometimes no valid location exists
            try:
                fill_area(board, p0, is_horiz, boat_specs)
            except TypeError:
                # Generate new board with recovered dict
                board = create_area(STANDARD_SIZE)
                generate_boat(board, copy, profi_check=profi_check)


def surrounding_area(board, row, col, length=1, is_horiz=True, INDEX=False):
    width, height = len(board[0]), len(board)

    lower_col_bound, lower_row_bound = boundary(col - 1, width), boundary(row - 1, height)

    upper_col_bound = boundary(col + length + 1, width) if is_horiz \
        else boundary(col + 2, width)

    upper_row_bound = boundary(row + 2, height) if is_horiz \
        else boundary(row + length + 1, height)

    index_list = [(row_idx, col_idx) for row_idx in range(lower_row_bound, upper_row_bound)
                  for col_idx in range(lower_col_bound, upper_col_bound)]

    area_list = [board[row_idx][lower_col_bound:upper_col_bound]
                 for row_idx in range(lower_row_bound, upper_row_bound)]

    return index_list if INDEX else area_list


def valid_boat_position(board, is_horiz, length):
    """
    Checks the board for a valid boat position

    :param board: :list: The board to check
    :param is_horiz: :bool: Orientation of the boat
    :param length: :int: Length of the boat
    :return: :tuple: Valid position
    """
    for row, col in index_generator(board, is_horiz=is_horiz):
        if check_area(board, (row, col), is_horiz, length, profi_check=True):
            return row, col


def index_generator(board, is_horiz=True):
    """
    Yields all empty board fields as tuple

    :param board: :list:
    :param is_horiz: :bool:
    :return: :tuple:
    """
    width, height = len(board[0]), len(board)

    for row in range(height):
        for col in range(width):
            if board[row][col] == EMPTY:
                yield (row, col) if is_horiz else (col, row)


def boundary(value, limit):
    return min(limit, max(0, value))


def flatten(nested_list):
    return [item for sublist in nested_list for item in sublist]


def play_battleship(MODE='SOLO'):
    player1 = {'board': create_area(STANDARD_SIZE),
               'shots': create_area(STANDARD_SIZE),
               'stack': [],
               'ships': GAME_CONFIG.copy(),
               'boat_loc': []}

    player2 = {'board': create_area(STANDARD_SIZE),
               'shots': create_area(STANDARD_SIZE),
               'stack': [],
               'boat_loc': []}

    generate_boat(player1['board'], GAME_CONFIG, profi_check=True)
    generate_boat(player2['board'], GAME_CONFIG, profi_check=True)

    active_player = 1

    turn = 0
    running = True

    while running:
        turn += 1

        if MODE == 'SOLO':
            active_player = 1

        if active_player == 1:
            if MODE == 'PLAY':
                print_area(player1['shots'], 'Deine Schuesse')
                row, col = tuple(int(x) for x in input().split(','))
            else:
                row, col = optimized_turn(player1)

            if player2['board'][row][col] == SHIP:
                player1['shots'][row][col] = HIT
                player2['board'][row][col] = HIT
            else:
                player1['shots'][row][col] = MISS
                active_player = 2

        elif active_player == 2:
            row, col = optimized_turn(player2)
            print_area(player2['shots'], 'Gegner Schuesse')
            if player1['board'][row][col] == SHIP:
                player2['shots'][row][col] = HIT
                player1['board'][row][col] = HIT
            else:
                player2['shots'][row][col] = MISS
                active_player = 1

        if check_win(player1['board']) or check_win(player2['board']):
            running = False

    else:
        print(f'Player{active_player} won in {turn}. turns!')
        print_area(player2['board'], 'Player2 board')
        print_area(player1['shots'], 'Player1 shots')


def check_win(board):
    return False if SHIP in flatten(board) else True


def optimized_turn(player):
    shots = player['shots']
    stack = player['stack']

    if len(stack) > 0:
        row, col = stack.pop()
        if shots[row][col] == HIT:
            for i, j in invalid_shots(shots, row, col):
                if shots[i][j] == EMPTY:
                    shots[i][j] = INVALID

            for i, j in stack:
                if shots[i][j] != EMPTY:
                    stack.remove((i, j))

            stack += [(i, j) for i, j in surrounding_area(shots, row, col, INDEX=True)
                      if shots[i][j] == EMPTY and (i, j) not in stack]

        if len(stack) == 0:
            row, col = random_possible_shot(shots)
            stack.append((row, col))

        else:
            row, col = stack[-1]

    else:
        row, col = random_possible_shot(shots)
        stack.append((row, col))

    return row, col


def random_possible_shot(shots, PARITY=2):
    possible_shots = [idx for idx in index_generator(shots) if sum(idx) % PARITY == 0]
    try:
        row, col = possible_shots[randint(0, len(possible_shots) - 1)]
    except ValueError:
        row, col = next(index_generator(shots))

    return row, col


def invalid_shots(board, row, col):
    result = []
    surrounding_hits = [(row, col) for row, col in surrounding_area(board, row, col, INDEX=True)
                        if board[row][col] == HIT]

    if len(surrounding_hits) > 1:
        orientation = check_ship_orientation(surrounding_hits)
        if orientation is None:
            pass
        elif orientation == 'HORIZ':
            result = [(row, col) for row, col in surrounding_area(board, row, col, INDEX=True)
                      if row != surrounding_hits[0][0]]
        elif orientation == 'VERTICAL':
            result = [(row, col) for row, col in surrounding_area(board, row, col, INDEX=True)
                      if col != surrounding_hits[0][1]]
    else:
        result = [idx for idx in surrounding_area(board, row, col, INDEX=True)
                  if idx[0] != row and idx[1] != col]

    return result


def check_ship_orientation(idx_list):
    result = None
    for row, col in idx_list:
        if row == idx_list[0][0]:
            result = 'HORIZ'
        elif col == idx_list[0][1]:
            result = 'VERTICAL'
        else:
            result = None
            break
    return result


if __name__ == '__main__':
    play_battleship()
