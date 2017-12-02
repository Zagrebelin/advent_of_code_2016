from functools import lru_cache


def is_openspace(x: int, y: int, secret: int) -> bool:
    n = x * x + 3 * x + 2 * x * y + y + y * y + secret
    b = bin(n)
    ret = b.count('1') % 2
    return ret == 0

@lru_cache(maxsize=10000)
def is_wall(x, y, secret):
    return not is_openspace(x, y, secret)


cells = {(1, 1): 0}
secret = 1352
offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
st = 0
while (31, 39) not in cells:            # Part A
    st += 1
    new = []
    for cell, distance in cells.items():
        # check north, south, west and east
        for offset in offsets:
            neighbour = (cell[0] + offset[0], cell[1] + offset[1])
            if is_wall(neighbour[0], neighbour[1], secret):
                continue
            if neighbour in cells and cells[neighbour] > distance + 1:
                new.append(neighbour)
            elif neighbour not in cells:
                new.append(neighbour)
    for c in new:
        cells[c] = distance + 1

print(cells[(31,39)])                      # Part A, 90
