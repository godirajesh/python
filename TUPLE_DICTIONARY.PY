list_of_tuples = [(1, 10), (2, 20), (1, 80), (3, 40), (2, 56)]
# Step 2: Extract unique keys from tuples
unique_keys = set(key for key, _ in list_of_tuples)
#print(unique_keys)
# Step 3: Create a dictionary with unique keys and initialize sum to 0
result_dict = {key: 0 for key in unique_keys}
#print(unique_keys)
for key, value in list_of_tuples:
    #result_dict[key] += value
    result_dict[key] = result_dict.get(key, 0) + value

print("Result Dictionary:")
print(result_dict)