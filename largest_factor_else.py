n=int(input("Enter the value: "))
for i in range(n//2,1,-1):
    if(n%i==0):
        print(f"{i} is the factor")
        break
else:
    print(n ,"is a Prime Number")