# Initialize an empty dictionary to store string counts
string_counts = {}

# Get input string from the user
input_string = input("Enter a string: ")

# Split the input string into individual strings
strings = input_string.split( )
print(strings)
# Count the occurrences of each string
for string in strings:
    string_counts[string] = string_counts.get(string, 0) + 1
print(string_counts)
# Display the counts of each string
print("\nNumber of times each string is present:")
for string, count in string_counts.items():
    print(f"'{string}': {count}")