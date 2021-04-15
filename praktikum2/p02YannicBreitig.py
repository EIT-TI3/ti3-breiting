from random import randint, choice

EMPTY = ' '
SHIP = 'X'

MAX_ATTEMPTS = 10


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
    Fills the board elements with 'X' for the boat

    :param board: :list: Board to fill
    :param p0: :tuple: Start position
    :param is_horiz: :bool: Orientation of the boat
    :param length: :int: Length of the boat
    :return: :None:
    """
    row, col = p0

    if is_horiz:
        board[row][col:col + length] = SHIP * length

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
    Validates the position of the new boat

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
        if not horiz_check(board, row, col, length):
            validation = False

    else:
        if not vertical_check(board, row, col, length):
            validation = False

    if profi_check:
        if 'X' in flatten(surrounding_field(board, row, col, is_horiz, length)):
            validation = False

    return validation


def generate_boat(board, boat_specs):
    """
    Generates boats with the given boat_specs

    :param board: Board to add boats
    :param boat_specs: :int: Length of the boat or
                      :dict: {key: Length of the boat, value: Amount of boats}
    :return: :None:
    """
    if isinstance(boat_specs, dict):
        for length, amount in boat_specs.items():
            idx = 0
            while idx < amount:
                generate_boat(board, length)
                idx += 1
    else:
        attempt = 0
        while attempt <= MAX_ATTEMPTS:
            attempt += 1

            p0 = (randint(0, 10), randint(0, 10))
            is_horiz = choice([True, False])

            if check_area(board, p0, is_horiz, boat_specs, profi_check=True):
                fill_area(board, p0, is_horiz, boat_specs)
                break
        else:
            is_horiz = choice([True, False])
            p0 = valid_boat_position(board, is_horiz, boat_specs)
            fill_area(board, p0, is_horiz, boat_specs)


def valid_boat_position(board, is_horiz, length):
    for row, col in index_generator(board, is_horiz):
        if check_area(board, (row, col), is_horiz, length):
            return row, col


def index_generator(board, is_horiz):
    width, height = len(board[0]), len(board)

    for row in range(height):
        for col in range(width):
            yield (row, col) if is_horiz else (col, row)


def horiz_check(board, row, col, length):
    width, height = len(board[0]), len(board)
    validation = True

    if col + length > width:
        validation = False

    elif 'X' in board[row][col:col + length]:
        validation = False

    return validation


def vertical_check(board, row, col, length):
    width, height = len(board[0]), len(board)
    validation = True

    if row + length > height:
        validation = False

    elif 'X' in [board[i][col] for i in range(row, row + length)]:
        validation = False

    return validation


def surrounding_field(board, row, col, is_horiz, length):
    width, height = len(board[0]), len(board)

    lower_col_bound, lower_row_bound = boundary(col - 1, width), boundary(row - 1, height)

    upper_col_bound = boundary(col + length + 1, width) if is_horiz else boundary(col + 2, width)
    upper_row_bound = boundary(row + 2, height) if is_horiz else boundary(row + length + 1, height)

    return [board[row_idx][lower_col_bound:upper_col_bound] for row_idx in range(lower_row_bound, upper_row_bound)]


def boundary(value, limit):
    return min(limit, max(0, value))


def flatten(nested_list):
    return [item for sublist in nested_list for item in sublist]


def check_win(board):
    return False if 'X' in flatten(board) else True


def play_battleship():
    board1 = create_area((10, 10)), create_area((10, 10))
    board2 = create_area((10, 10)), create_area((10, 10))

    generate_boat(board1[0], {5: 1, 4: 2, 3: 3, 2: 4}), generate_boat(board2[0], {5: 1, 4: 2, 3: 3, 2: 4})

    active_player = 1

    turn = 0
    running = True

    print_area(board1[0], 'Dein Board')

    while running:
        turn += 1

        if active_player == 1:
            p0 = tuple(int(x) for x in input('Gib die Position des gewünschten Feldes ein <X,Y>').split(','))
            if game_loop(board2, p0):
                active_player = 2

        elif active_player == 2:
            p1 = (randint(0, 9), randint(0, 9))
            if game_loop(board1, p1):
                active_player = 1

        if check_win(board1[0]) or check_win(board2[0]):
            break


def game_loop(board, p0):
    row, col = p0
    change_player = True

    if board[1][row][col] == 'O':
        print('Invalider Zug!\n')
        change_player = False

    elif board[0][row][col] == 'X':
        print('Treffer!\n')
        board[0][row][col] = 'O'
        board[1][row][col] = 'O'
        change_player = False

    elif board[0][row][col] == ' ':
        board[1][row][col] = 'O'
        print('Leider nicht getroffen!\n')

    print_area(board[1], '')

    return change_player


if __name__ == '__main__':
    play_battleship()
