def positions(s,p):
    l=[]
    for i in range(len(s)-len(p)+1):
        same=True
        for j in range(len(p)):
            print(i)
            if p[j].upper() != s[i+j].upper() and p[j] != "?":
                same=False
                break
        if same:
            l.append(i)
    return l
print(positions("ABCD?A","A"))