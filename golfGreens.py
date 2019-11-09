import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
pars=[]
scores=[]

for i in input().split():
    x = int(i)
    pars.append(x)
for i in input().split():
    x = int(i)
    scores.append(x)

score = 0
for x in range(len(pars)):
    score += scores[x]-pars[x]
    
print(score)