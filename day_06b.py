from collections import Counter

def encode_santa(msg):
    r'''
    >>> encode_santa("eedadn\ndrvtee\neandsr\nraavrd\natevrs\ntsrnev\nsdttsa\nrasrtv\nnssdts\nntnada\nsvetve\ntesnvt\nvntsnd\nvrdear\ndvrsen\nenarar")
    'advent'

    :param msg:
    :return:
    '''
    msg = msg.split()
    verts = zip(*msg)
    counters = (Counter(vert) for vert in verts)
    less_commons = (c.most_common(26)[-1][0] for c in counters)
    ret = ''.join(less_commons)
    return ret

def test():
    import doctest
    failure, tests = doctest.testmod()
    print('Unittests: {ok} of {t} OK'.format(ok=tests - failure, t=tests))
    return failure == 0


def main():
    answer = encode_santa(open('data\\06a.txt').read())
    print('The answer must be rwqoacfz')
    print('The real answer is %s' % answer)
    assert answer == 'rwqoacfz'





if __name__ == '__main__':
    if test():
        main()

