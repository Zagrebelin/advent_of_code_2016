import itertools

def is_triangle(a, b, c):
    return a + b > c and b + c > a and a + c > b


def solve(data):
    cnt = 0
    lines = [list(map(int, line.split())) for line in data]
    for i in range(0, len(lines) - 2, 3):
        l1, l2, l3 = lines[i:i + 3]
        cnt += sum(is_triangle(l1[k], l2[k], l3[k]) for k in (0,1,2))
    return cnt


print('The correct answer is: 1826')
print('The answer is: ', solve(open(r'data\03a.txt')))
