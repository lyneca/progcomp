last_a = 100000000
for i in range(11058):
    i += 1
    if 11058 % i == 0:
        a = abs(11058 // i - i)
        if a < last_a:
            last_a = a

print(last_a, 11058 // last_a)
