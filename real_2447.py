import sys
import math
input = sys.stdin.readline 

n = 27 #int(input())
layer = [['*' for _ in range(n)]for _ in range(n)]

def star(lay, n):
    if n == 1:
        return lay
    else:
        a = int(n/3)
        b = int(math.log(n, 3))
        m = 3 % b
        try:
            if m == 0:
                m = 3 % (b-1) + 1   
        except:ZeroDivisionError
        m = 9 * m
        if n == 1:
            return 1
        for i in range(m):
            z = a + (3 * i)
            for j in range(m):
                x = a + (3 *j)
                for k in range(a):
                    for l in range(a):
                        if (z + k) < 27 and (x + l) < 27:
                            lay[z + k][x + l] = ' '
                        
        return star(lay, n/3) * int(b)
    
    
a = star(layer, n)
for i in a:
    print(''.join(i))