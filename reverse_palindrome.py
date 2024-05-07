num=int(input("Enter the number to be reversed: "))
temp=sum=0
pal=num
while(num>0):
    rem=num%10
    temp=temp*10+rem
    sum=sum+rem
    num=num//10
print("The reversed value is ",temp)
print("The Total value is ",sum)
if(pal==temp):
    print(temp," is a palindrome")