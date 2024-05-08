s=input("Enter the String:")
count=0
for c in s:
    if c.isupper():
        count+=1
print(count)