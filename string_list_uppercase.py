s="My Name is RajesH"
l=[]
for c in s:
    if (c.isupper()==True and c not in l):
        l.append(c)
print(l)