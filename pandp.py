import re
l = []
with open('pandp.txt') as f:
    for word in f.read().split():
        word = re.sub(r'[^\w\']', '', word)
        if len(word) > 5:
            l.append(word)
print(l[19])
