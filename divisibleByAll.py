z=input
z()
z()
p=[int(i) for i in z().split()]
i=[int(i) for i in z().split()]
a=""
for x in i:
    g=True
    for y in p:
        if x%y>0:
            g=False
    a+='T' if g else 'F'
print(a)