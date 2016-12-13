import doctest
import re


# используем комплексные числа и маленько арифметики.
# координата в 2д - это комплексное число. direction - направление движения, поворот в какую-то сторону - суть умножение
# на i или -i в зависимости от стороны поворота.
def solve(data):
    """
    >>> solve('R8, R4, R4, R8')
    4

    :param data:
    :return:
    """
    turns = {
        'L': complex(0, 1),
        'R': complex(0, -1)
    }
    direction = complex(0, 1)
    position = complex(0, 0)
    visited = set()

    steps = re.findall('([LR])(\d+)', data)
    for turn_to, distance in steps:
        distance = int(distance)
        direction *= turns[turn_to]

        for walked in range(distance):
            position += direction
            if position in visited:
                return int(abs(position.real) + abs(position.imag))
            else:
                visited.add(position)
    return int(abs(position.real) + abs(position.imag))

failure, tests = doctest.testmod()
print('Unittests: {ok} of {t} OK'.format(ok=tests-failure, t=tests))
print(solve(open(r'data\01a.txt', 'r').read()))