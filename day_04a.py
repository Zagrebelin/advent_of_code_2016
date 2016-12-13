import doctest
import re
from collections import Counter
from functools import total_ordering


@total_ordering
class X:
    def __init__(self, letter, count):
        self.letter = letter
        self.count = count

    def __eq__(self, other):
        return self.letter == other.a and self.count == other.b

    def __lt__(self, other):
        return self.count > other.count or (self.count == other.count and self.letter < other.letter)

    def __repr__(self):
        return '%s = %d' % (self.letter, self.count)


def calc_checksum(s):
    """
    >>> calc_checksum('aaaaa-bbb-z-y-x')
    'abxyz'
    >>> calc_checksum('a-b-c-d-e-f-g-h')
    'abcde'
    >>> calc_checksum('not-a-real-room')
    'oarel'
    """
    c = Counter(s.replace('-', ''))
    x = [X(*a) for a in c.items()]
    xs = sorted(x)
    ret = ''.join(a.letter for a in xs[0:5])
    return ret


def get_sector_id(s):
    """
    >>> get_sector_id('aaaaa-bbb-z-y-x-123[abxyz]')
    123
    >>> get_sector_id('a-b-c-d-e-f-g-h-987[abcde]')
    987
    >>> get_sector_id('not-a-real-room-404[oarel]')
    404
    >>> get_sector_id('totally-real-room-200[decoy]')
    >>>

    :param s:
    :return:
    """
    parts = re.match("(.*)-(\d+)\[(.{5})\]", s)
    name, sector_id, checksum = parts.groups()
    if checksum == calc_checksum(name):
        return int(sector_id)
    return None


failure, tests = doctest.testmod()
print('Unittests: {ok} of {t} OK'.format(ok=tests - failure, t=tests))
rc = sum(filter(None, map(get_sector_id, open('data\\04a.txt', 'r').readlines())))
print('The answer is ', rc)
print('Answer must be 278221')
