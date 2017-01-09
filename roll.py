import random
def roll():
    x = random.randint(1, 6)
    y = 0
    for i in range(x):
        y += random.randint(1, 6)
    x = 0
    for i in range(y):
        x += random.randint(1, 6)
    y = 0
    for i in range(x):
        y += random.randint(1, 6)
    return y

T = 2000000
print(sum(roll() for x in range(T)) / T)


# 150.16565
