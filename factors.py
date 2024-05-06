import os
os.system('cls||clear')
print("Factors")
val=int(input("Enter the value: "))
print("The factors of ",val,"are:")
for i in range(1, val + 1):
       if val % i == 0:
           print(i,end=" ")