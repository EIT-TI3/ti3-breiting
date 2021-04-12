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
'!%$ABC'

Frage 5:
list(zip(['A', 'B', 'C'], [1, 2, 3], ['a', 'b', 'c']))
"""

try:
    with open('C:/Users/Yanni/Documents/GitHub/ti3/praktikum1/praktikum1.txt', 'r') as file:
        text = file.readlines()
except Exception as e:
    print(e)


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
    function behaves self inverse with the same code

    :param message: :str: which should be encoded/decoded
    :param code: :str: for encoding logic
    :return: :str: encoded message
    """
    encoded_message = [(ord(char) - 65) ^ (ord(code_char) - 65) for char, code_char in
                       zip(message, code_iterator(code))]

    return ''.join([chr(char + 65) for char in encoded_message])


# 1. Das Codewort

zwischencode = text[5][2] + text[2][26:29] + text[1][:3] + text[-1][:3]
code_wort = (''.join(reversed(zwischencode)) * 5)[:-2][8::8]


# 2.1 Einzeichencode

botschaft1 = 'RTFVQXSSE'
code1 = 'X'

botschaft_val1 = [ord(char) - 65 for char in botschaft1]

code_val1 = [ord(code1) - 65]

result_val1 = [char ^ code_val1[0] for char in botschaft_val1]

result1 = ''.join([chr(char + 65) for char in result_val1])


# 3. Allgemeiner Code

botschaft = 'SLCVZCILAG'

botschaft_val = [ord(char) - 65 for char in botschaft]

code_long = divmod(len(botschaft), len(code_wort))[0] * code_wort + code_wort[
                                                                    :divmod(len(botschaft), len(code_wort))[1]]

code_val = [ord(char) - 65 for char in code_long]

result_val = [char ^ code_char for char, code_char in zip(botschaft_val, code_val)]

result = ''.join([chr(char + 65) for char in result_val])
