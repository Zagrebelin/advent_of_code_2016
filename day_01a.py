import doctest
import re


# используем комплексные числа и маленько арифметики.
# координата в 2д - это комплексное число. direction - направление движения, поворот в какую-то сторону - суть умножение
# на i или -i в зависимости от стороны поворота.
def solve(data):
    """
    >>> solve('R2, L3')
    5
    >>> solve('R2, R2, R2')
    2
    >>> solve('R5, L5, R5, R3')
    12

    :param data:
    :return:
    """
    turns = {
        'L': complex(0, 1),
        'R': complex(0, -1)
    }
    direction = complex(0, 1)
    position = complex(0, 0)

    steps = re.findall('([LR])(\d+)', data)
    for turn_to, distance in steps:
        distance = int(distance)
        direction *= turns[turn_to]
        position += distance*direction
    return int(abs(position.real) + abs(position.imag))

failure, tests = doctest.testmod()
print('Unittests: {ok} of {t} OK'.format(ok=tests-failure, t=tests))
print(solve(open(r'data\01a.txt', 'r').read()))