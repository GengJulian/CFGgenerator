a = 1
b = 2
if a > b:
    a = b
    a += b
else:
    b = a

for i in range(100):
    if i % 2 == 0:
        i = i * 100
        continue
    else:
        b = b + i
