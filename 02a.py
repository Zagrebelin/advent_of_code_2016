import doctest
import re


# и снова используем комплексные числа и маленько арифметики.
# поле
# (1,-1) (1,0) (1,1)
# (0,-1) (0,0) (0,1)
# (-1,-1) (-1,0) (-1,1)
# начинаем в (0,0), прибавляем прибавку в зависимости от положения
def solve(data):
    """
    >>> solve('''ULL
    ... RRDDD
    ... LURDL
    ... UUUUD''')
    '1985'
    """
    moves = {
        'U': complex(0, 1), 'L': complex(-1, 0), 'R': complex(1, 0), 'D': complex(0, -1)
    }
    digits = [
        complex(-1, 1), complex(0, 1), complex(1, 1),
        complex(-1, 0), complex(0, 0), complex(1, 0),
        complex(-1, -1), complex(0, -1), complex(1, -1),
    ]
    position = complex(0, 0)
    rc = ''
    for line in data.split('\n'):
        for char in line:
            new_position = position + moves[char]
            if new_position not in digits:
                continue
            position = new_position
        digit = digits.index(position)+1
        rc += str(digit)
    return rc


failure, tests = doctest.testmod()
print('Unittests: {ok} of {t} OK'.format(ok=tests - failure, t=tests))
print('The answer is', solve(open(r'data\02a.txt', 'r').read()))
print('The real answer is: 78293')