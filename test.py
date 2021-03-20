
def test_pretty_print():
    assert pretty_print((10, 27, 38, 24)) == '10 + 27*x^1 + 38*x^2 + 24*x^3'
    assert pretty_print((3, -4, 7, -9)) == '3 - 4*x^1 + 7*x^2 - 9*x^3'
    assert pretty_print((0,)) == '0'
    assert pretty_print((-1,)) == '-1'
    assert pretty_print((0, 0)) == '0 + 0*x^1'
    assert pretty_print((0, 0, -0)) == '0 + 0*x^1 + 0*x^2'
    assert pretty_print((0, -1, -4)) == '0 - 1*x^1 - 4*x^2'
    assert pretty_print(tuple()) == ''

def test_add():
    assert add((5, 5, 5, 5), (5, 5, 5, 5)) == (10, 10, 10, 10)
    assert add((5, 5, 5, 5), (-5, -5, -5, -5)) == (0, 0, 0, 0)
    assert add((0, 0, 0, 0), (0, 0, 0, 0)) == (0, 0, 0, 0)
    assert add((5, 5, 5), (-5, -5, -5, -5)) == (0, 0, 0, -5)
    assert add((5, 5, 5), ()) == (5, 5, 5)
    assert add(tuple(), tuple()) == tuple()


def pretty_print(p):
    output = ''
    for idx, coefficient in enumerate(p):
        if idx == 0:
            output += str(p[0])
        else:
            output += f' {"-" if coefficient < 0 else "+"} {abs(coefficient)}*x^{idx}'
    return output

def add(p1, p2):
    pass