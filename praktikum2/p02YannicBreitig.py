from random import randint, choice

EMPTY = ' '
SHIP = 'X'

MAX_ATTEMPTS = 100


def create_area(size):
    return [[EMPTY for _ in range(size[1])] for _ in range(size[0])] \
        if 2 <= size[0] <= 10 and 2 <= size[1] <= 10 else None


def fill_area(area, p0, is_horiz, length):
    row, col = p0[0], p0[1]

    if is_horiz:
        area[row][col:col + length] = SHIP * length
    else:
        for i in range(row, row + length):
            area[i][col] = SHIP


def print_area(area, title):
    output = f"{title}\n"
    width, height = len(area[0]), len(area)

    output += f" |{''.join([str(i) for i in range(width)])}|\n"

    for i, row in enumerate(area):
        output += f"{i}|{''.join(row)}|\n"

    output += f" |{''.join([str(i) for i in range(width)])}|\n"

    print(output)


def check_area(area, p0, is_horiz, length, profi_check=False):
    width, height = len(area[0]), len(area)
    row, col = p0[0], p0[1]

    if not (0 <= row < height and 0 <= col < width):
        return False

    elif is_horiz:
        if col + length > width:
            return False

        elif profi_check:
            return False if 'X' in unpack([area[i][boundary(col - 1, width):boundary(col + length + 1, width)]
                                           for i in range(boundary(row - 1, height),
                                                          boundary(row + 2, height))]) else True

        return False if 'X' in area[row][col:col + length] else True

    else:
        if row + length > height:
            return False

        elif profi_check:
            return False if 'X' in unpack([area[i][boundary(col - 1, width):boundary(col + 2, width)]
                                           for i in range(boundary(row - 1, height),
                                                          boundary(row + length + 1, height))]) else True

        return False if 'X' in [area[i][col] for i in range(row, row + length)] else True


def boundary(value, limit):
    return min(limit, max(0, value))


def unpack(regular_list):
    return [item for sublist in regular_list for item in sublist]


def generate_boat(area, boat_spec):
    if isinstance(boat_spec, dict):
        for key, val in boat_spec.items():
            idx = 0
            while idx < key:
                idx += 1
                generate_boat(area, val)
    else:
        attempt = 0
        while attempt <= MAX_ATTEMPTS:
            attempt += 1

            p0 = (randint(0, 10), randint(0, 10))
            direction = choice([True, False])

            if check_area(area, p0, direction, boat_spec):
                fill_area(area, p0, direction, boat_spec)
                break

