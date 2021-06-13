import random
from math import floor


def slowsort(iterable, *_args):
    if _args is None:
        i, j = min(iterable), max(iterable)
    else:
        i, j = _args

    if i < j:
        m = floor((i + j) / 2)

        slowsort(iterable, i, m)
        slowsort(iterable, m + 1, j)

        if iterable[j] < iterable[m]:
            iterable[j], iterable[m] = iterable[m], iterable[j]

        slowsort(iterable, i, j - 1)


def quicksort(iterable, lower, higher):
    if lower < higher:
        p = partition(iterable, lower, higher)
        quicksort(iterable, lower, p-1)
        quicksort(iterable, p + 1, higher)


def partition(iterable, lower, higher):
    pivot = iterable[higher]
    i = lower
    for j in range(lower, higher):
        if iterable[j] < pivot:
            iterable[i], iterable[j] = iterable[j], iterable[i]

    iterable[i], iterable[higher] = iterable[higher], iterable[i]
    return i


test_list = [random.randint(0, 10) for _ in range(10)]
quicksort(test_list, 0, len(test_list)-1)
