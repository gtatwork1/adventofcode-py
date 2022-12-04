# Open the input file
with open("in03.txt") as f:
    # Read the lines from the file
    lines = f.readlines()

# Initialize the sum of the values
sum = 0

# Process each line in the input
for line in lines:
    # Split the line into two equal-length strings
    s1, s2 = line[:len(line)//2], line[len(line)//2:]

    # Find the common letter that appears in both strings
    common = ""
    for c1 in s1:
        for c2 in s2:
            if c1 == c2:
                common = c1
                break

    # Calculate the value of the common letter
    if "a" <= common <= "z":
        value = ord(common) - ord("a") + 1
    elif "A" <= common <= "Z":
        value = ord(common) - ord("A") + 27
    else:
        value = 0

    # Add the value to the sum
    sum += value

    # Output the value for this row
    print("Value for row:", value)

# Output the sum
print("Sum of values:", sum)
