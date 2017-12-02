import re

from collections import defaultdict

bots = defaultdict(list)
outputs = {}

lines = open('data/10.txt').readlines()
for step in range(1000):
    todo = []
    for line in lines:
        # value 19 goes to bot 186
        m1 = re.match('value (\d+) goes to bot (\d+)', line)
        # bot 166 gives low to bot 93 and high to bot 75
        # bot 43 gives low to output 11 and high to output 12
        m2 = re.match('bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)', line)
        if m1:
            value, bot = m1.groups()
            value, bot = int(value), int(bot)
            bots[bot].append(value)
        elif m2:
            bot_no, low_target, low_no, high_target, high_no = m2.groups()
            bot_no, low_no, high_no = int(bot_no), int(low_no), int(high_no)
            bot = bots[bot_no]
            if len(bot) != 2:
                todo.append(line)
                continue
            found_bot = list(filter(lambda x: 61 in x[1] and 17 in x[1], bots.items()))
            # if found_bot:                 # part A
            #     print('!!!', found_bot)   # part A

            low, high = sorted(bot)
            if low_target == 'bot':
                bots[low_no].append(low)
            elif low_target == 'output':
                outputs[low_no] = low
            else:
                raise ValueError(line)
            if high_target == 'bot':
                bots[high_no].append(high)
            elif high_target == 'output':
                outputs[high_no] = high
            else:
                raise ValueError(line)
        else:
            raise ValueError(line)
    if 0 in outputs and 1 in outputs and 2 in outputs:  # part B
        print(outputs[0]*outputs[1]*outputs[2])         # part B
        die()                                           # part B
    lines = todo

