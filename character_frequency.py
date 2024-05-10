String = input("Enter the main String: ")
pre = []
for n in String:
    occurrences = []
    start_index = 0
    while True :
        index = String.find(n, start_index)
        if index == -1:
            break
        occurrences.append(index)
        start_index = index + 1
    if n not in pre:
        pre.append(n)
        print(n, len(occurrences))
