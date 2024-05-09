l=[]
while True:
     num=int(input("Enter the value [0 to stop]: "))
     if num==0:
         break
     if num not in l:
         l.append(num)
l.sort(reverse=True)         
print(l)