# Read the input list of number groups
groups = []
cur_group = []

while True:
    try:
        # Read the next line from standard input
        line = input()

        # If the line is empty, add the current number group to the list
        # and start a new group
        if line == "":
            groups.append(cur_group)
            cur_group = []
        else:
            # Add the current line to the current number group
            cur_group.append(int(line))
    except EOFError:
        # Stop reading when we reach the end of the input
        break

# Sum the numbers in each group and print the result
sums = []
for group in groups:
    sums.append(sum(group))
    print(sum(group))

# Print the largest sum
print("Largest sum:", max(sums))

# Sort the sums in descending order and take the top 3
top_sums = sorted(sums, reverse=True)[:3]

# Print the sum of the top 3 sums
print("Sum of top 3 sums:", sum(top_sums))
