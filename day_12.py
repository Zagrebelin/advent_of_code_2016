data = """cpy 1 a
cpy 1 b
cpy 26 d
jnz c 2
jnz 1 5
cpy 7 c
inc d
dec c
jnz c -2
cpy a c
inc a
dec b
jnz b -2
cpy c b
dec d
jnz d -6
cpy 19 c
cpy 14 d
inc a
dec d
jnz d -2
dec c
jnz c -5"""


regs = {'a':0, 'b':0, 'c':0, 'd':0}     # part A
regs = {'a':0, 'b':0, 'c':1, 'd':0}     # part B
cmds = []
ptr = 0

def cpy(src, dst):
    global ptr
    if src in regs:
        src = regs[src]
    regs[dst] = int(src)
    ptr += 1
def inc(reg):
    global ptr
    regs[reg] += 1
    ptr += 1
def dec(reg):
    global ptr
    regs[reg] -= 1
    ptr += 1
def jnz(reg, offset):
    global ptr
    if reg in regs:
        value = regs[reg]
    else:
        value = int(reg)
    if value != 0:
        ptr += int(offset)
    else:
        ptr += 1


for line in data.split('\n'):
    op_code = line.split()[0]
    if op_code == 'cpy':
        _, value, reg = line.split()
        cmds.append((cpy, (value, reg)))
    elif op_code == 'inc':
        _, reg = line.split()
        cmds.append((inc, (reg,)))
    elif op_code == 'dec':
        _, reg = line.split()
        cmds.append((dec, (reg,)))
    elif op_code == 'jnz':
        _, reg, offset = line.split()
        cmds.append((jnz, (reg, offset)))

while ptr<len(cmds):
    op, args = cmds[ptr]
    op(*args)
print(regs)