i = 0
with open('vowels.txt') as f:
    for line in f:
        if line.count('a') == line.count('e'):
            i += 1
print(i)
