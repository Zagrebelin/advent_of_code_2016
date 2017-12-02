import hashlib
from functools import lru_cache
import re

@lru_cache(maxsize=1100)
def hash(prefix, idx):
    s = f'{prefix}{idx}'
    # s = hashlib.md5(s.encode('ascii')).hexdigest()         # part A
    for _ in range(2017):                                    # part B
        s = hashlib.md5(s.encode('ascii')).hexdigest()       # part B
    return s


def have_3(s):
    ret = re.findall(r'(.)\1{2}', s)
    return ret[0] if ret else []

found = 0
salt = 'qzyelonm'
idx = 0


def have_5(s, threes):
    for th in threes:
        if th*5 in s:
            return True
    return False


while found<=64:
    threes = have_3(hash(salt, idx))
    if threes:
        for idx2 in range(idx+1, idx+1001):
            if have_5(hash(salt, idx2), threes):
                found += 1
                print(found, idx, hash(salt, idx), idx2, hash(salt, idx2), have_3(hash(salt, idx)))
                break
        pass
    idx += 1
# part a: 15168