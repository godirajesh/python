c_count = {}
while True:
    color = input(
        "Enter your favorite color (or type 'end' to finish): ").lower()
    if color == 'end':
        break
    else:
        c_count[color] = c_count.get(color, 0) + 1
print("\nNumber of users who opted for each color:")
for color, count in c_count.items():
    print(f"{color.capitalize()}: {count}")
