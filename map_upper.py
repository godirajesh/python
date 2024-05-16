def is_upper(n):
    for c in n:
        if c.isupper() == True:
            str.add(c)
    return str
nums = ["RajesH", "raJ", "Rajesgod", "GodrajEs"]
str=set()
for n in map(is_upper, nums):
    pass
print(str)
