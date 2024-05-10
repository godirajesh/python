s1="12,22,33,24,5"
total=0
l = s1.split(",")
for n in l:
    total+=int(n)
print(total)