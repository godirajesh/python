def total_nine(n):
    sum=0
    while n>0:
        rem=n%10
        sum+=rem
        n=n//10
    if sum==9:
        return True
    else:
        return False

nums = [10, 18, 27, 34, 55, 66]

for n in filter(total_nine, nums):
    print(n)