# (c) 2021 Yannic Breiting

# S. 46, Aufgabe 3
try:
    a, b, c = (int(i) for i in (input('1.Number'), input('2.Number'), input('3.Number')))
    print((a + b) * c)
except:
    print('Invalid Argument! Must be type <int>')
