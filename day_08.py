import numpy as np
import re
import matplotlib.pyplot as plt


def test():
    import doctest
    failure, tests = doctest.testmod()
    print('Unittests: {ok} of {t} OK'.format(ok=tests - failure, t=tests))
    return failure == 0


def rect(screen, a, b):
    '''
    >>> rect(np.zeros((3, 7), dtype=np.int), 3, 2)
    array([[1, 1, 1, 0, 0, 0, 0],
           [1, 1, 1, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0]])

    :param screen:
    :param a:
    :param b:
    :return:
    '''
    screen[0:b, 0:a] = 1
    return screen


def rotate_column(screen, x, by):
    '''
    >>> rotate_column(rect(np.zeros((3, 7), dtype=np.int), 3, 2), 1, 1)
    array([[1, 0, 1, 0, 0, 0, 0],
           [1, 1, 1, 0, 0, 0, 0],
           [0, 1, 0, 0, 0, 0, 0]])
    >>> rotate_column(rotate_row(rotate_column(rect(np.zeros((3, 7), dtype=np.int), 3, 2), 1, 1), 0, 4), 1, 1)
    array([[0, 1, 0, 0, 1, 0, 1],
           [1, 0, 1, 0, 0, 0, 0],
           [0, 1, 0, 0, 0, 0, 0]])

    :param screen:
    :param x:
    :param by:
    :return:
    '''
    screen[:, x] = np.roll(screen[:, x], by)
    return screen


def rotate_row(screen, y, by):
    '''
    >>> rotate_row(rotate_column(rect(np.zeros((3, 7), dtype=np.int), 3, 2), 1, 1), 0, 4)
    array([[0, 0, 0, 0, 1, 0, 1],
           [1, 1, 1, 0, 0, 0, 0],
           [0, 1, 0, 0, 0, 0, 0]])
    >>> rotate_row(rotate_column(rect(np.zeros((3, 7), dtype=np.int), 3, 2), 1, 1), 0, 5)
    array([[1, 0, 0, 0, 0, 1, 0],
           [1, 1, 1, 0, 0, 0, 0],
           [0, 1, 0, 0, 0, 0, 0]])

    :param screen:
    :param y:
    :param by:
    :return:
    '''
    screen[y] = np.roll(screen[y], by)
    return screen


def show(screen, step=-1):
    plt.show(screen)
    plt.imsave('x%s.png' % ('%03d'%step if step>=0 else ''), screen)
    for row in screen:
        print(''.join('X' if cell else '.' for cell in row))
    print('')


def main():
    screen = np.zeros((8, 50), dtype=np.int)
    for step, line in enumerate(open('data\\08a.txt')):
        command = line.split(' ')[0]
        if command == 'rect':
            a, b = map(int, re.match('rect (\d+)x(\d+)', line).groups())
            rect(screen, a, b)
        elif command == 'rotate':
            direction, row, by = re.match('rotate (\S+) .=(\d+) by (\d+)', line).groups()
            if direction == 'row':
                rotate_row(screen, int(row), int(by))
            elif direction == 'column':
                rotate_column(screen, int(row), int(by))
            else:
                raise ValueError(line)
        else:
            raise ValueError(line)
    ret = 0
    ret = np.count_nonzero(screen)
    show(screen)
    print('The answer must be 115')
    print('The real answer is %s' % '', ret)
    assert ret == 115


if __name__ == '__main__':
    if test():
        main()
