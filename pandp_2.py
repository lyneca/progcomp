i = 0
with open('pandp.txt') as pandp:
    words = pandp.read().split()

for word in words:
    if len(word) > i:
        i = len(word)

print(i)
