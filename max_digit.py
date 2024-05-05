value=int(input("Enter the value:"))
max=0
while(value>0):
    rem=value%10
    if(max<rem):
        max=rem
    value=value//10
print ("The largest is ",max)