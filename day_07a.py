import regex as re


def is_contain_abba(s):
    """
    >>> is_contain_abba('abba')
    True
    >>> is_contain_abba('xxxabba')
    True
    >>> is_contain_abba('abbaxxxx')
    True
    >>> is_contain_abba('xxabbaxx')
    True
    >>> is_contain_abba('aaaa')
    False
    >>> is_contain_abba('aaaaqwwqaaaa')
    True
    >>> is_contain_abba('aaaacca')
    True
    >>> is_contain_abba('ioxxoj')
    True

    :param s:
    :return:
    """
    for x in range(len(s)-3):
        if s[x]==s[x+3] and s[x+1]==s[x+2] and s[x]!=s[x+1]:
            return True
    return False
    #parts = re.findall(r'(.)(.)\2\1', s, overlapped=True)
    return any(m[0] != m[1] for m in parts)


def is_support(ip):
    """
    >>> is_support('abba[mnop]qrst')
    True
    >>> is_support('abcd[bddb]xyyx')
    False
    >>> is_support('aaaa[qwer]tyui')
    False
    >>> is_support('ioxxoj[asdfgh]zxcvbn')
    True
    >>> is_support('kogkhuakigjclxbjoi[yuidmmdeopwzvatxc]qdsbzscrwpmnloga[xsnwctwrdpgqvggoian]yayspjjhhpdsyzkkzx[qbttlvpkbplhagtb]ndnljzkxhgdvclz')
    False
    >>> is_support('twopcscmaiqhzsepel[qhydrqfqwvjjvinlq]tfmaoxgmccymtrbecjk[zkuwqiccdgoubccjoc]pepwccwqlxzlvuhb')
    False
    >>> is_support('unvvlzfszuuztae[ytbzbzacrvxlksvk]aeaoeugpmkydbixbmv[nzznffshspwmlkqig]hwamlnoeyfmzhrxmbi')
    False
    >>> is_support('jccjsrpjiyokryde[gfwdanjjnbycygt]iqiuzghicmveelbxp[tzugzompmkteyydyeb]bkvntycebtvjlgour')
    False

    :param ip:
    :return:
    """
    networks = re.findall("\[(.*?)\]", ip)
    address = re.split("\[.*?\]", ip)

    inside = any(map(is_contain_abba, networks))
    outside = any(map(is_contain_abba, address))
    ret = outside and not inside
    return ret


def test():
    import doctest
    failure, tests = doctest.testmod()
    print('Unittests: {ok} of {t} OK'.format(ok=tests - failure, t=tests))
    return failure == 0


def main():
    print('The answer must be 105')
    answer = sum(filter(None, map(is_support, open('data\\07a.txt').readlines())))
    print('The real answer is %d' % answer)  #
    assert answer == 105
    pass


if __name__ == '__main__':
    if test():
        main()
