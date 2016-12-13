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
    '5DB3'
    """
    moves = {
        'U': complex(0, 1), 'L': complex(-1, 0), 'R': complex(1, 0), 'D': complex(0, -1)
    }
    digits = {
                                                   complex(0, 2): '1',
                             complex(-1, 1): '2',  complex(0, 1): '3', complex(1, 1): '4',
        complex(-2, 0): '5', complex(-1, 0): '6',  complex(0, 0): '7', complex(1, 0): '8', complex(2, 0): '9',
                             complex(-1, -1): 'A', complex(0, -1): 'B', complex(1, -1): 'C',
                                                   complex(0, -2): 'D',
    }
    assert len(digits)==13
    position = complex(-2, 0)
    rc = ''
    for line in data.split('\n'):
        for char in line:
            new_position = position + moves[char]
            if new_position not in digits:
                continue
            position = new_position
        rc += str(digits[position])
    return rc


failure, tests = doctest.testmod()
print('Unittests: {ok} of {t} OK'.format(ok=tests - failure, t=tests))
print('The answer is', solve(open(r'data\02a.txt', 'r').read()))
print('The real answer is: AC8C8')
