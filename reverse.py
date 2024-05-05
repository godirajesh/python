num=int(input("Enter the number to be reversed: "))
temp=0
while(num>0):
    rem=num%10
    temp=temp*10+rem
    print(rem,end='')
    num=num//10
print("\n",temp,sep='')