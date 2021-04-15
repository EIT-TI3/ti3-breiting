from random import randint, choice

EMPTY = ' '
SHIP = 'X'

MAX_ATTEMPTS = 1000


def create_area(size):
    """
    Creates the board after validation

    :param size: :tuple: Size of the board
    :return: :list: Nested list which contains empty strings
    """
    row, col = size

    if 2 <= row <= 10 and 2 <= col <= 10:
        return [[EMPTY for _ in range(col)] for _ in range(row)]


def fill_area(area, p0, is_horiz, length):
    """
    Fills the board elements with 'X' for the boat

    :param area: :list: Board to fill
    :param p0: :tuple: Start position
    :param is_horiz: :bool: Orientation of the boat
    :param length: :int: Length of the boat
    :return: :None:
    """
    row, col = p0

    if is_horiz:
        area[row][col:col + length] = SHIP * length

    elif not is_horiz:
        for i in range(row, row + length):
            area[i][col] = SHIP
    return


def print_area(area, title):
    """
    Prints the enumerated board in the console

    :param area: :list: Board to print
    :param title: :str: Title of the board
    :return: :None:
    """
    output = f"{title}\n"
    width, height = len(area[0]), len(area)

    output += f" |{''.join([str(i) for i in range(width)])}|\n"

    for i, row in enumerate(area):
        output += f"{i}|{''.join(row)}|\n"

    output += f" |{''.join([str(i) for i in range(width)])}|\n"

    print(output)
    return


def check_area(area, p0, is_horiz, length, profi_check=False):
    """
    Validates the position of the new boat

    :param area: :list: Board which gets tested
    :param p0: :tuple: Start position of the new boat
    :param is_horiz: :bool: Orientation of the boat
    :param length: :int: Length of the boat
    :param profi_check: :bool: Prevents boats from touching each other
    :return: :bool: True if the position is valid
    """
    width, height = len(area[0]), len(area)
    row, col = p0
    validation = True

    if not (0 <= row < height and 0 <= col < width):
        validation = False

    elif is_horiz:
        if not _horiz_check(area, row, col, length, profi_check):
            validation = False

    elif not is_horiz:
        if not _vertical_check(area, row, col, length, profi_check):
            validation = False

    return validation


def generate_boat(area, boat_spec):
    """
    Generates boats with the given boat_spec

    :param area: Board to add boats
    :param boat_spec: :int: Length of the boat or
                      :dict: {key: Amount of boats, value: Length of the boat}
    :return: :None:
    """
    if isinstance(boat_spec, dict):
        for amount, length in boat_spec.items():
            idx = 0
            while idx < amount:
                idx += 1
                generate_boat(area, length)
    else:
        attempt = 0
        while attempt <= MAX_ATTEMPTS:
            attempt += 1

            p0 = (randint(0, 10), randint(0, 10))
            direction = choice([True, False])

            if check_area(area, p0, direction, boat_spec, profi_check=True):
                fill_area(area, p0, direction, boat_spec)
                break
    return


def _horiz_check(area, row, col, length, profi_check=False):
    width, height = len(area[0]), len(area)
    validation = True

    if col + length > width:
        validation = False

    elif profi_check:
        if 'X' in flatten(_horiz_surrounding_field(area, row, col, length)):
            validation = False

    elif 'X' in area[row][col:col + length]:
        validation = False

    return validation


def _vertical_check(area, row, col, length, profi_check=False):
    width, height = len(area[0]), len(area)
    validation = True

    if row + length > height:
        validation = False

    elif profi_check:
        if 'X' in flatten(_vertical_surrounding_field(area, row, col, length)):
            validation = False

    elif 'X' in [area[i][col] for i in range(row, row + length)]:
        validation = False

    return validation


def _horiz_surrounding_field(area, row, col, length):
    width, height = len(area[0]), len(area)

    lower_col_bound, upper_col_bound = boundary(col - 1, width), boundary(col + length + 1, width)
    lower_row_bound, upper_row_bound = boundary(row - 1, height), boundary(row + 2, height)

    return [area[row_idx][lower_col_bound:upper_col_bound] for row_idx in range(lower_row_bound, upper_row_bound)]


def _vertical_surrounding_field(area, row, col, length):
    width, height = len(area[0]), len(area)

    lower_col_bound, upper_col_bound = boundary(col - 1, width), boundary(col + 2, width)
    lower_row_bound, upper_row_bound = boundary(row - 1, height), boundary(row + length + 1, height)

    return [area[row_idx][lower_col_bound:upper_col_bound] for row_idx in range(lower_row_bound, upper_row_bound)]


def boundary(value, limit):
    return min(limit, max(0, value))


def flatten(nested_list):
    return [item for sublist in nested_list for item in sublist]


def check_win(area):
    return False if 'X' in flatten(area) else True


def play_battleship():
    board1 = create_area((10, 10)), create_area((10, 10))
    board2 = create_area((10, 10)), create_area((10, 10))

    generate_boat(board1[0], {1: 5, 2: 4, 3: 3, 4: 2}), generate_boat(board2[0], {1: 5, 2: 4, 3: 3, 4: 2})

    activ_player = 1

    turn = 0
    running = True

    print_area(board1[0], 'Dein Board')

    while running:
        turn += 1

        if activ_player == 1:
            p0 = tuple(int(x) for x in input('Gib die Position des gewünschten Feldes ein <X,Y>').split(','))
            if game_loop(board2, p0):
                activ_player = 2

        elif activ_player == 2:
            p1 = (randint(0, 9), randint(0, 9))
            if game_loop(board1, p1):
                activ_player = 1

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
