def is_triangle(a, b, c):
    return a + b > c and b + c > a and a + c > b


def solve(data):
    return sum(is_triangle(*map(int, line.split())) for line in data)


print('The corrent answer is: 982')
print('The answer is: ', solve(open(r'data\03a.txt')))
