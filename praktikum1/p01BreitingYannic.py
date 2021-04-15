"""
Frage 1:
0 0 -> 0
0 1 -> 1
1 0 -> 1
1 1 -> 0

Frage 2:
0 0 ^ 0 -> 0 0 ^ 0 -> 0 0
0 1 ^ 1 -> 1 0 ^ 1 -> 0 1
1 0 ^ 0 -> 1 0 ^ 0 -> 1 0
1 1 ^ 1 -> 0 0 ^ 1 -> 1 1

Frage 3:
Da 65 den Buchstaben A in Ascii repräsentiert und A auf 0 gemappt wird

Frage 4:
''A!%$B!%$C''

Frage 5:
list(zip('ABC', [1, 2, 3], 'abc'))
"""


def code_iterator(code):
    """
    Code-Generator for repetitive looping through the given code.

    :param code: :str: code for encoding
    :return: :str: single letter from code
    """
    while True:
        for code_char in code:
            yield code_char


def encode(message, code):
    """
    Encodes a massage with the given code
    Function behaves self inverse with the same code

    :param message: :str: which should be encoded/decoded
    :param code: :str: for encoding logic
    :return: :str: encoded message
    """
    encoded_message = [(ord(char) - 65) ^ (ord(code_char) - 65)
                       for char, code_char in zip(message, code_iterator(code))]

    return ''.join(chr(char + 65) for char in encoded_message)


try:
    with open('C:/Users/Yanni/Documents/GitHub/ti3/praktikum1/praktikum1ext.txt', 'r') as file:
        text = file.readlines()
except Exception as e:
    print(e)

# 1. Das Codewort

zwischencode = text[5][2] + text[2][26:29] + text[1][:3] + text[-1][:3]
code_wort = (''.join(reversed(zwischencode)) * 5)[:-2][8::8]

# 2.1 Einzeichencode

botschaft1 = 'RTFVQXSSE'
code1 = 'X'

botschaft_val1 = [ord(char) - 65 for char in botschaft1]

code_val1 = ord(code1) - 65

result_val1 = [char ^ code_val1 for char in botschaft_val1]

result1 = ''.join(chr(char + 65) for char in result_val1)

# 3. Allgemeiner Code

# botschaft = 'SLCVZCILAG'
botschaft = 'SEW^Y[ELMBPEQBV'

botschaft_val = [ord(char) - 65 for char in botschaft]

code_long = (len(botschaft) // len(code_wort)) * code_wort + \
            code_wort[:len(botschaft) % len(code_wort)]

code_val = [ord(char) - 65 for char in code_long]

result_val = [bot_char ^ code_char for bot_char, code_char in zip(botschaft_val, code_val)]

result = ''.join(chr(char + 65) for char in result_val)
