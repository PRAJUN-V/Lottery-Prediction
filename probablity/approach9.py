from data1 import data
a = data[-2]
b = data[-9]

sum = 0
for i in b:
    sum += i

c = sum  // len(b)

print(c in b)

