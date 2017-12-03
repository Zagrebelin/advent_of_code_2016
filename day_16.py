

def generate(p):
    a = p
    b = a
    b = b[::-1]
    b = b.replace('0', 'x').replace('1', '0').replace('x', '1')
    r = f'{a}0{b}'
    return r


def cheksum(s):
    while True:
        ch = ''
        for i in range(0, len(s), 2):
            if s[i]==s[i+1]:
                ch += '1'
            else:
                ch += '0'
        if len(ch)%2==1:
            return ch
        s = ch
    return ch


def fill(length, seed):
    ret = seed
    print(length, 'a')
    while len(ret)<=length:
        ret = generate(ret)
    print(length, 'b')
    ret = ret[:length]
    print(length, 'c')
    ch = cheksum(ret)
    return ch




assert generate('1')=='100'
assert generate('1') == '100'
assert generate('0') == '001'
assert generate('11111') == '11111000000'
assert generate('111100001010') == '1111000010100101011110000'
assert cheksum('110010110100') == '100'
assert fill(20, '10000') == '01100'

print(fill(272, '01111001100111011')) # part A
print(fill(35651584, '01111001100111011')) # part B. Stupid solution, i think there must be some kind of generator.