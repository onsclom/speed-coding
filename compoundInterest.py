import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n, i, m = [int(i) for i in input().split()]

for x in range(m):
    n = n + n*(i/100)
    
print(int(n))
    