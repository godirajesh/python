String = input("Enter the main String: ")
substring = input("Enter the sub String: ")
occurrences = []
start_index = 0
while True:
    index = String.find(substring, start_index)
    if index == -1:
        break
    occurrences.append(index)
    start_index = index + 1
print(occurrences)
