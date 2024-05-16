def is_upper(n):
    for c in n:
        if c.isupper() == True:
            return True
nums = ["Rajesh", "raj", "rajesgod", "Godrajes"]
for n in filter(is_upper, nums):
    print(n)
