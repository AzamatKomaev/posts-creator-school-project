import math


a = int(input())
b = int(input())
c = int(input())

d = b**2 - 4*a*c

x_values = []

if d > 0:
    x_values.append((-b + math.sqrt(d)) / (2 * a))
    x_values.append((-b - math.sqrt(d)) / (2 * a))
elif d == 0:
    x_values.append((-b + math.sqrt(d)) / (2 * a))
else:
    x_values.append('D меньше нуля, корней нет!')

print(*x_values)
