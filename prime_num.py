n=int(input("Enter the Number:"))
for i in range(2,n//2):
    if (n%i==0):
        print("Not a Prime Number")
        break
else:
    print(n , "is a Prime Number")