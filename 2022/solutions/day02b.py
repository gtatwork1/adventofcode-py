# Open the input file
with open("input2.txt") as f:
    # Read the lines from the file
    lines = f.readlines()

# Initialize the sum of the scores
sum = 0

# Process each line in the input
for line in lines:
    # Split the line into the two columns
    col1, col2 = line.split()

    # Calculate the score for the row
    if col2 == "X":
        score = 0
        if col1 == "A":
            score += 3
        elif col1 == "B":
            score += 1
        elif col1 == "C":
            score += 2
    elif col2 == "Y":
        score = 3
        if col1 == "A":
            score += 1
        elif col1 == "B":
            score += 2
        elif col1 == "C":
            score += 3
    elif col2 == "Z":
        score = 6
        if col1 == "A":
            score += 2
        elif col1 == "B":
            score += 3
        elif col1 == "C":
            score += 1

    # Add the score to the sum
    sum += score

    # Output the score for the row
    print("Score for row:", score)

# Output the sum of the scores
print("Sum of scores:", sum)
