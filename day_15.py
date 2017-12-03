import re

data = """Disc  # 1 has 17 positions; at time=0, it is at position 5.
Disc  # 2 has 19 positions; at time=0, it is at position 8.
Disc  # 3 has 7 positions; at time=0, it is at position 1.
Disc  # 4 has 13 positions; at time=0, it is at position 7.
Disc  # 5 has 5 positions; at time=0, it is at position 1.
Disc  # 6 has 3 positions; at time=0, it is at position 0."""

data += "\nDisc  # 7 has 11 positions; at time=0, it is at position 0." # part B

length = []
position = []
disk = []
for line in data.split('\n'):
    d, l, p = map(int,
                  re.match(r"Disc  # (\d+) has (\d+) positions; at time=0, it is at position (\d+).", line).groups())
    length.append(l)
    position.append(p)
    disk.append(d)

step = 0
while True:
    here = [(d + p + step) % l for d, p, l in zip(disk, position, length)]
    if all(h == 0 for h in here):
        break
    step += 1

print(step)  # part A = 16824, part B = 3543984
