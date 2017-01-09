import re
with open('diff.c') as f:
    f = f.read()

print(len(''.join([re.sub(r'[^a-zA-Z0-9]', '', x) for x in re.findall(r'/\*.*?\*/', f, re.DOTALL)])))

# [print(x) for x in re.findall(r'/\*.*?\*/', f, re.DOTALL)]
