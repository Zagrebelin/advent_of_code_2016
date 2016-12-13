import doctest
import re
from functools import total_ordering

def shift(s, cnt):
    s = s.replace('-', 'a')
    for _ in range(cnt%26):
        s = ''.join('a' if c == 'z' else ' ' if c ==' ' else chr(ord(c) + 1) for c in s)
    return s


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



def get_sector_id(s):
    """

    :param s:
    :return:
    """
    parts = re.match("(.*)-(\d+)\[(.{5})\]", s)
    name, sector_id, checksum = parts.groups()
    sector_id = int(sector_id)
    print(shift(name, sector_id), sector_id)


failure, tests = doctest.testmod()
print('Unittests: {ok} of {t} OK'.format(ok=tests - failure, t=tests))
for x in open('data\\04a.txt', 'r').readlines():
    get_sector_id(x)
