def greater(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c

a = 15
b = 78
c = 87

print(greater(a, b, c))