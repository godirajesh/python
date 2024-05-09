s=input("Enter the String 1:")
s1=input("Enter the String 2:")
l=[]
for c in s:
    if (c in s1 and c not in l):
        l.append(c)
print(l)     