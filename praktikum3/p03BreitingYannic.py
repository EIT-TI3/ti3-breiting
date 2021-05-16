"""
Frage1:
split ist eine Methode der Klasse String, die mit dem assoziierten Objekt aufgerufen wird
Funktionen sind aufrufbare Objekte, die mit dem 'call operator' aufgerufen werden
"""

from v3_util import check_time


def read_data(data, val_name='value'):
    with open(data) as file:
        text = file.readlines()

    table = {'date': list(), 'time': list(), val_name: list()}
    data_list = list(zip(*[line.split(';') for line in text]))

    for i, e in enumerate(table):
        table[e] = data_list[i]
    return table


def stats(table, val_name):
    values = [float(element) for element in table[val_name] if element is not None]

    return len(values), min(values), max(values), sum(values) / len(values)


def add_entry(table, d, t, val_name0, val_name1, val0, val1):
    table['date'].append(d)
    table['time'].append(t)
    table[val_name0].append(val0)
    table[val_name1].append(val1)


def merge(data0, data1):
    key1, key2 = tuple(data0.keys())[-1], tuple(data1.keys())[-1]
    table = {'date': list(), 'time': list(), key1: list(), key2: list()}

    curr_ndx0, curr_ndx1 = 0, 0
    while curr_ndx0 < len(data0['date']) or curr_ndx1 < len(data1['date']):
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

        else:
            continue

        add_entry(table, date, time, key1, key2, val0, val1)

    return table


def print_table(table, number_space=7, entry_space=15):

    output = 'index'.ljust(number_space)

    for title in table.keys():
        output += f'{title}'.ljust(entry_space)

    output += "\n"

    for idx in range(len(table['date'])):
        output += f'{idx+1}'.ljust(number_space)
        for row in table:
            output += f"{table[row][idx]}".ljust(entry_space)
        output += '\n'

    print(output)


if __name__ == '__main__':
    fn = "TESTcsv_803_172.csv"
    table_no2 = read_data(fn, "no2")
    fn = "TESTcsv_803_132G.csv"
    table_fs = read_data(fn, "fs")
    table_new = merge(table_no2, table_fs)
    print_table(table_new)
