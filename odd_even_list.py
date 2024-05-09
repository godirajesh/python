l = []
odd = []
for i in range(1, 11):
    num = int(input("Enter the value"))
    if num%2 != 0:
        if num not in l:
            odd.append(num)
    else:
        l.append(num)
print(odd+l)
