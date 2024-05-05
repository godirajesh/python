
total=0
count=0
while True:
    value=int(input("Enter the Number(0 to stop):"))
    if value==0:
        break
    else:
        if value >0:
            total+=value
            count+=1
print("The average of positive numbers is ",total/count)