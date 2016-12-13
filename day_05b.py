from day_05a import is_valid_password

def get_char_position(p):
    '''
    >>> get_char_position(b'abc3231929')
    (1, '5')
    >>> get_char_position(b'abc5017308')
    (None, None)
    >>> get_char_position(b'abc5357525')
    (4, 'e')


    :param p:
    :return:
    '''
    hash = is_valid_password(p)
    if not hash:
        return None, None
    position, char = int(hash[5], 16), hash[6]
    if position>=8:
        return None, None
    return position, char


def test():
    import doctest
    failure, tests = doctest.testmod()
    print('Unittests: {ok} of {t} OK'.format(ok=tests - failure, t=tests))
    return  failure==0

def main():
    x = b'reyedfim'
    idx = 0
    pwd = list('_'*8)
    while any(x =='_' for x in pwd):
        p = b'%s%d' % (x, idx)
        position, char= get_char_position(p)
        if position is not None and pwd[position]=='_':
            pwd[position] = char
            print(''.join(pwd))
        idx += 1

    print('The answer must be 863dde27')
    print('The real answer is %s' % pwd)


if __name__ == '__main__':
    if test():
        main()

