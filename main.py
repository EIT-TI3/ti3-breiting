import cmath
import datetime

from operator import mod
from numpy.ma import arctan

import stack


def ggT(a, b):
    if b == 0:
        return a
    else:
        return ggT(b, mod(a, b))


def magic(l, r):
    p = 0
    if r == 0:
        return
    else:
        while r > 0:
            p = p + l
            r = r - 1
        return p


# Aufgabe 1
def python():
    return '+--------+\n'' + Python + \n''+--------+\n'


# Aufgabe 2
def hello():
    name, surename = input('Bitte gib deinen Vor&Nachnamen ein!').split(' ')
    print(f'Guten Tag {name} {surename}')


# Aufgabe 3
def calculate(a, b, c):
    return (a+b) * c


def kot_arctan(number):
    return arctan(number)


def days_parsed(a, b):
    d1, m1, y1, = a.split('.')
    d2, m2, y2, = b.split('.')
    output = 0
    d_diff = abs(int(d2) - int(d1))
    d1, m1, y1 = int(d1), int(m1), int(y1)
    d2, m2, y2 = int(d2), int(m2), int(y2)

    for year in range(int(y1), int(y2) + 1):
        if mod(y1 + year, 4) == 0:
            output += 366
        else:
            output += 365

    for month in range(int(m1), int(m2) + 1):
        if m1 == 1:
            output += 29
        if mod(m1 + month, 2) == 0:
            output += 30
        else:
            output += 31

    print(output + d_diff)


def days_parsed_time(a, b):
    time1 = datetime.datetime.fromisoformat(a)
    time2 = datetime.datetime.fromisoformat(b)
    time_res = time1 - time2
    print(abs(time_res))


# l1 = [3]
# l2 = [1, 2]
# l3 = [l1, 4]
# l4 = [l2, l3]
# l5 = ['abc', l4, 5]
# l1[0] = 42

def format_seconds():
    sec = int(input('Bitte die Sekunden angeben!'))
    min, seconds = divmod(sec, 60)
    hours, minutes = divmod(min, 60)
    print(f'{hours}:{minutes}:{seconds}')


def mitternachtsformel(a, b, c):
    try:
        a, b, c = int(a), int(b), int(c)
    except ValueError:
        return 'beliebige Loesung'
    if a == 0:
        try:
            x = -c / b
            return x
        except ZeroDivisionError:
            return 'keine Loesung'

    det = b ** 2 - 4 * a * c

    if det == 0:
        x = -b / (2 * a)
        return x
    elif det:
        x1 = (-b + cmath.sqrt(det)) / (2 * a)
        x2 = (-b - cmath.sqrt(det)) / (2 * a)
        return x1, x2


def convert_str():
    s = '0123456789'
    print(s[1:len(s)])
    print(s[0:-1])
    print(s[2:])
    print(s[0:-2])
    print(s[1:-1])
    print(s[7] + s[4] + s[1])
    print(s + rotate_str(s))
    print(only_odd(s) + rotate_str(s)[0:])
    odd_str = only_odd(s)
    print(sort_string(odd_str) + rotate_str(sort_string(odd_str))[1:])


def rotate_str(string):
    out = ''
    for e in range(0, len(string)):
        out += string[-e - 1]
    return out


def only_odd(string):
    out = ''
    for i in range(0, len(string)):
        if mod(int(string[i]), 2) != 0:
            out += string[i]
    return out


def sort_string(string):
    out = ''
    num = []
    for e in range(0, len(string)):
        num.append(int(string[e]))
    for i in sorted(num):
        out += str(i)
    return out


def check_c_code():
    file_name = 'mittel.c'
    stapel = stack.Stack()
    paare = {'<': '>', '{': '}', '(': ')', '[': ']'}
    datei_zeilen = open(file_name, 'r').readlines()
    zeilen_nummer = 0
    fehler = False
    for zeile in datei_zeilen:
        if fehler:
            break
        zeilen_nummer += 1
        for zeichen in zeile:
            if zeichen in paare.keys():
                stapel.push([zeichen, zeilen_nummer])
            elif zeichen in paare.values():
                if paare[stapel.top()[0]] == zeichen:
                    stapel.pop()
                else:
                    print(f'Fehler {stapel.top()[0]} in Zeile {stapel.top()[1]}')
                    fehler = True

    if not fehler:
        print(f'Programm {file_name} hat keine Klammer-Fehler!')


# t_c = [-17.2, 12.4, -2.5, 1.7, -5.3, 20.5, 13.8, -9.9]
# kalt = [n for n in t_c if n < 0]
# warm = [n for n in t_c if n > 0]
#
# t_f = [t * (9 / 5) + 32 for t in t_c]
#
# satz = "Man muss nicht alles wissen"
# l1 = [satz[i] for i in range(0, len(satz))]
# vowels = ['a', 'e', 'i', 'o', 'u']
# l2 = [i for i in l1 if i.lower() not in vowels]
# print(l2)


def sieb_des_eratosthenes(n):
    l = list(range(2, n))
    p = []

    while l[0] ** 2 < n:
        p.append(l[0])
        filter = [n for n in l if mod(n, l[0]) == 0]
        for i in filter:
            l.remove(i)
    p.append(l)
    print(f'Gefundene Primzahlen: {p}')


def cards():
    farben = ['Karo', 'Herz', 'Pik', 'Kreuz']
    symbole = ['7', '8', '9', 'Bube', 'Dame', 'Koenig', '10', 'Ass']
    karten = [[i, f] for f in farben for i in symbole]


def self_zip():
    damen = ['Maria', 'Anne', 'Else', 'Lisa']
    herren = ['Hans', 'Leo', 'Tim', 'Sigi']
    erg_zip = list(zip(damen, herren))
    my_zip = [(damen[i-1], herren[i-1]) for i in range(0, len(damen))]



def perfect_numbers(n):
    list = [i for i in range(1, n+1) if i == sum(e for e in [d for d in range(1, n+1) if (mod(i, d) == 0) and (i is not d)])]
    print(list)

perfect_numbers(500)