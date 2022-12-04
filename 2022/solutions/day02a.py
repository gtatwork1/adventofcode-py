# Read the input data
rows = []

while True:
    try:
        # Read the next line from standard input
        line = input()

        # Split the line into two columns
        col1, col2 = line.split(" ")

        # Calculate the score for this row
        score = 0
        if col1 == "A":
            score = 1
        elif col1 == "B":
            score = 2
        elif col1 == "C":
            score = 3

        # Add additional points based on the rules
        if col2 == "X":
            score += 0
        elif col2 == "Y":
            score += 3
        elif col2 == "Z":
            score += 6

        # Add the score for this row to the list of scores
        rows.append(score)
    except EOFError:
        # Stop reading when we reach the end of the input
        break

# Output the sum of the scores for each row
for score in rows:
    print(score)

# Output the overall sum of all scores
print("Overall sum:", sum(rows))
