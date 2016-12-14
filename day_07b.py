import regex as re
import itertools

def get_aba(ip):
    yield from (m for m in re.findall(r'(.)(.)\1', ip, overlapped=True) if m[0]!=m[1])

def is_support(ip):
    '''
    >>> is_support('aba[bab]xyz')
    True
    >>> is_support('xyx[xyx]xyx')
    False
    >>> is_support('aaa[kek]eke')
    True
    >>> is_support('zazbz[bzb]cdb')
    True

    :param ip:
    :return:
    '''
    networks = re.findall("\[(.*?)\]", ip)
    address = re.split("\[.*?\]", ip)

    x = itertools.chain(*map(get_aba, address))
    for a, b in x:
        bab = b+a+b
        if any(bab in network for network in networks):
            return True
    return False


def test():
    import doctest
    failure, tests = doctest.testmod()
    print('Unittests: {ok} of {t} OK'.format(ok=tests - failure, t=tests))
    return failure == 0


def main():
    print('The answer must be 258')
    answer = sum(filter(None, map(is_support, open('data\\07a.txt').readlines())))
    print('The real answer is %d' % answer)  #
    assert answer == 258


if __name__ == '__main__':
    if test():
        main()

