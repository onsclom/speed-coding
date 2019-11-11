key = input()
n = int(input())
for i in range(n):
    
    str = input()
    good = 0
    
    for x in range(len(str)):
        if str[x].lower() == key[x].lower():
            good += 1

    print("pass" if good/len(key)>=.9 else "fail")