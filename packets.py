l = []
with open('packets.txt') as f:
    for line in f:
        if line.split()[0] == 'MSG':
            l.append(line.split()[1])
        else:
            l.remove(line.split()[1])
print(len(l))
