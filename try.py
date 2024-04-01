import sys
import math

input = sys.stdin.readline 

n = int(input())
layer = [['*' for _ in range(n)] for _ in range(n)]

def star(lay, n):
    if n == 1:
        return layer
    
    a = int(n/3)
    b = int(math.log(n, 3))
    m = 3 ** b
    
    for i in range(b):
        for j in range(b):
            if i == 1 and j == 1:
                continue
            z = a * i
            x = a * j
            for k in range(a):
                for l in range(a):
                    lay[z + k][x + l] = ' '
    
    return star(lay, n//3)
    
    
a = star(layer, n)
for row in a:
    print(''.join(row))
