import cmath
import csv
import datetime
import math
from itertools import chain

from operator import mod
from random import randint

from numpy.ma import arctan

import stack


def ggT(a, b):
    if b == 0:
        return a
    else:
        return ggT(b, mod(a, b))


# S. 12
def magic(l, r):
    p = 0
    if r == 0:
        return
    else:
        while r > 0:
            p = p + l
            r = r - 1
        return p


# S. 46, Aufgabe 1
def python():
    return '+--------+\n'' + Python + \n''+--------+\n'


# S. 46, Aufgabe 2
def hello():
    name, surename = input('Bitte gib deinen Vor&Nachnamen ein!').split(' ')
    print(f'Guten Tag {name} {surename}')


# S. 46, Aufgabe 3
def calculate(a, b, c):
    return (a + b) * c


# S. 46
def calc_arctan(number):
    return arctan(number)


# S. 47
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
    print(s[1:])
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


# S. 128
def check_c_code():
    file_name = 'C:/Users/Yanni/Documents/GitHub/ti3/mittel.c'
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

# S. 137
def sieb_des_eratosthenes(n):
    l, p = list(range(2, n)), []

    while l[0] ** 2 < n:
        p.append(l[0])
        for i in [n for n in l if mod(n, l[0]) == 0]:
            l.remove(i)
    p += l
    print(f'Gefundene Primzahlen: {p}')


# S.138
def cards():
    farben = ['Karo', 'Herz', 'Pik', 'Kreuz']
    symbole = ['7', '8', '9', 'Bube', 'Dame', 'Koenig', '10', 'Ass']
    return [[i, f] for f in farben for i in symbole]


# S.138
def self_zip():
    damen = ['Maria', 'Anne', 'Else', 'Lisa']
    herren = ['Hans', 'Leo', 'Tim', 'Sigi']
    erg_zip = list(zip(damen, herren))
    return [(damen[i - 1], herren[i - 1]) for i in range(0, len(damen))]


# S.138
def perfect_numbers(n):
    list = [i for i in range(1, n + 1) if
            i == sum([d for d in range(1, n + 1) if (mod(i, d) == 0) and (i is not d)])]
    print(list)


def potenz_mengeL(m):
    return


def pretty_print(p):
    output = ''
    for idx, coefficient in enumerate(p):
        if idx == 0:
            output += str(p[0])
        else:
            output += f' {"-" if coefficient < 0 else "+"} {abs(coefficient)}*x^{idx}'
    return output


def add(p1, p2):
    return tuple([sum(element) for element in zip(p1, p2)])


def mul(p1, p2):
    return tuple([element[0] * element[1] for element in zip(p1, p2)])


def diff(p):
    return tuple([index * number for index, number in enumerate(p)])


def integrate(p):
    return tuple([p[0]] + [number / (index + 1) for index, number in enumerate(p)])


def to_pig_latin(word):
    if ord(word[0]) >= 90:
        return str(word[2::] + word[0:2])
    else:
        return str(word[2].upper() + word[3::] + word[0:2].lower())


def from_pig_latin(word):
    if ord(word[0]) >= 90:
        return str(word[-1:-2] + word[2::])
    else:
        return str(word[-2].upper() + word[-1] + word[:-2].lower())


def from_pig_zeile(zeile):
    output = ''
    for word in [to_pig_latin(word) for word in zeile.split()]:
        output += word + ' '
    return output


def from_pig_latin_zeile(zeile):
    output = ''
    for word in [from_pig_zeile(word) for word in zeile.split()]:
        output += word + ' '
    return output


def to_pig_latin_file(file_name='C:/Users/Yanni/Documents/GitHub/ti3/pig_latin.txt',
                      file_name_pig='C:/Users/Yanni/Documents/GitHub/ti3/pig_latin.txt'):
    try:
        with open(file_name, 'r') as file:
            text = file.readlines()
    except FileNotFoundError:
        print('Datein konnte nicht gefunden werden!')

    new_text = ''
    for lines in text:
        new_text += f'{from_pig_zeile(lines)}\n'
    try:
        with open(file_name_pig, 'w') as new_file:
            new_file.write(str(new_text))
    except Exception as e:
        print(e)


def haeufogkeit(zeile):
    chars = dict()
    for char in [char.upper() for char in zeile]:
        if char in chars:
            chars[char] = chars[char] + 1
        elif char.isalpha():
            chars[char] = 1

    output = ''
    idx = 0
    for letter, number in chars.items():
        idx += 1
        output += f'{letter} :   {number}   '
        if idx % 4 == 0:
            output += '\n'
    return output


def wortschatz(file_name='C:/Users/Yanni/Documents/GitHub/ti3/win1.txt'):
    unic_words = dict()
    all_words = 0

    try:
        file = open(file_name, 'r', errors='ignore')
    except Exception as e:
        print(e)
        return

    text = file.readlines()
    for lines in text:
        for word in lines.split(' '):
            all_words += 1
            if word in unic_words:
                unic_words[word] += 1
            else:
                unic_words[word] = 1
    quotient = len(unic_words) / all_words
    print(f'unterschiedliche Wörter: {len(unic_words)}, Wörter total: {all_words}, Quotient: {quotient}')


def read_csv():
    umsatz_dict = dict()

    with open('C:/Users/Yanni/Documents/GitHub/ti3/getreanke.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            values = row[0].split(';')
            umsatz_dict[values[0]] = [float(e) for e in values[1:]]
    return umsatz_dict


def berechne_summen_ueber_laeden(umsatz_dict):
    for getraenk in umsatz_dict:
        umsatz_dict[getraenk].append(sum(umsatz_dict[getraenk]))
    return umsatz_dict


def berechne_getraenke_summmen(umsatz_dict):
    umsatz_dict['Summe'] = []
    for i in range(4):
        summe = 0
        for getraenk in umsatz_dict:
            if getraenk != 'Summe':
                summe += umsatz_dict[getraenk][i]
        umsatz_dict['Summe'].append(summe)


def print_umsatz(umsatz_dict):
    output = 'Getraenk    Laden 0     Laden1     Summe\n'
    for getraenk in umsatz_dict:
        output += f'{getraenk}'
        for i in range(4):
            output += f'   {umsatz_dict[getraenk][i]}'
        output += '\n'
    print(output)


def get_min_umsatz(umsatz_dict):
    pass


def read_data(file_name='C:/Users/Yanni/Documents/GitHub/ti3/stichworte.txt'):
    try:
        with open(file_name, 'r') as file:
            text = file.readlines()
    except Exception as e:
        print(e)

    stichwoerter = dict()
    for line in text:
        key = line.split(':')[0]
        value = line[:-1].split(':')[1]
        if key not in stichwoerter.keys():
            stichwoerter[key] = [value]
        elif value not in stichwoerter[key]:
            stichwoerter[key].append(value)
    return stichwoerter


def print_index(stichwoerter):
    output = ''
    unique_types = set([value for value in chain.from_iterable(stichwoerter.values())])
    for e in unique_types:
        output += f'{e}      :'
        for i in stichwoerter.items():
            if e in i[1]:
                output += f'  {i[0]},'
        output += '\n'
    print(output)


# S. 191 Aufgabe 1
def drei_teilbar(n):
    return True if mod(n, 3) == 0 else False


# S. 191 Aufgabe 2
def compare_number1(n):
    return True if (1 / 3 <= n <= 8 / 13) else False


# S. 191 Aufgabe 3
def compare_number2(n):
    return True if (1 / 3 <= n <= 8 / 13) or (350 <= n <= 400) else False


# S. 191 Aufgabe 4
def compare_number3(n):
    return True if not (0 <= n <= 100) or (350 <= n <= 400) else False


# S. 191 Aufgabe 5

# if betrag <= stand:
#   stand -= betrag
# if betrag > stand:
#   stand -= betrag
#   stand -= gebuehr

# S. 192 Aufgabe 6
def mehrfach_teilbar(n):
    if mod(n, 2) + mod(n, 3) == 0:
        print('Teilbar durch 2 und 3!')
    elif mod(n, 2) == 0:
        print('Teilbar durch 2!')
    elif mod(n, 3) == 0:
        print('Teilbar durch 3!')
    else:
        print('Zahl ist nicht durch 2 oder 3 teilbar!')


# S. 192 Aufgabe 7
def rabattfunktion(n, k):
    if 1 <= n <= 100 and k == 0:
        print('3%')
    elif 1 <= n <= 100 and k != 0:
        print('5%')
    elif n >= 100 and k == 0:
        print('10%')
    elif n >= 100 and k != 0:
        print('15%')


# S. 192 Aufgabe 8
def compare_number(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    elif c < a and c < b:
        return c


# S. 192 Aufgabe 9
def check_input(func_input):
    vowels = ['a', 'e', 'i', 'o', 'u']
    try:
        int(func_input)
        print('Eingabe ist eine Zahl ')
        return
    except ValueError:
        pass

    if 65 <= ord(func_input) <= 90:
        if func_input.lower() in vowels:
            print('Eingabe ist ein Großbuchstabe und ein Vokal!')
        else:
            print('Eingabe ist ein Großbuchstabe und ein Konsonant!')
        return
    elif 97 <= ord(func_input) <= 122:
        if func_input in vowels:
            print('Eingabe ist ein Kleinbuchstabe und ein Vokal!')
        else:
            print('Eingabe ist ein Kleinbuchstabe und ein Konsonant!')
        return
    else:
        print('Eingabe konnte nicht zugeordnet werden!')
        return


# S. 195 Aufgabe 10
def calc_func(x):
    if -2 < x <= 3 or 4 <= x <= 5:
        return x ** 2 + 2 / 3 * x
    elif 5 < x < 6 or 10 <= x < 11:
        return math.sin(x)
    else:
        return math.cos(x)


# S. 195 Aufgabe 11
def check_schaltjahr(n):
    if n % 4 == 0:
        return False if (n % 100 == 0) and (n % 400 != 0) else True
    return False


# S. 196 Aufgabe 12
def erdbeben_skala():
    s_input = input("Welche Staerke?")
    s = float(s_input)

    if 0 <= s < 3.5:
        print("wird nicht bemerkt")
    elif 3.5 <= s < 4.5:
        print("leichte Zerstoerung")
    elif 4.5 <= s < 6.0:
        print("mittlere Zerstoerung")
    elif 6.0 <= s < 8.0:
        print("starke Zerstoerung")
    elif s >= 8.0:
        print("alles wird zerstoert")
    else:
        print("falsche Eingabe")


# S.200
def betragsfunction(x):
    return x if x >= 0 else -x


def kleiner_gauss(n):
    summe = 0
    for i in range(n + 1):
        summe += i
    return summe


def faculty(n):
    produkt = 1
    for i in range(1, n + 1):
        produkt *= i
    return produkt


def verdopplung_startkapital(k_0=1000, z=0.03):
    k = k_0
    n = 0
    while k < 2 * k_0:
        n += 1
        k = k + k * z
    return n


def quersumme(n):
    ziffern = str(n)
    quer_summe = 0
    for i in range(len(ziffern)):
        quer_summe += int(ziffern[i])
    print(f'Ziffern: {len(ziffern)}\n'
          f'Quersumme: {quer_summe}')


def babylonisches_wurzelziehen(n):
    x = n
    a = n
    e = 10 ** (-8)
    while abs(my_squirt(x, a) - x) > e:
        x = my_squirt(x, a)
        a = (2 * my_squirt(x, a) - x) * x
        if abs(my_squirt(x, a) - a) < e:
            break
    return x


def my_squirt(n, a):
    return 1 / 2 * (n + a / n)


# S. 219
def tannenbaum(h):
    output = ''
    n = 2 * h - 1
    for idx, i in enumerate(range(1, n + 1, 2)):
        output += ' ' * (n - idx) + '*' * i + '\n'
    output += ' ' * n + '*' + '\n'
    return output


def dreieck(h):
    output = ''
    n = 2 * h - 1
    for idx, i in enumerate(range(1, n + 1, 2)):
        output += ' ' * (n - idx) + '*' * i + '\n'
    return output



def diamant(h):
    output = ''
    n = 2 * h - 1
    for idx, i in enumerate(range(1, n + 1, 2)):
        output += ' ' * (n - idx) + '*' * i + '\n'
    l = len(output.split('\n'))
    for idx, i in enumerate(range(n, 0, -2)):
        if idx > 0:
            output += ' ' * (l + idx - 1) + '*' * i + '\n'
    return output


def wuerfelspiel():
    money = 10000
    zug = [0, 0, 0, 0]
    while money > 0:
        zug[0] += 1
        money -= 1
        number = randint(1, 6) + randint(1, 6)

        if number == 10:
            zug[1] += 1
            money += 1
        elif number == 11:
            zug[2] += 1
            money += 5
        elif number == 12:
            zug[3] += 1
            money += 10

        print(f'Züge:  {zug[0]}\n'
              f'Geld:   {money}\n'
              f'Summe 10: {zug[1] * 100 / zug[0]}%\n'
              f'Summe 11: {zug[2] * 100 / zug[0]}%\n'
              f'Summe 12: {zug[3] * 100 / zug[0]}%\n')


def bino(n, k):
    return faculty(n) / (faculty(k) * faculty(n - k))


def ist_dreiecks(n):
    x = - 1 / 2 + math.sqrt(1 / 4 + 2 * n)
    return True if abs(int(x) - x) < 10 ** (-8) else False


def rahmen(namen):
    output = ''
    for i in range(3):
        if i == 1:
            output += f'|{namen}|\n'
        else:
            output += '+' + '-' * len(namen) + '+\n'
    print(output)


counter = 0


# S. 235
def countUp(n):
    global counter
    counter += 1
    if n == 0:
        return
    print(counter)
    countUp(n - 1)


# S. 235
def countDown(n):
    if n == 0:
        return
    print(n)
    countDown(n - 1)


def quer_summe(n):
    pass


# S. 236
def isPalindrom(wort):
    if len(wort) <= 1:
        print('Wort ist ein Palindrom')
    elif wort[0].lower() == wort[-1].lower():
        isPalindrom(wort[1:-1])
    else:
        print('Wort ist kein Palindrom')


def fib(n):
    f1, f2 = 0, 1
    for i in range(n):
        if i == 0:
            yield f1
        elif i == 1:
            yield f2
        else:
            f1, f2 = f2, f1 + f2
            yield f2


def wuerfeln(n):
    dist = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    tries = 0
    while n > tries:
        tries += 1
        p = randint(1, 6)
        dist[p] += 1
    print(dist)

