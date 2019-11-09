n = int(input())
for i in range(n):
    w = input()

    goodString = True
    for x in range(len(w)//2):
        if w[0+x] != w[len(w)-1-x]:
            goodString = False

    if goodString:
        print("true")
    else:
        print("false")