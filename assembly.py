with open('assembly.txt') as f:
    f = f.read().split('\n')

d = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}

counter = 0

def interpret(line):
    global counter
    if len(line.split()) > 2:
        command, var, val = line.split()
    else:
        command, var = line.split()
    if command == 'inc':
        d[var] += int(val)
    elif command == 'add':
        d[var] += d[val]
    elif command == 'xor':
        d[var] = d[val] ^ d[var]
    elif command == 'jnz':
        if d[var] != 0: counter += int(val)
    elif command == 'out':
        print(chr(d[var]))


while counter < len(f):
    if f[counter]:
        interpret(f[counter])
    counter += 1
