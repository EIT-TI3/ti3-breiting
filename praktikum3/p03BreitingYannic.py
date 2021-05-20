"""
Frage1:
split ist eine Methode der Klasse String, die mit dem assoziierten Objekt aufgerufen wird
Funktionen sind aufrufbare Objekte, die mit dem 'call operator' aufgerufen werden
"""

from v3_util import check_time


def read_data(data: str, val_name: str = 'value') -> dict:
    """
    Reads data from csv file and parses it to a dict

    :param data: :str: Name of the file
    :param val_name: :str: Name of the measured values
    :return: :dict: Parsed values from given csv file
    """

    with open(data) as file:
        text = file.readlines()

    table = {'date': [], 'time': [], val_name: []}
    data_list = list(zip(*[line.strip().split(';') for line in text]))

    for idx, e in enumerate(table):
        table[e] = data_list[idx]

    return table


def stats(table: dict, val_name: str) -> tuple or None:
    """
    Calculates the length, maximum, minimum and average of the measured values

    :param table: :dict: Table containing the data
    :param val_name: :str: Name of the measured values
    :return: :tuple(int | float): or :None: if no values exist
    """

    values = tuple(float(element) for element in table[val_name] if element is not None)

    return (len(values), min(values), max(values), sum(values) / len(values)) if len(values) != 0 else (None,)*4


def add_entry(table: dict, d: str, t: str, val_name0: str, val_name1: str, val0: int, val1: int) -> None:
    """
    Adds a new entry to the data dict

    :param table: :dict: Table containing the data
    :param d: :str: Date
    :param t: :str: Time
    :param val_name0: :str: Name of the measured values from the first table
    :param val_name1: :str: Name of the measured values from the second table
    :param val0: :int: Measured value from the first table
    :param val1: :int: Measured value from the first table
    :return: :None:
    """

    table['date'].append(d)
    table['time'].append(t)
    table[val_name0].append(val0)
    table[val_name1].append(val1)


def merge(data0: dict, data1: dict) -> dict:
    """
    Combines the input tables and sorts it by date and time

    :param data0: :dict: First table
    :param data1: :dict: Second table
    :return: :dict: Combined table
    """

    key1, key2 = (data0.keys() - data1.keys()).pop(), (data1.keys() - data0.keys()).pop()
    table = {name: list() for name in data0.keys() | data1.keys()}

    curr_ndx0, curr_ndx1 = 0, 0
    data0_len, data1_len = len(data0['date']), len(data1['date'])

    while curr_ndx0 < data0_len or curr_ndx1 < data1_len:
        position = check_time(data0, data1, curr_ndx0, curr_ndx1)

        if position == -1:
            date, time = data0['date'][curr_ndx0], data0['time'][curr_ndx0]
            val0, val1 = int(data0[key1][curr_ndx0]), None
            curr_ndx0 += 1

        elif position == 1:
            date, time = data1['date'][curr_ndx1], data1['time'][curr_ndx1]
            val0, val1 = None, int(data1[key2][curr_ndx1])
            curr_ndx1 += 1

        elif position == 0:
            date, time = data1['date'][curr_ndx1], data1['time'][curr_ndx1]
            val0, val1 = int(data0[key1][curr_ndx0]), int(data1[key2][curr_ndx1])
            curr_ndx0 += 1
            curr_ndx1 += 1

        # Kommt nur im Fehlerfall vor!
        else:
            continue

        add_entry(table, date, time, key1, key2, val0, val1)

    return table


def print_table(table: dict, index_space: int = 7, entry_space: int = 15) -> None:
    """
    Prints the data of the table in the console

    :param table: :dict: Table containing the data
    :param index_space: :int: Defines the spacing of indices
    :param entry_space: :int: Defines the spacing of entries
    :return: :None:
    """
    order = ('date', 'time', *(table.keys() - {'date', 'time'}))
    output = 'index'.ljust(index_space)

    for title in order:
        output += f'{title}'.ljust(entry_space)

    output += "\n"

    for idx in range(len(table['date'])):
        output += f'{idx+1}'.ljust(index_space)
        for row in order:
            output += f"{table[row][idx]}".ljust(entry_space)
        output += '\n'

    print(output)


if __name__ == '__main__':
    fn = "TESTcsv_803_172.csv"
    table_no2 = read_data(fn, "n02")

    fn = "TESTcsv_803_132G.csv"
    table_fs = read_data(fn, "fs")
    test = stats(table_no2, "n02")

    print('N02 Werte \nMesswerte: {}, Min: {}, Max: {}, Durchschnitt: {:F} \n'.format(*stats(table_no2, "n02")))
    print('Feinstaub Werte \nMesswerte: {}, Min: {}, Max: {}, Durchschnitt: {:F} \n'.format(*stats(table_fs, "fs")))

    table_new = merge(table_no2, table_fs)
    print_table(table_new)
